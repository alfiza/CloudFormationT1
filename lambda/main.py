import json
def lambda_fun(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello World Lambda",
            "input": event
        })
    }
    
