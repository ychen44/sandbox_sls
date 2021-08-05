import json 
from api.responses import ok_response, invalid_request_response
import logging
import os
import time
import uuid
import boto3

dynamodb = boto3.resource('dynamodb')

def main(event, context):
    path_params = event.get('pathParameters', None)
    if not path_params:
        return invalid_request_response()

    user_id = path_params.get('id', None)

    if not user_id:
        return invalid_request_response()
    return ok_response({
        'user': {
            'id': user_id
            }
        })



def create(event, context):
    data = json.loads(event['body'])
    if 'firstname' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create user")
    
    timestamp = str(time.time())

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': str(uuid.uuid1()),
        'firstname': data['firstname'],
        'lastname': data['lastname'],
        'email': data['email'],
        'password': data['password'],
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }

    # write the todo to the database
    table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return ok_response(response)


if __name__ == '__main__':
    event = {
        'pathParameters': {
        'id':'testId'
        }
    }
    result = main(event, None)
    print(result)