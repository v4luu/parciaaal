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
    response = lambda_handler(event, context)

    assert response["statusCode"] == 200, "La función lambda no retornó un código 200."

    assert mock_urlopen.call_count == 10, (
        f"Se esperaban 10 llamadas, pero se hicieron {mock_urlopen.call_count}"
    )


# Prueba 2: Verificar si la función maneja los errores correctamente
@patch("boto3.client")
@patch("urllib.request.urlopen")
def test_lambda_handler_error(mock_urlopen, mock_boto_client):
    """Prueba para verificar que la función maneja errores en la solicitud HTTP."""
    mock_urlopen.side_effect = Exception("Error de red")

    mock_s3_client = MagicMock()
    mock_boto_client.return_value = mock_s3_client

    event, context = {}, {}
    response = lambda_handler(event, context)

    assert response["statusCode"] == 500, "No se manejó correctamente el error de red."
    assert "Error de red" in response["body"], "El mensaje de error no es el esperado."


# Prueba 3: Verificar la existencia de la fecha de descarga en el archivo
def test_check_date_in_filename():
    """Prueba para verificar que el nombre del archivo contiene la fecha actual."""
    today = datetime.utcnow().strftime("%Y-%m-%d")
    assert today in f"{today}/page_1.html", "La fecha no está presente en el nombre del archivo."
