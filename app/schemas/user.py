from models.user import UserId

def userid_to_dict(userid: UserId) -> dict:
    """
    Convierte un usuario de MongoDB a un diccionario Python.

    Parámetros:
    - `userid`: El usuario en formato MongoDB.

    Retorna:
    - `dict`: Un diccionario con los datos del usuario.
    """
    return {"id":str(userid["_id"]),  
            "fullName":userid["fullName"], 
            "email":userid["email"], 
            "role":userid["role"],
            "password":userid["password"]
            }