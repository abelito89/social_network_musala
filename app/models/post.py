from pydantic import BaseModel, Field
from typing import List


class Post(BaseModel):
    """_Model representing a social media post.

    Args:
        BaseModel (type): Base model class for data validation and serialization.

    Attributes:
        text (str): Publication content.
        public_visibility (bool): Indicates whether the post is public or private.
    """
    text:str = Field(..., description="Publication Content")
    public_visbility:bool = Field(..., description="Indicate whether the post is public o private")
    likes:List[str] = Field()


class PostId(Post):
    """Extended model representing a social media post with an additional identifier.

    Args:
        Post (class): Base class representing a social media post.

    Attributes:
        id (str): Identifier inherited from MongoDB.

    Inherits:
        Post: Base model containing attributes for a social media post.
    """
    id:str = Field(..., description="id heredated from MongoDB")