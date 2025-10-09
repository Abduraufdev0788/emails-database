from pydantic import BaseModel

class MailBase(BaseModel):
    email: str

class MailCreate(MailBase):
    pass

class Mail(MailBase):
    id: int

    class Config:
        orm_mode = True