from db.database import users_collection
from models.user import User

async def get_user_by_email(email: str):
    """Fetch a user by email."""
    return await users_collection.find_one({"email": email})

async def create_user(new_user: User):
    """Insert a new user into the database."""
    user_dict = new_user.model_dump()
    result = await users_collection.insert_one(user_dict)
    inserted_id = result.inserted_id
    created_user = await users_collection.find_one({"_id": inserted_id})
    if created_user:
        created_user["_id"] = str(created_user["_id"])  # Convert ObjectId to string for JSON serialization
    return created_user