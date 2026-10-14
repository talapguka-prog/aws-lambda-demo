

def lambda_handler(event, context):
    name = event.get("name", "Student")

    return {
        "statusCode": 200,
        "body": f"Сәлем, {name}! AWS Lambda жұмыс істеп тұр."
    }


if __name__ == "__main__":
    result = lambda_handler({"name": "Student"}, None)
    print(result)