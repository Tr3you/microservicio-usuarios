import logging
import json
from database_connection import update_password

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
        old_password = req_body['old_password']
        new_password = req_body['new_password']
        id_restaurante = req_body['id_restaurante']
        status_code = update_password(old_password=old_password, new_password=new_password, id_restaurante=id_restaurante)
        if(status_code == 200):
            response = {"r": "Contraseña cambiada con exito", "status_code": 200}
            response = json.dumps(response)
            return func.HttpResponse(response, status_code=200)
        else:
            return func.HttpResponse('ERROR FATAL', status_code=500)
    except Exception as e:
        return func.HttpResponse(f'ERROR:{e}', status_code=500)