import json


def lambda_handler(event, context):
    name = event.get("queryStringParameters", {}).get("nombre")

    if not name:
        response = {
            "statusCode": 400,
            "body": {"message": "Falta el parámetro 'nombre'."},
        }
        return json.dumps(response)

    response = {"statusCode": 200, "body": {"message": f"Hola, {name}!"}}
    return json.dumps(response)
