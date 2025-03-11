import json
import boto3
import csv
from bs4 import BeautifulSoup
from datetime import datetime
import io

def lambda_handler(event, context):
    print("Evento recibido:", json.dumps(event, indent=2))  # Depuración
    
    # Verificar si "Records" está en event
    if "Records" not in event or not event["Records"]:
        print("El evento no contiene 'Records'.")
        return {
            "statusCode": 400,
            "body": "Evento incorrecto. Se esperaba una notificación de S3."
        }
    
    s3_client = boto3.client("s3")
    bucket_origen = event["Records"][0]["s3"]["bucket"]["name"]
    archivo = event["Records"][0]["s3"]["object"]["key"]
    print(f"Bucket de origen: {bucket_origen}, Archivo: {archivo}")
    
    target_bucket = "paginaspruebas"
    carpeta_origen = "2025-03-10/"  # Carpeta donde están los archivos HTML
    
    try:
        # Crear el buffer del CSV y el escritor
        csv_buffer = io.StringIO()  # Buffer en memoria para escribir el CSV
        csv_writer = csv.writer(csv_buffer)  # Crear el escritor para el CSV
        
        # Escribir los encabezados en el archivo CSV
        csv_writer.writerow(["FechaDescarga", "Barrio", "Valor", "NumHabitaciones", "NumBanos", "mts2"])
        
        # Iterar sobre los archivos de las páginas
        page_number = 1  # Empezamos con la primera página
        while True:
            # Generar el nombre del archivo para cada página
            archivo_html = f"{carpeta_origen}page_{page_number}.html"
            print(f"Procesando archivo: {archivo_html}")
            
            try:
                # Descargar el archivo HTML correspondiente
                response = s3_client.get_object(Bucket=bucket_origen, Key=archivo_html)
                html_content = response['Body'].read().decode("utf-8")
                
                # Parsear el HTML con BeautifulSoup
                soup = BeautifulSoup(html_content, "html.parser")
                
                # Extraer los datos de las propiedades
                propiedades = soup.find_all("div", class_="listing-card__content")
                if not propiedades:
                    print(f"No se encontraron propiedades en {archivo_html}, finalizando.")
                    break  # Si no hay propiedades, se termina la iteración
                
                # Procesar los datos de cada propiedad
                for casa in propiedades:
                    try:
                        # Fecha de descarga
                        fecha_descarga = datetime.utcnow().strftime("%Y-%m-%d")
                        
                        # Barrio (Ubicación)
                        barrio = casa.find("div", class_="listing-card__location__geo")
                        barrio = barrio.text.strip() if barrio else "N/A"
                        
                        # Precio (Valor)
                        valor = casa.find("span", class_="price__actual")
                        valor = valor.text.strip() if valor else "N/A"
                        
                        # Número de habitaciones
                        num_habitaciones = casa.find("p", {"data-test": "bedrooms"})
                        num_habitaciones = num_habitaciones.text.strip() if num_habitaciones else "N/A"
                        
                        # Número de baños
                        num_banos = casa.find("p", {"data-test": "bathrooms"})
                        num_banos = num_banos.text.strip() if num_banos else "N/A"
                        
                        # Área (en mts²)
                        mts2 = casa.find("p", {"data-test": "floor-area"})
                        mts2 = mts2.text.strip() if mts2 else "N/A"
                        
                        # Escribir la fila de datos en el buffer CSV
                        csv_writer.writerow([fecha_descarga, barrio, valor, num_habitaciones, num_banos, mts2])
                    
                    except Exception as e:
                        print(f"Error al extraer datos de una propiedad: {str(e)}")
                        continue
                
                # Aumentar el número de página
                page_number += 1
            
            except s3_client.exceptions.NoSuchKey:
                # Si no existe el archivo, terminar el bucle
                print(f"No se encontró el archivo {archivo_html}. Terminando proceso.")
                break

        # Subir el CSV a S3 solo si hay datos
        if csv_buffer.getvalue().strip():  # Comprobar que el buffer tiene datos
            # Nombre del archivo CSV
            csv_filename = f"{datetime.utcnow().strftime('%Y-%m-%d')}.csv"
            csv_key = csv_filename  # No se usa una carpeta
            
            # Subir el CSV a S3
            s3_client.put_object(
                Bucket=target_bucket,
                Key=csv_key,
                Body=csv_buffer.getvalue(),
                ContentType="text/csv"
            )
            print(f"Archivo guardado en s3://{target_bucket}/{csv_key}")
        
        else:
            print("No se extrajeron datos de propiedades.")
        
        return {
            "statusCode": 200,
            "body": json.dumps(f"Proceso completado. Datos guardados en {target_bucket}/{csv_key}")
        }
    
    except Exception as e:
        print(f"Error procesando el archivo: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps(f"Error interno del servidor: {str(e)}")
        }
