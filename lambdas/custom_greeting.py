import json


def lambda_handler(event, context):
    name = event.get("queryStringParameters", {}).get("nombre")

    if not name:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Falta el parámetro 'nombre'."}),
        }

    return {"statusCode": 200, "body": json.dumps({"message": f"Hola, {name}!"})}
