import json


def lambda_handler(event, context):
    body = event.get("body")

    if not body:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Se requiere un cuerpo JSON con el texto."}),
        }

    data = json.loads(body)
    text = data.get("texto")

    if not text:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "El campo 'texto' es obligatorio."}),
        }

    words = len(text.split())
    characters = len(text)
    text_upper = text.upper()
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "palabras": words,
                "caracteres": characters,
                "texto_mayusculas": text_upper,
            }
        ),
    }
