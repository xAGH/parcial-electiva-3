import json

import boto3
from botocore.exceptions import ClientError


def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("Estudiantes")
    student_id = event.get("queryStringParameters", {}).get("id")

    if not student_id:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "El parámetro 'id' es obligatorio."}),
        }

    if not student_id.isdigit():
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "El parámetro 'id' debe de ser un número."}),
        }

    try:
        response = table.get_item(Key={"id": int(student_id)})
        item = response.get("Item")

        if not item:
            return {
                "statusCode": 404,
                "body": json.dumps({"error": "Estudiante no encontrado."}),
            }

        return {"statusCode": 200, "body": json.dumps(item)}
    except ClientError as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
