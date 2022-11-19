from sqlmodel import Session

from . import models

def create_user(
    db: Session,
    user: models.UserSchema
):
    hashed_password = user.password + "HASHED"
    db_user = models.User(
        email = user.email,
        username = user.username,
        role = user.role,
        hashed_password = hashed_password
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(
    db: Session()
):
    return db.query(models.User).all()