import json
import boto3
from datetime import datetime
import uuid


def lambda_handler(event, context):
    ddb = boto3.resource('dynamodb')
    table = ddb.Table('UserTable')
    
    body = json.loads(event["body"])
    
    item = {
        "photoID": body["photoID"],
        "email": body["email"],
        "created_at": str(datetime.now()),
        "dirphoto": body["dirphoto"],
    }

    table.put_item(Item=item)
    
    return {
        "statusCode": 200,
        "body": json.dumps(item)
    }