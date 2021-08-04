import json 
from api.responses import ok_response, invalid_request_response


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

if __name__ == '__main__':
    event = {
        'pathParameters': {
        'id':'testId'
        }
    }
    result = main(event, None)
    print(result)

