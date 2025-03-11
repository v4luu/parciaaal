import json
import urllib.request
import boto3
from datetime import datetime

def lambda_handler(event, context):
    """Función principal de Lambda para descargar páginas y guardarlas en S3."""
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": (
            "text/html,application/xhtml+xml,application/xml;q=0.9," 
            "image/webp,*/*;q=0.8"
        ),
        "Connection": "keep-alive",
    }

    cookies = {"captcha_token": "your_captcha_solution"}
    s3_bucket = "paginaspruebas"
    base_url = (
        "https://casas.mitula.com.co/find?operationType=sell&geoId="
        "mitula-CO-poblacion-0000014156&text=Bogot%C3%A1%2C++%28Cundinamarca%29&page={}"
    )
    s3_client = boto3.client("s3")
    today = datetime.utcnow().strftime("%Y-%m-%d")

    for page in range(1, 11):  # Descargar 10 páginas
        url = base_url.format(page)
        print(f"Descargando: {url}")
        try:
            req = urllib.request.Request(url, headers=headers)
            req.add_header("Cookie", f"captcha_token={cookies['captcha_token']}")
            
            with urllib.request.urlopen(req) as response:
                html_content = response.read().decode("utf-8")
                file_name = f"{today}/page_{page}.html"
                s3_key = file_name
                
                s3_client.put_object(
                    Bucket=s3_bucket,
                    Key=s3_key,
                    Body=html_content,
                    ContentType="text/html",
                )
                print(f"Guardado en S3: s3://{s3_bucket}/{s3_key}")
        except Exception as e:
            print(f"Error al procesar la página {page}: {e}")

    return {"statusCode": 200, "body": json.dumps("Descarga y almacenamiento completados.")}
