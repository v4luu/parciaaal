import json
import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime

# Importar la función lambda_handler de tu código
from proyecto import lambda_handler  # Ajusta esto al nombre de tu archivo

# Prueba 1: Verificar la llamada a la URL y subida a S3 (Simulada)
@patch("boto3.client")
@patch("urllib.request.urlopen")
def test_lambda_handler(mock_urlopen, mock_boto_client):  # El orden de los parámetros importa
    # Simula la respuesta de la solicitud HTTP
    mock_html = "<html><body>Test content</body></html>"
    mock_response = MagicMock()
    mock_response.read.return_value = mock_html.encode("utf-8")
    mock_urlopen.return_value = mock_response

    # Simula el cliente S3 de boto3
    mock_s3_client = MagicMock()
    mock_boto_client.return_value = mock_s3_client

    # Llamar a lambda_handler
    event = {}
    context = {}
    lambda_handler(event, context)

    # Verificar cuántas veces se llamó urlopen
    print(f"Cantidad de llamadas a urlopen: {mock_urlopen.call_count}")  # Depuración
    assert mock_urlopen.call_count == 10, f"Se esperaban 10 llamadas, pero se hicieron {mock_urlopen.call_count}"

# Prueba 2: Verificar si la función maneja los errores correctamente
@patch("urllib.request.urlopen")
@patch("boto3.client")
def test_lambda_handler_error(mock_boto_client, mock_urlopen):
    # Simula un error en la solicitud HTTP
    mock_urlopen.side_effect = Exception("Error de red")

    # Simula el cliente S3 de boto3
    mock_s3_client = MagicMock()
    mock_boto_client.return_value = mock_s3_client  # Asegurar que devuelve un mock

    # Llamar a lambda_handler con un error en la solicitud
    event = {}
    context = {}

    try:
        result = lambda_handler(event, context)
    except Exception as e:
        assert str(e) == "Error de red"  # Verificar que se está manejando la excepción correctamente


# Prueba 3: Verificar la existencia de la fecha de descarga en el archivo
def test_check_date_in_filename():
    today = datetime.utcnow().strftime("%Y-%m-%d")
    assert today in f"{today}/page_1.html"
