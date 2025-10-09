from fastapi import APIRouter
from ..schemas.mails import Mail
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/mails",
   tags=["mails"],
)
@router.get("/")
def read_mails(db: Session = get_db()):
    mails = db.query(Mail).all()
    return mails

@router.post("/")
def create_mail(mail: Mail, db: Session = get_db()):
    db.add(mail)
    db.commit()
    db.refresh(mail)
    return mail
