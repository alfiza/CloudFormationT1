import json   #for JSON data
import boto3  #for Python to to access DynamoDB

dynamodb = boto3.resource('dynamodb')  
table = dynamodb.Table('Results')  

def handler(event, context):
    
    data = json.loads(event.get('body', '{}'))  
    name = data.get('name')   
    result = data.get('result')               

    # Validating the input data
    if not name or not result:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Student name or result is not valid.'})
        }

    # Storing the data to DB
    table.put_item(Item={
        'name': name,
        'result': result
    })

    # Return success message
    return {
        'statusCode': 200,
        'body': json.dumps({'message': f'Result stored for {name}'})
        
    }
