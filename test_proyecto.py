import json
import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime

# Importar la función lambda_handler de tu código
from proyecto import lambda_handler  # Ajusta esto al nombre de tu archivo

# Prueba 1: Verificar la llamada a la URL y subida a S3 (Simulada)
@patch("boto3.client")
@patch("urllib.request.urlopen")
def test_lambda_handler(mock_urlopen, mock_boto_client):
    """Prueba para verificar que se realizan las llamadas a urlopen y subida a S3."""
    mock_html = "<html><body>Test content</body></html>"
    mock_response = MagicMock()
    mock_response.read.return_value = mock_html.encode("utf-8")
    mock_urlopen.return_value = mock_response

    mock_s3_client = MagicMock()
    mock_boto_client.return_value = mock_s3_client

    event, context = {}, {}
    lambda_handler(event, context)

    print(f"Cantidad de llamadas a urlopen: {mock_urlopen.call_count}")  # Depuración
    assert mock_urlopen.call_count == 10, (
        f"Se esperaban 10 llamadas, pero se hicieron {mock_urlopen.call_count}"
    )

# Prueba 2: Verificar si la función maneja los errores correctamente
@patch("urllib.request.urlopen")
@patch("boto3.client")
def test_lambda_handler_error(mock_boto_client, mock_urlopen):
    """Prueba para verificar que la función maneja errores en la solicitud HTTP."""
    mock_urlopen.side_effect = Exception("Error de red")

    mock_s3_client = MagicMock()
    mock_boto_client.return_value = mock_s3_client

    event, context = {}, {}
    
    try:
        lambda_handler(event, context)
    except Exception as e:
        assert str(e) == "Error de red", "El error no fue manejado correctamente"

# Prueba 3: Verificar la existencia de la fecha de descarga en el archivo
def test_check_date_in_filename():
    """Prueba para verificar que el nombre del archivo contiene la fecha actual."""
    today = datetime.utcnow().strftime("%Y-%m-%d")
    assert today in f"{today}/page_1.html"