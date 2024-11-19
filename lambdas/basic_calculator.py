def lambda_handler(event, context):
    params = event.get("queryStringParameters", {})
    a = params.get("a")
    b = params.get("b")
    operator = params.get("operador")

    try:
        a = float(a)
        b = float(b)
    except (ValueError, TypeError):
        return {
            "statusCode": 400,
            "body": {"error": "Los parámetros 'a' y 'b' deben ser números válidos."},
        }

    valid_operators = ["+", "-", "*", "/", "**"]

    if operator not in valid_operators:
        return {
            "statusCode": 400,
            "body": {"error": f"El operador debe ser {valid_operators}"},
        }

    if operator == "/" and b == 0:
        return {
            "statusCode": 400,
            "body": {"error": "División por cero no permitida."},
        }

    result = eval(f"{a} {operator} {b}")
    return {"statusCode": 200, "body": {"resultado": result}}
