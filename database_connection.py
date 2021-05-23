import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def add_new_user(id_restaurante, password):
    try: 
        db.collection('usuario').document(str(id_restaurante)).set({
            'id_restaurante': id_restaurante, 
            'password':password
        })
        return 200
    except:
        return 500
        

def get_user(id_restaurante, password):
    try: 
        result = db.collection('usuario').document(str(id_restaurante)).get()
        if result.exists:
            result = result.to_dict()
            if(result['password']==password):
                return 200
            else:
                return 500
        else:
            return 500
    except:
        return 500


def update_password(old_password, new_password, id_restaurante):
    try:
        result = db.collection('usuario').document(str(id_restaurante)).get()
        if result.exists:
            result = result.to_dict()
            if(result['password'] == old_password):
                try:
                    db.collection('usuario').document(str(id_restaurante)).update({'password': new_password})
                    return 200
                except:
                    return 500
        else:
            return 500
    except:
        return 500
