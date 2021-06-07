import json

# import requests


def lambda_handler(event, context):
    ddb = boto3.resource('dynamodb')
    table = ddb.Table('LogTable')

    res = table.scan()
    items = res["Items"]

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(items)
    }