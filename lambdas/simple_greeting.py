import json


def lambda_handler(event, context):
    response = {"statusCode": 200, "body": {"message": "Hola, bienvenido al sistema"}}
    return json.dumps(response)
