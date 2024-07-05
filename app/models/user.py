from pydantic import BaseModel, Field, EmailStr, field_validator
import re


class User(BaseModel):
    """Model representing a user.

    Args:
        BaseModel (type): Base model class for data validation and serialization.

    Attributes:
        fullName (str): Full name of the user.
        email (EmailStr): Email address of the user.
        password (str): Password of the user, with specific validation criteria.

    Raises:
        ValueError: If the password does not meet the specified criteria.

    Notes:
        The password must be at least 8 characters long and include at least one uppercase letter,
        one lowercase letter, one number, and one special character from '!@#$%^&*(),.?":{}|<>'.
    """
    fullName:str = Field(..., description="Full name of the user")
    email:EmailStr = Field(..., description="email of the user")
    password:str = Field(min_length=8, description="password of the user")


    @field_validator('password')
    def validate_password(cls, v):
        """Validate the password against specified criteria.

        Args:
            v (str): Password to validate.

        Returns:
            str: Validated password.

        Raises:
            ValueError: If the password does not meet the specified criteria.
        """
        if len(v) < 8:
            raise ValueError('Password must have 8 characters at least')
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r'[a-z]', v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search(r'[0-9]', v):
            raise ValueError('Password must contain at least one number')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', v):
            raise ValueError('Password must contain at least one special character')
        return v


class UserId(User):
    """Extended model representing a user with an additional identifier.

    Args:
        User (class): Base class representing a user.

    Attributes:
        id (str): Identifier inherited from MongoDB.
        role (str): Role of the user, defaults to 'user'.

    Inherits:
        User: Base model containing attributes for a user.
    """
    id:str = Field(..., description="id heredated from MongoDB")
    role:str = Field(default="user", description="By default all users have the user role" )