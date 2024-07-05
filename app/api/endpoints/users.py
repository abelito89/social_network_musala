from fastapi import APIRouter, HTTPException
from models.user import User, UserId
from crud import users
from crud.users import get_user_by_email 
import bcrypt
from api.my_email import send_email


users_router = APIRouter()

@users_router.post("/create_user", response_model=UserId, status_code=201, summary="Create a new user")
async def create_user(new_user: User) -> UserId:
    """
    Create a new user and store it in the database.

    This endpoint allows the creation of a new user, including the following steps:
    - Check if the email already exists in the database.
    - Hash the user's password.
    - Insert the new user data into the database.
    - Send a confirmation email to the user.

    Args:
        new_user (User): The new user data.

    Returns:
        UserId: The created user's data including the MongoDB ID and the role field, 'user' by default.

    Raises:
        HTTPException: If the email is already in use.
    """
    existing_user = await get_user_by_email(new_user.email)
    if existing_user:
        raise HTTPException(status_code=409, detail="El correo electrónico ya está en uso")
    hashed_password = bcrypt.hashpw(new_user.password.encode('utf-8'), bcrypt.gensalt())
    new_user.password = hashed_password.decode('utf-8')
    created_user = await users.create_user(new_user)
    # Transform _id to id
    created_user["id"] = str(created_user.pop("_id"))
    to_email = created_user['email']
    subject = 'Correo de confirmación de creación de usuario nuevo'
    body = f'Se ha creado el usuario {created_user["fullName"]} satisfactoriamente'
    send_email(to_email, subject, body)
    return UserId(**created_user)



