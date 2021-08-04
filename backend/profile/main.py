import json 
from api.responses import ok_response


def main(event, context):
    return ok_response(body = {'message':'hello'})

if __name__ == '__main__':
    main(None, None)

