import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.social_network

users_collection = database.get_collection("users")
posts_collection = database.get_collection("posts")

async def connect_db():
    """Verifies the connection to the MongoDB database.

    Attempts to retrieve the server information to check if the 
    connection to MongoDB is successful. If it fails, prints the error.

    Raises:
        Exception: If unable to connect to MongoDB.
    """
    try:
        await client.server_info()  # Trigger exception if connection fails
        print("Successfully connected to MongoDB")
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")

async def close_db():
    """
    Closes the connection to the MongoDB database.

    Closes the open connection to the MongoDB client asynchronously.
    """
    await client.close()
