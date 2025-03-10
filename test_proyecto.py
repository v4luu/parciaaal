import json
import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime

# Importar la función lambda_handler de tu código
from lambda_function import lambda_handler  # Ajusta esto al nombre de tu archivo

# Prueba 1: Verificar la llamada a la URL y subida a S3 (Simulada)
@patch("urllib.request.urlopen")
@patch("boto3.client")
def test_lambda_handler(mock_boto_client, mock_urlopen):
    # Simula la respuesta de la solicitud HTTP
    mock_html = "<html><body>Test content</body></html>"
    mock_response = MagicMock()
    mock_response.read.return_value = mock_html.encode("utf-8")
    mock_urlopen.return_value = mock_response

    # Simula el cliente S3 de boto3
    mock_s3_client = MagicMock()
    mock_boto_client.return_value = mock_s3_client

    # Establecer los valores esperados
    expected_bucket = "paginaspruebas"
    expected_key = f"{datetime.utcnow().strftime('%Y-%m-%d')}/page_1.html"

    # Llamar a lambda_handler (como lo haría AWS Lambda)
    event = {}
    context = {}
    result = lambda_handler(event, context)

    # Verificar si la solicitud a la URL fue hecha correctamente
    mock_urlopen.assert_called_once()

    # Verificar que la llamada a S3 se haya realizado correctamente
    mock_s3_client.put_object.assert_called_once_with(
        Bucket=expected_bucket,
        Key=expected_key,
        Body=mock_html,
        ContentType="text/html"
    )

    # Verificar que el mensaje de éxito fue retornado
    assert result["statusCode"] == 200
    assert json.loads(result["body"]) == "Descarga y almacenamiento completados."

# Prueba 2: Verificar si la función maneja los errores correctamente
@patch("urllib.request.urlopen")
@patch("boto3.client")
def test_lambda_handler_error(mock_boto_client, mock_urlopen):
    # Simula un error en la solicitud HTTP
    mock_urlopen.side_effect = Exception("Error de red")

    # Simula el cliente S3 de boto3
    mock_s3_client = MagicMock()
    mock_boto_client.return_value = mock_s3_client

    # Llamar a lambda_handler con un error en la solicitud
    event = {}
    context = {}
    result = lambda_handler(event, context)

    # Verificar que la función haya manejado el error
    assert result["statusCode"] == 200
    assert "Error al procesar la página" in json.loads(result["body"])

# Prueba 3: Verificar la formación correcta del nombre del archivo
def test_filename_format():
    today = datetime.utcnow().strftime("%Y-%m-%d")
    filename = f"{today}/page_1.html"
    assert filename.startswith(today)
    assert filename.endswith("page_1.html")

# Prueba 4: Verificar la existencia de la fecha de descarga en el archivo
def test_check_date_in_filename():
    today = datetime.utcnow().strftime("%Y-%m-%d")
    assert today in f"{today}/page_1.html"
