{"filter":false,"title":"test_proyecto.py","tooltip":"/test_proyecto.py","undoManager":{"mark":33,"position":33,"stack":[[{"start":{"row":0,"column":0},"end":{"row":77,"column":0},"action":"insert","lines":["import json","import pytest","from unittest.mock import patch, MagicMock","from datetime import datetime","","# Importar la función lambda_handler de tu código","from lambda_function import lambda_handler  # Ajusta esto al nombre de tu archivo","","# Prueba 1: Verificar la llamada a la URL y subida a S3 (Simulada)","@patch(\"urllib.request.urlopen\")","@patch(\"boto3.client\")","def test_lambda_handler(mock_boto_client, mock_urlopen):","    # Simula la respuesta de la solicitud HTTP","    mock_html = \"<html><body>Test content</body></html>\"","    mock_response = MagicMock()","    mock_response.read.return_value = mock_html.encode(\"utf-8\")","    mock_urlopen.return_value = mock_response","","    # Simula el cliente S3 de boto3","    mock_s3_client = MagicMock()","    mock_boto_client.return_value = mock_s3_client","","    # Establecer los valores esperados","    expected_bucket = \"paginaspruebas\"","    expected_key = f\"{datetime.utcnow().strftime('%Y-%m-%d')}/page_1.html\"","","    # Llamar a lambda_handler (como lo haría AWS Lambda)","    event = {}","    context = {}","    result = lambda_handler(event, context)","","    # Verificar si la solicitud a la URL fue hecha correctamente","    mock_urlopen.assert_called_once()","","    # Verificar que la llamada a S3 se haya realizado correctamente","    mock_s3_client.put_object.assert_called_once_with(","        Bucket=expected_bucket,","        Key=expected_key,","        Body=mock_html,","        ContentType=\"text/html\"","    )","","    # Verificar que el mensaje de éxito fue retornado","    assert result[\"statusCode\"] == 200","    assert json.loads(result[\"body\"]) == \"Descarga y almacenamiento completados.\"","","# Prueba 2: Verificar si la función maneja los errores correctamente","@patch(\"urllib.request.urlopen\")","@patch(\"boto3.client\")","def test_lambda_handler_error(mock_boto_client, mock_urlopen):","    # Simula un error en la solicitud HTTP","    mock_urlopen.side_effect = Exception(\"Error de red\")","","    # Simula el cliente S3 de boto3","    mock_s3_client = MagicMock()","    mock_boto_client.return_value = mock_s3_client","","    # Llamar a lambda_handler con un error en la solicitud","    event = {}","    context = {}","    result = lambda_handler(event, context)","","    # Verificar que la función haya manejado el error","    assert result[\"statusCode\"] == 200","    assert \"Error al procesar la página\" in json.loads(result[\"body\"])","","# Prueba 3: Verificar la formación correcta del nombre del archivo","def test_filename_format():","    today = datetime.utcnow().strftime(\"%Y-%m-%d\")","    filename = f\"{today}/page_1.html\"","    assert filename.startswith(today)","    assert filename.endswith(\"page_1.html\")","","# Prueba 4: Verificar la existencia de la fecha de descarga en el archivo","def test_check_date_in_filename():","    today = datetime.utcnow().strftime(\"%Y-%m-%d\")","    assert today in f\"{today}/page_1.html\"",""],"id":32}],[{"start":{"row":6,"column":5},"end":{"row":6,"column":20},"action":"remove","lines":["lambda_function"],"id":33},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["p"]},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["r"]},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["o"]},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["y"]},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["e"]},{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":["c"]},{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":["t"]}],[{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["o"],"id":34}],[{"start":{"row":66,"column":0},"end":{"row":72,"column":0},"action":"remove","lines":["# Prueba 3: Verificar la formación correcta del nombre del archivo","def test_filename_format():","    today = datetime.utcnow().strftime(\"%Y-%m-%d\")","    filename = f\"{today}/page_1.html\"","    assert filename.startswith(today)","    assert filename.endswith(\"page_1.html\")",""],"id":35},{"start":{"row":65,"column":0},"end":{"row":66,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":70,"column":0},"action":"remove","lines":["import json","import pytest","from unittest.mock import patch, MagicMock","from datetime import datetime","","# Importar la función lambda_handler de tu código","from proyecto import lambda_handler  # Ajusta esto al nombre de tu archivo","","# Prueba 1: Verificar la llamada a la URL y subida a S3 (Simulada)","@patch(\"urllib.request.urlopen\")","@patch(\"boto3.client\")","def test_lambda_handler(mock_boto_client, mock_urlopen):","    # Simula la respuesta de la solicitud HTTP","    mock_html = \"<html><body>Test content</body></html>\"","    mock_response = MagicMock()","    mock_response.read.return_value = mock_html.encode(\"utf-8\")","    mock_urlopen.return_value = mock_response","","    # Simula el cliente S3 de boto3","    mock_s3_client = MagicMock()","    mock_boto_client.return_value = mock_s3_client","","    # Establecer los valores esperados","    expected_bucket = \"paginaspruebas\"","    expected_key = f\"{datetime.utcnow().strftime('%Y-%m-%d')}/page_1.html\"","","    # Llamar a lambda_handler (como lo haría AWS Lambda)","    event = {}","    context = {}","    result = lambda_handler(event, context)","","    # Verificar si la solicitud a la URL fue hecha correctamente","    mock_urlopen.assert_called_once()","","    # Verificar que la llamada a S3 se haya realizado correctamente","    mock_s3_client.put_object.assert_called_once_with(","        Bucket=expected_bucket,","        Key=expected_key,","        Body=mock_html,","        ContentType=\"text/html\"","    )","","    # Verificar que el mensaje de éxito fue retornado","    assert result[\"statusCode\"] == 200","    assert json.loads(result[\"body\"]) == \"Descarga y almacenamiento completados.\"","","# Prueba 2: Verificar si la función maneja los errores correctamente","@patch(\"urllib.request.urlopen\")","@patch(\"boto3.client\")","def test_lambda_handler_error(mock_boto_client, mock_urlopen):","    # Simula un error en la solicitud HTTP","    mock_urlopen.side_effect = Exception(\"Error de red\")","","    # Simula el cliente S3 de boto3","    mock_s3_client = MagicMock()","    mock_boto_client.return_value = mock_s3_client","","    # Llamar a lambda_handler con un error en la solicitud","    event = {}","    context = {}","    result = lambda_handler(event, context)","","    # Verificar que la función haya manejado el error","    assert result[\"statusCode\"] == 200","    assert \"Error al procesar la página\" in json.loads(result[\"body\"])","","# Prueba 4: Verificar la existencia de la fecha de descarga en el archivo","def test_check_date_in_filename():","    today = datetime.utcnow().strftime(\"%Y-%m-%d\")","    assert today in f\"{today}/page_1.html\"",""],"id":36},{"start":{"row":0,"column":0},"end":{"row":70,"column":0},"action":"insert","lines":["import json","import pytest","from unittest.mock import patch, MagicMock","from datetime import datetime","","# Importar la función lambda_handler de tu código","from proyecto import lambda_handler  # Ajusta esto al nombre de tu archivo","","# Prueba 1: Verificar la llamada a la URL y subida a S3 (Simulada)","@patch(\"urllib.request.urlopen\")","@patch(\"boto3.client\")","def test_lambda_handler(mock_boto_client, mock_urlopen):","    # Simula la respuesta de la solicitud HTTP","    mock_html = \"<html><body>Test content</body></html>\"","    mock_response = MagicMock()","    mock_response.read.return_value = mock_html.encode(\"utf-8\")","    mock_urlopen.return_value = mock_response","","    # Simula el cliente S3 de boto3","    mock_s3_client = MagicMock()","    mock_boto_client.return_value = mock_s3_client","","    # Establecer los valores esperados","    expected_bucket = \"paginaspruebas\"","    expected_key = f\"{datetime.utcnow().strftime('%Y-%m-%d')}/page_1.html\"","","    # Llamar a lambda_handler (como lo haría AWS Lambda)","    event = {}","    context = {}","    result = lambda_handler(event, context)","","    # Verificar si la solicitud a la URL fue hecha correctamente","    mock_urlopen.assert_called_once()","","    # Verificar que la llamada a S3 se haya realizado correctamente","    mock_s3_client.put_object.assert_called_once_with(","        Bucket=expected_bucket,","        Key=expected_key,","        Body=mock_html,","        ContentType=\"text/html\"","    )","","    # Verificar que el mensaje de éxito fue retornado","    assert result[\"statusCode\"] == 200","    assert json.loads(result[\"body\"]) == \"Descarga y almacenamiento completados.\"","","# Prueba 2: Verificar si la función maneja los errores correctamente","@patch(\"urllib.request.urlopen\")","@patch(\"boto3.client\")","def test_lambda_handler_error(mock_boto_client, mock_urlopen):","    # Simula un error en la solicitud HTTP","    mock_urlopen.side_effect = Exception(\"Error de red\")","","    # Simula el cliente S3 de boto3","    mock_s3_client = MagicMock()","    mock_boto_client.return_value = mock_s3_client","","    # Llamar a lambda_handler con un error en la solicitud","    event = {}","    context = {}","    result = lambda_handler(event, context)","","    # Verificar que la función haya manejado el error","    assert result[\"statusCode\"] == 200","    assert \"Error al procesar la página\" in json.loads(result[\"body\"])","","# Prueba 3: Verificar la existencia de la fecha de descarga en el archivo","def test_check_date_in_filename():","    today = datetime.utcnow().strftime(\"%Y-%m-%d\")","    assert today in f\"{today}/page_1.html\"",""]}],[{"start":{"row":10,"column":22},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":37},{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":38}],[{"start":{"row":12,"column":0},"end":{"row":13,"column":0},"action":"insert","lines":["assert mock_urlopen.call_count == 10",""],"id":39}],[{"start":{"row":12,"column":36},"end":{"row":13,"column":0},"action":"remove","lines":["",""],"id":40}],[{"start":{"row":11,"column":0},"end":{"row":12,"column":36},"action":"remove","lines":["","assert mock_urlopen.call_count == 10"],"id":41},{"start":{"row":10,"column":22},"end":{"row":11,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":12,"column":0},"end":{"row":46,"column":0},"action":"remove","lines":["def test_lambda_handler(mock_boto_client, mock_urlopen):","    # Simula la respuesta de la solicitud HTTP","    mock_html = \"<html><body>Test content</body></html>\"","    mock_response = MagicMock()","    mock_response.read.return_value = mock_html.encode(\"utf-8\")","    mock_urlopen.return_value = mock_response","","    # Simula el cliente S3 de boto3","    mock_s3_client = MagicMock()","    mock_boto_client.return_value = mock_s3_client","","    # Establecer los valores esperados","    expected_bucket = \"paginaspruebas\"","    expected_key = f\"{datetime.utcnow().strftime('%Y-%m-%d')}/page_1.html\"","","    # Llamar a lambda_handler (como lo haría AWS Lambda)","    event = {}","    context = {}","    result = lambda_handler(event, context)","","    # Verificar si la solicitud a la URL fue hecha correctamente","    mock_urlopen.assert_called_once()","","    # Verificar que la llamada a S3 se haya realizado correctamente","    mock_s3_client.put_object.assert_called_once_with(","        Bucket=expected_bucket,","        Key=expected_key,","        Body=mock_html,","        ContentType=\"text/html\"","    )","","    # Verificar que el mensaje de éxito fue retornado","    assert result[\"statusCode\"] == 200","    assert json.loads(result[\"body\"]) == \"Descarga y almacenamiento completados.\"",""],"id":42},{"start":{"row":12,"column":0},"end":{"row":32,"column":0},"action":"insert","lines":["@patch(\"urllib.request.urlopen\")","@patch(\"boto3.client\")","def test_lambda_handler(mock_boto_client, mock_urlopen):","    # Simula la respuesta de la solicitud HTTP","    mock_html = \"<html><body>Test content</body></html>\"","    mock_response = MagicMock()","    mock_response.read.return_value = mock_html.encode(\"utf-8\")","    mock_urlopen.return_value = mock_response","","    # Simula el cliente S3 de boto3","    mock_s3_client = MagicMock()","    mock_boto_client.return_value = mock_s3_client","","    # Llamar a lambda_handler","    event = {}","    context = {}","    lambda_handler(event, context)","","    # Verificar cuántas veces se llamó urlopen","    assert mock_urlopen.call_count == 10  # Ajusta esto según el número esperado de descargas",""]}],[{"start":{"row":9,"column":0},"end":{"row":10,"column":22},"action":"remove","lines":["@patch(\"urllib.request.urlopen\")","@patch(\"boto3.client\")"],"id":43},{"start":{"row":8,"column":66},"end":{"row":9,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":32},"action":"remove","lines":["@patch(\"urllib.request.urlopen\")"],"id":44}],[{"start":{"row":11,"column":22},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":45}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":32},"action":"insert","lines":["@patch(\"urllib.request.urlopen\")"],"id":46}],[{"start":{"row":9,"column":0},"end":{"row":10,"column":0},"action":"remove","lines":["",""],"id":47},{"start":{"row":9,"column":0},"end":{"row":10,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":32,"column":0},"end":{"row":32,"column":22},"action":"remove","lines":["@patch(\"boto3.client\")"],"id":48}],[{"start":{"row":31,"column":0},"end":{"row":32,"column":0},"action":"insert","lines":["",""],"id":49}],[{"start":{"row":31,"column":0},"end":{"row":31,"column":22},"action":"insert","lines":["@patch(\"boto3.client\")"],"id":50}],[{"start":{"row":28,"column":4},"end":{"row":28,"column":40},"action":"remove","lines":["assert mock_urlopen.call_count == 10"],"id":51},{"start":{"row":28,"column":4},"end":{"row":28,"column":41},"action":"insert","lines":["assert mock_urlopen.call_count == 10 "]}],[{"start":{"row":48,"column":4},"end":{"row":49,"column":70},"action":"remove","lines":["assert result[\"statusCode\"] == 200","    assert \"Error al procesar la página\" in json.loads(result[\"body\"])"],"id":52},{"start":{"row":48,"column":4},"end":{"row":48,"column":41},"action":"insert","lines":["assert mock_urlopen.call_count == 10 "]}],[{"start":{"row":9,"column":0},"end":{"row":29,"column":0},"action":"remove","lines":["@patch(\"boto3.client\")","@patch(\"urllib.request.urlopen\")","def test_lambda_handler(mock_boto_client, mock_urlopen):","    # Simula la respuesta de la solicitud HTTP","    mock_html = \"<html><body>Test content</body></html>\"","    mock_response = MagicMock()","    mock_response.read.return_value = mock_html.encode(\"utf-8\")","    mock_urlopen.return_value = mock_response","","    # Simula el cliente S3 de boto3","    mock_s3_client = MagicMock()","    mock_boto_client.return_value = mock_s3_client","","    # Llamar a lambda_handler","    event = {}","    context = {}","    lambda_handler(event, context)","","    # Verificar cuántas veces se llamó urlopen","    assert mock_urlopen.call_count == 10   # Ajusta esto según el número esperado de descargas",""],"id":53},{"start":{"row":9,"column":0},"end":{"row":30,"column":0},"action":"insert","lines":["@patch(\"boto3.client\")","@patch(\"urllib.request.urlopen\")","def test_lambda_handler(mock_urlopen, mock_boto_client):  # El orden de los parámetros importa","    # Simula la respuesta de la solicitud HTTP","    mock_html = \"<html><body>Test content</body></html>\"","    mock_response = MagicMock()","    mock_response.read.return_value = mock_html.encode(\"utf-8\")","    mock_urlopen.return_value = mock_response","","    # Simula el cliente S3 de boto3","    mock_s3_client = MagicMock()","    mock_boto_client.return_value = mock_s3_client","","    # Llamar a lambda_handler","    event = {}","    context = {}","    lambda_handler(event, context)","","    # Verificar cuántas veces se llamó urlopen","    print(f\"Cantidad de llamadas a urlopen: {mock_urlopen.call_count}\")  # Depuración","    assert mock_urlopen.call_count == 10, f\"Se esperaban 10 llamadas, pero se hicieron {mock_urlopen.call_count}\"",""]}],[{"start":{"row":33,"column":0},"end":{"row":33,"column":32},"action":"remove","lines":["@patch(\"urllib.request.urlopen\")"],"id":54}],[{"start":{"row":33,"column":0},"end":{"row":34,"column":0},"action":"remove","lines":["",""],"id":55},{"start":{"row":33,"column":0},"end":{"row":34,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":32,"column":0},"end":{"row":33,"column":0},"action":"insert","lines":["",""],"id":56}],[{"start":{"row":32,"column":0},"end":{"row":32,"column":32},"action":"insert","lines":["@patch(\"urllib.request.urlopen\")"],"id":57}],[{"start":{"row":34,"column":0},"end":{"row":49,"column":0},"action":"remove","lines":["def test_lambda_handler_error(mock_boto_client, mock_urlopen):","    # Simula un error en la solicitud HTTP","    mock_urlopen.side_effect = Exception(\"Error de red\")","","    # Simula el cliente S3 de boto3","    mock_s3_client = MagicMock()","    mock_boto_client.return_value = mock_s3_client","","    # Llamar a lambda_handler con un error en la solicitud","    event = {}","    context = {}","    result = lambda_handler(event, context)","","    # Verificar que la función haya manejado el error","    assert mock_urlopen.call_count == 10 ",""],"id":58},{"start":{"row":34,"column":0},"end":{"row":49,"column":101},"action":"insert","lines":["def test_lambda_handler_error(mock_boto_client, mock_urlopen):","    # Simula un error en la solicitud HTTP","    mock_urlopen.side_effect = Exception(\"Error de red\")","","    # Simula el cliente S3 de boto3","    mock_s3_client = MagicMock()","    mock_boto_client.return_value = mock_s3_client  # Asegurar que devuelve un mock","","    # Llamar a lambda_handler con un error en la solicitud","    event = {}","    context = {}","","    try:","        result = lambda_handler(event, context)","    except Exception as e:","        assert str(e) == \"Error de red\"  # Verificar que se está manejando la excepción correctamente"]}],[{"start":{"row":49,"column":101},"end":{"row":50,"column":0},"action":"insert","lines":["",""],"id":59},{"start":{"row":50,"column":0},"end":{"row":50,"column":8},"action":"insert","lines":["        "]},{"start":{"row":50,"column":8},"end":{"row":51,"column":0},"action":"insert","lines":["",""]},{"start":{"row":51,"column":0},"end":{"row":51,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":51,"column":4},"end":{"row":51,"column":8},"action":"remove","lines":["    "],"id":60},{"start":{"row":51,"column":0},"end":{"row":51,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":50,"column":8},"end":{"row":51,"column":0},"action":"remove","lines":["",""],"id":61},{"start":{"row":50,"column":4},"end":{"row":50,"column":8},"action":"remove","lines":["    "]},{"start":{"row":50,"column":0},"end":{"row":50,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":50,"column":0},"end":{"row":51,"column":0},"action":"insert","lines":["",""],"id":62}],[{"start":{"row":0,"column":0},"end":{"row":56,"column":0},"action":"remove","lines":["import json","import pytest","from unittest.mock import patch, MagicMock","from datetime import datetime","","# Importar la función lambda_handler de tu código","from proyecto import lambda_handler  # Ajusta esto al nombre de tu archivo","","# Prueba 1: Verificar la llamada a la URL y subida a S3 (Simulada)","@patch(\"boto3.client\")","@patch(\"urllib.request.urlopen\")","def test_lambda_handler(mock_urlopen, mock_boto_client):  # El orden de los parámetros importa","    # Simula la respuesta de la solicitud HTTP","    mock_html = \"<html><body>Test content</body></html>\"","    mock_response = MagicMock()","    mock_response.read.return_value = mock_html.encode(\"utf-8\")","    mock_urlopen.return_value = mock_response","","    # Simula el cliente S3 de boto3","    mock_s3_client = MagicMock()","    mock_boto_client.return_value = mock_s3_client","","    # Llamar a lambda_handler","    event = {}","    context = {}","    lambda_handler(event, context)","","    # Verificar cuántas veces se llamó urlopen","    print(f\"Cantidad de llamadas a urlopen: {mock_urlopen.call_count}\")  # Depuración","    assert mock_urlopen.call_count == 10, f\"Se esperaban 10 llamadas, pero se hicieron {mock_urlopen.call_count}\"","","# Prueba 2: Verificar si la función maneja los errores correctamente","@patch(\"urllib.request.urlopen\")","@patch(\"boto3.client\")","def test_lambda_handler_error(mock_boto_client, mock_urlopen):","    # Simula un error en la solicitud HTTP","    mock_urlopen.side_effect = Exception(\"Error de red\")","","    # Simula el cliente S3 de boto3","    mock_s3_client = MagicMock()","    mock_boto_client.return_value = mock_s3_client  # Asegurar que devuelve un mock","","    # Llamar a lambda_handler con un error en la solicitud","    event = {}","    context = {}","","    try:","        result = lambda_handler(event, context)","    except Exception as e:","        assert str(e) == \"Error de red\"  # Verificar que se está manejando la excepción correctamente","","","# Prueba 3: Verificar la existencia de la fecha de descarga en el archivo","def test_check_date_in_filename():","    today = datetime.utcnow().strftime(\"%Y-%m-%d\")","    assert today in f\"{today}/page_1.html\"",""],"id":64},{"start":{"row":0,"column":0},"end":{"row":50,"column":42},"action":"insert","lines":["import json","import pytest","from unittest.mock import patch, MagicMock","from datetime import datetime","","# Importar la función lambda_handler de tu código","from proyecto import lambda_handler  # Ajusta esto al nombre de tu archivo","","# Prueba 1: Verificar la llamada a la URL y subida a S3 (Simulada)","@patch(\"boto3.client\")","@patch(\"urllib.request.urlopen\")","def test_lambda_handler(mock_urlopen, mock_boto_client):","    \"\"\"Prueba para verificar que se realizan las llamadas a urlopen y subida a S3.\"\"\"","    mock_html = \"<html><body>Test content</body></html>\"","    mock_response = MagicMock()","    mock_response.read.return_value = mock_html.encode(\"utf-8\")","    mock_urlopen.return_value = mock_response","","    mock_s3_client = MagicMock()","    mock_boto_client.return_value = mock_s3_client","","    event, context = {}, {}","    lambda_handler(event, context)","","    print(f\"Cantidad de llamadas a urlopen: {mock_urlopen.call_count}\")  # Depuración","    assert mock_urlopen.call_count == 10, (","        f\"Se esperaban 10 llamadas, pero se hicieron {mock_urlopen.call_count}\"","    )","","# Prueba 2: Verificar si la función maneja los errores correctamente","@patch(\"urllib.request.urlopen\")","@patch(\"boto3.client\")","def test_lambda_handler_error(mock_boto_client, mock_urlopen):","    \"\"\"Prueba para verificar que la función maneja errores en la solicitud HTTP.\"\"\"","    mock_urlopen.side_effect = Exception(\"Error de red\")","","    mock_s3_client = MagicMock()","    mock_boto_client.return_value = mock_s3_client","","    event, context = {}, {}","    ","    try:","        lambda_handler(event, context)","    except Exception as e:","        assert str(e) == \"Error de red\", \"El error no fue manejado correctamente\"","","# Prueba 3: Verificar la existencia de la fecha de descarga en el archivo","def test_check_date_in_filename():","    \"\"\"Prueba para verificar que el nombre del archivo contiene la fecha actual.\"\"\"","    today = datetime.utcnow().strftime(\"%Y-%m-%d\")","    assert today in f\"{today}/page_1.html\""]}],[{"start":{"row":0,"column":0},"end":{"row":50,"column":42},"action":"remove","lines":["import json","import pytest","from unittest.mock import patch, MagicMock","from datetime import datetime","","# Importar la función lambda_handler de tu código","from proyecto import lambda_handler  # Ajusta esto al nombre de tu archivo","","# Prueba 1: Verificar la llamada a la URL y subida a S3 (Simulada)","@patch(\"boto3.client\")","@patch(\"urllib.request.urlopen\")","def test_lambda_handler(mock_urlopen, mock_boto_client):","    \"\"\"Prueba para verificar que se realizan las llamadas a urlopen y subida a S3.\"\"\"","    mock_html = \"<html><body>Test content</body></html>\"","    mock_response = MagicMock()","    mock_response.read.return_value = mock_html.encode(\"utf-8\")","    mock_urlopen.return_value = mock_response","","    mock_s3_client = MagicMock()","    mock_boto_client.return_value = mock_s3_client","","    event, context = {}, {}","    lambda_handler(event, context)","","    print(f\"Cantidad de llamadas a urlopen: {mock_urlopen.call_count}\")  # Depuración","    assert mock_urlopen.call_count == 10, (","        f\"Se esperaban 10 llamadas, pero se hicieron {mock_urlopen.call_count}\"","    )","","# Prueba 2: Verificar si la función maneja los errores correctamente","@patch(\"urllib.request.urlopen\")","@patch(\"boto3.client\")","def test_lambda_handler_error(mock_boto_client, mock_urlopen):","    \"\"\"Prueba para verificar que la función maneja errores en la solicitud HTTP.\"\"\"","    mock_urlopen.side_effect = Exception(\"Error de red\")","","    mock_s3_client = MagicMock()","    mock_boto_client.return_value = mock_s3_client","","    event, context = {}, {}","    ","    try:","        lambda_handler(event, context)","    except Exception as e:","        assert str(e) == \"Error de red\", \"El error no fue manejado correctamente\"","","# Prueba 3: Verificar la existencia de la fecha de descarga en el archivo","def test_check_date_in_filename():","    \"\"\"Prueba para verificar que el nombre del archivo contiene la fecha actual.\"\"\"","    today = datetime.utcnow().strftime(\"%Y-%m-%d\")","    assert today in f\"{today}/page_1.html\""],"id":65},{"start":{"row":0,"column":0},"end":{"row":52,"column":0},"action":"insert","lines":["import json","import pytest","from unittest.mock import patch, MagicMock","from datetime import datetime","","# Importar la función lambda_handler de tu código","from proyecto import lambda_handler  # Ajusta esto al nombre de tu archivo","","# Prueba 1: Verificar la llamada a la URL y subida a S3 (Simulada)","@patch(\"boto3.client\")","@patch(\"urllib.request.urlopen\")","def test_lambda_handler(mock_urlopen, mock_boto_client):","    \"\"\"Prueba para verificar que se realizan las llamadas a urlopen y subida a S3.\"\"\"","    mock_html = \"<html><body>Test content</body></html>\"","    mock_response = MagicMock()","    mock_response.read.return_value = mock_html.encode(\"utf-8\")","    mock_urlopen.return_value = mock_response","","    mock_s3_client = MagicMock()","    mock_boto_client.return_value = mock_s3_client","","    event, context = {}, {}","    response = lambda_handler(event, context)","    ","    assert response[\"statusCode\"] == 200, \"La función lambda no retornó un código 200.\"","    ","    print(f\"Cantidad de llamadas a urlopen: {mock_urlopen.call_count}\")  # Depuración","    assert mock_urlopen.call_count == 10, (","        f\"Se esperaban 10 llamadas, pero se hicieron {mock_urlopen.call_count}\"","    )","","# Prueba 2: Verificar si la función maneja los errores correctamente","@patch(\"boto3.client\")","@patch(\"urllib.request.urlopen\")","def test_lambda_handler_error(mock_urlopen, mock_boto_client):","    \"\"\"Prueba para verificar que la función maneja errores en la solicitud HTTP.\"\"\"","    mock_urlopen.side_effect = Exception(\"Error de red\")","","    mock_s3_client = MagicMock()","    mock_boto_client.return_value = mock_s3_client","","    event, context = {}, {}","    response = lambda_handler(event, context)","    ","    assert response[\"statusCode\"] == 500, \"No se manejó correctamente el error de red.\"","    assert \"Error de red\" in response[\"body\"], \"El mensaje de error no es el esperado.\"","","# Prueba 3: Verificar la existencia de la fecha de descarga en el archivo","def test_check_date_in_filename():","    \"\"\"Prueba para verificar que el nombre del archivo contiene la fecha actual.\"\"\"","    today = datetime.utcnow().strftime(\"%Y-%m-%d\")","    assert today in f\"{today}/page_1.html\", \"La fecha no está presente en el nombre del archivo.\"",""]}],[{"start":{"row":0,"column":0},"end":{"row":52,"column":0},"action":"remove","lines":["import json","import pytest","from unittest.mock import patch, MagicMock","from datetime import datetime","","# Importar la función lambda_handler de tu código","from proyecto import lambda_handler  # Ajusta esto al nombre de tu archivo","","# Prueba 1: Verificar la llamada a la URL y subida a S3 (Simulada)","@patch(\"boto3.client\")","@patch(\"urllib.request.urlopen\")","def test_lambda_handler(mock_urlopen, mock_boto_client):","    \"\"\"Prueba para verificar que se realizan las llamadas a urlopen y subida a S3.\"\"\"","    mock_html = \"<html><body>Test content</body></html>\"","    mock_response = MagicMock()","    mock_response.read.return_value = mock_html.encode(\"utf-8\")","    mock_urlopen.return_value = mock_response","","    mock_s3_client = MagicMock()","    mock_boto_client.return_value = mock_s3_client","","    event, context = {}, {}","    response = lambda_handler(event, context)","    ","    assert response[\"statusCode\"] == 200, \"La función lambda no retornó un código 200.\"","    ","    print(f\"Cantidad de llamadas a urlopen: {mock_urlopen.call_count}\")  # Depuración","    assert mock_urlopen.call_count == 10, (","        f\"Se esperaban 10 llamadas, pero se hicieron {mock_urlopen.call_count}\"","    )","","# Prueba 2: Verificar si la función maneja los errores correctamente","@patch(\"boto3.client\")","@patch(\"urllib.request.urlopen\")","def test_lambda_handler_error(mock_urlopen, mock_boto_client):","    \"\"\"Prueba para verificar que la función maneja errores en la solicitud HTTP.\"\"\"","    mock_urlopen.side_effect = Exception(\"Error de red\")","","    mock_s3_client = MagicMock()","    mock_boto_client.return_value = mock_s3_client","","    event, context = {}, {}","    response = lambda_handler(event, context)","    ","    assert response[\"statusCode\"] == 500, \"No se manejó correctamente el error de red.\"","    assert \"Error de red\" in response[\"body\"], \"El mensaje de error no es el esperado.\"","","# Prueba 3: Verificar la existencia de la fecha de descarga en el archivo","def test_check_date_in_filename():","    \"\"\"Prueba para verificar que el nombre del archivo contiene la fecha actual.\"\"\"","    today = datetime.utcnow().strftime(\"%Y-%m-%d\")","    assert today in f\"{today}/page_1.html\", \"La fecha no está presente en el nombre del archivo.\"",""],"id":67},{"start":{"row":0,"column":0},"end":{"row":52,"column":0},"action":"insert","lines":["from unittest.mock import patch, MagicMock","from datetime import datetime","","# Importar la función lambda_handler de tu código","from proyecto import lambda_handler  # Ajusta esto al nombre de tu archivo","","","# Prueba 1: Verificar la llamada a la URL y subida a S3 (Simulada)","@patch(\"boto3.client\")","@patch(\"urllib.request.urlopen\")","def test_lambda_handler(mock_urlopen, mock_boto_client):","    \"\"\"Prueba para verificar que se realizan las llamadas a urlopen y subida a S3.\"\"\"","    mock_html = \"<html><body>Test content</body></html>\"","    mock_response = MagicMock()","    mock_response.read.return_value = mock_html.encode(\"utf-8\")","    mock_urlopen.return_value = mock_response","","    mock_s3_client = MagicMock()","    mock_boto_client.return_value = mock_s3_client","","    event, context = {}, {}","    response = lambda_handler(event, context)","","    assert response[\"statusCode\"] == 200, \"La función lambda no retornó un código 200.\"","","    assert mock_urlopen.call_count == 10, (","        f\"Se esperaban 10 llamadas, pero se hicieron {mock_urlopen.call_count}\"","    )","","","# Prueba 2: Verificar si la función maneja los errores correctamente","@patch(\"boto3.client\")","@patch(\"urllib.request.urlopen\")","def test_lambda_handler_error(mock_urlopen, mock_boto_client):","    \"\"\"Prueba para verificar que la función maneja errores en la solicitud HTTP.\"\"\"","    mock_urlopen.side_effect = Exception(\"Error de red\")","","    mock_s3_client = MagicMock()","    mock_boto_client.return_value = mock_s3_client","","    event, context = {}, {}","    response = lambda_handler(event, context)","","    assert response[\"statusCode\"] == 500, \"No se manejó correctamente el error de red.\"","    assert \"Error de red\" in response[\"body\"], \"El mensaje de error no es el esperado.\"","","","# Prueba 3: Verificar la existencia de la fecha de descarga en el archivo","def test_check_date_in_filename():","    \"\"\"Prueba para verificar que el nombre del archivo contiene la fecha actual.\"\"\"","    today = datetime.utcnow().strftime(\"%Y-%m-%d\")","    assert today in f\"{today}/page_1.html\", \"La fecha no está presente en el nombre del archivo.\"",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":52,"column":0},"end":{"row":52,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1741661826590,"hash":"1d5d075ebaf6aaa3351cd6861d5185240e234067"}