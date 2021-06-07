import json
import boto3


def lambda_handler(event, context):
    ddb = boto3.resource('dynamodb')
    table = ddb.Table('students')
    
    students = table.scan()['Items']

    return {
        "statusCode": 200,
        "body": json_response(students)
        ),
    }