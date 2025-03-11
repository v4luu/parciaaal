import json
import boto3
import csv
import io
from bs4 import BeautifulSoup
from datetime import datetime


def lambda_handler(event, context):
    """Maneja el evento de S3 y extrae datos de propiedades desde archivos HTML."""
    print("Evento recibido:", json.dumps(event, indent=2))  # Depuración

    if "Records" not in event or not event["Records"]:
        print("El evento no contiene 'Records'.")
        return {
            "statusCode": 400,
            "body": "Evento incorrecto. Se esperaba una notificación de S3.",
        }

    s3_client = boto3.client("s3")
    bucket_origen = event["Records"][0]["s3"]["bucket"]["name"]
    target_bucket = "paginaspruebas"
    carpeta_origen = "2025-03-10/"

    try:
        csv_buffer = io.StringIO()
        csv_writer = csv.writer(csv_buffer)
        csv_writer.writerow(
            ["FechaDescarga", "Barrio", "Valor", "NumHabitaciones", "NumBanos", "mts2"]
        )

        page_number = 1
        while True:
            archivo_html = f"{carpeta_origen}page_{page_number}.html"
            print(f"Procesando archivo: {archivo_html}")
            try:
                response = s3_client.get_object(Bucket=bucket_origen, Key=archivo_html)
                html_content = response["Body"].read().decode("utf-8")
                soup = BeautifulSoup(html_content, "html.parser")
                propiedades = soup.find_all("div", class_="listing-card__content")

                if not propiedades:
                    print(f"No se encontraron propiedades en {archivo_html}, finalizando.")
                    break

                for casa in propiedades:
                    try:
                        fecha_descarga = datetime.utcnow().strftime("%Y-%m-%d")
                        barrio = casa.find("div", class_="listing-card__location__geo")
                        valor = casa.find("span", class_="price__actual")
                        num_habitaciones = casa.find("p", {"data-test": "bedrooms"})
                        num_banos = casa.find("p", {"data-test": "bathrooms"})
                        mts2 = casa.find("p", {"data-test": "floor-area"})

                        csv_writer.writerow(
                            [
                                fecha_descarga,
                                barrio.text.strip() if barrio else "N/A",
                                valor.text.strip() if valor else "N/A",
                                num_habitaciones.text.strip()
                                if num_habitaciones
                                else "N/A",
                                num_banos.text.strip() if num_banos else "N/A",
                                mts2.text.strip() if mts2 else "N/A",
                            ]
                        )
                    except Exception as e:
                        print(f"Error al extraer datos de una propiedad: {str(e)}")
                        continue

                page_number += 1
            except s3_client.exceptions.NoSuchKey:
                print(f"No se encontró el archivo {archivo_html}. Terminando proceso.")
                break

        if csv_buffer.getvalue().strip():
            csv_filename = f"{datetime.utcnow().strftime('%Y-%m-%d')}.csv"
            csv_key = csv_filename
            s3_client.put_object(
                Bucket=target_bucket,
                Key=csv_key,
                Body=csv_buffer.getvalue(),
                ContentType="text/csv",
            )
            print(f"Archivo guardado en s3://{target_bucket}/{csv_key}")
            return {
                "statusCode": 200,
                "body": json.dumps(f"Datos guardados en {target_bucket}/{csv_key}"),
            }

        print("No se extrajeron datos de propiedades.")
        return {"statusCode": 200, "body": json.dumps("No se extrajeron datos.")}

    except Exception as e:
        print(f"Error procesando el archivo: {str(e)}")
        return {"statusCode": 500, "body": json.dumps(f"Error interno: {str(e)}")}
