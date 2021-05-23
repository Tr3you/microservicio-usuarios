import logging
import json
from database_connection import get_user

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
        id_restaurante = req_body['id_restaurante']
        password = req_body['password']
        status_code = get_user(id_restaurante=id_restaurante, password=password)
        if(status_code == 200):
            response = {"r": "Usuario existe en la base de datos", "status_code": 200}
            response = json.dumps(response)
            return func.HttpResponse(response, status_code=200)
        else:
            return func.HttpResponse('ERROR FATAL', status_code=500)
    except Exception as e:
        return func.HttpResponse(f'ERROR:{e}', status_code=500)