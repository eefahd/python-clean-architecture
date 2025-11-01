from pydantic import BaseModel, EmailStr


class Contact(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
