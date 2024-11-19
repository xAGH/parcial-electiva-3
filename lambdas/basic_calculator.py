import json


def lambda_handler(event, context):
    params = event.get("queryStringParameters", {})
    a = params.get("a")
    b = params.get("b")
    operator = params.get("operador")

    try:
        a = float(a)
        b = float(b)
    except (ValueError, TypeError):
        response = {
            "statusCode": 400,
            "body": {"error": "Los parámetros 'a' y 'b' deben ser números válidos."},
        }
        return json.dumps(response)

    valid_operators = ["+", "-", "*", "/", "**"]

    if operator not in valid_operators:
        response = {
            "statusCode": 400,
            "body": {"error": f"El operador debe ser {valid_operators}"},
        }
        return json.dumps(response)

    if operator == "/" and b == 0:
        response = {
            "statusCode": 400,
            "body": {"error": "División por cero no permitida."},
        }
        return json.dumps(response)

    result = eval(f"{a} {operator} {b}")
    response = {"statusCode": 200, "body": {"resultado": result}}
    return json.dumps(response)
