import json   #for JSON data
import boto3  #for Python to to access DynamoDB

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Result') 

def lambda_handler(event, context):
    
    params = event.get('queryStringParameters') or {} 
    name = params.get('name')

    # Validatinng the input data
    if not name:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Name is missing.'})
        }

    # get data from result table
    response = table.get_item(Key={'name': name})
    item = response.get('Item')

    # If student detail not exsit
    if not item:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Student not found'})
        }

    # Return found item
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }
