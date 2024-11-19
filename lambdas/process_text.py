import json


def lambda_handler(event, context):
    body = event.get("body")

    if not body:
        response = {
            "statusCode": 400,
            "body": {"error": "Se requiere un cuerpo JSON con el texto."},
        }
        return json.dumps(response)

    data = json.loads(body)
    text = data.get("texto")

    if not text:
        response = {
            "statusCode": 400,
            "body": {"error": "El campo 'texto' es obligatorio."},
        }
        return json.dumps(response)

    words = len(text.split())
    characters = len(text)
    text_upper = text.upper()

    response = {
        "statusCode": 200,
        "body": {
            "palabras": words,
            "caracteres": characters,
            "texto_mayusculas": text_upper,
        },
    }
    return json.dumps(response)
