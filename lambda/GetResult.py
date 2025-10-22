import json   #for JSON data
import boto3  #for Python to to access DynamoDB

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Results') 

def handler(event, context):
    try:
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

        # If student detail not exist
        if not item:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'Student not found'})
            }
        # Return found item
        return {
            'statusCode': 200,
            'body': json.dumps(item, default=str)
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
