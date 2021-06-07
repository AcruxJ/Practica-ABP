import json
import boto3
from datetime import datetime
import uuid


def lambda_handler(event, context):
    ddb = boto3.resource('dynamodb')
    table = ddb.Table('UserTable')
    
    body = json.loads(event["body"])
    
    item = {
        "logID": str(uuid.uuid4()),
        "photoID": body["photoID"],
        "email": body["email"],
        "date": str(datetime.now()),
    }

    table.put_item(Item=item)
    
    return {
        "statusCode": 200,
        "body": json.dumps(item)
    }