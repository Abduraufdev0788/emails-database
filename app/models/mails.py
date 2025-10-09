from sqlalchemy import Column, email, text
from ..database import Base

class Mail(Base):
    __tablename__ = "mails"
    id = Column("id", primary_key=True, index=True)
    email = Column("email", email)
    text = Column(text)

