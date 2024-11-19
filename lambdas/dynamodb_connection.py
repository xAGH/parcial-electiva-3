import boto3
from botocore.exceptions import ClientError


def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("Estudiantes")
    student_id = event.get("queryStringParameters", {}).get("id")

    if not student_id:
        return {
            "statusCode": 400,
            "body": {"error": "El parámetro 'id' es obligatorio."},
        }

    try:
        response = table.get_item(Key={"id": student_id})
        item = response.get("Item")

        if not item:
            return {
                "statusCode": 404,
                "body": {"error": "Estudiante no encontrado."},
            }

        return {"statusCode": 200, "body": item}
    except ClientError as e:
        return {"statusCode": 500, "body": {"error": str(e)}}
