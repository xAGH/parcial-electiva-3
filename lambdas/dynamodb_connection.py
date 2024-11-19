import json

import boto3
from botocore.exceptions import ClientError


def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("Estudiantes")
    student_id = event.get("queryStringParameters", {}).get("id")

    if not student_id:
        response = {
            "statusCode": 400,
            "body": {"error": "El parámetro 'id' es obligatorio."},
        }
        return json.dumps(response)

    try:
        response = table.get_item(Key={"id": student_id})
        item = response.get("Item")

        if not item:
            response = {
                "statusCode": 404,
                "body": {"error": "Estudiante no encontrado."},
            }
            return json.dumps(response)

        response = {"statusCode": 200, "body": item}
        return json.dumps(response)
    except ClientError as e:
        response = {"statusCode": 500, "body": {"error": str(e)}}
        return json.dumps(response)
