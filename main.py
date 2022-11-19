from sqlmodel import Session
from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import sql.database as database
import sql.models as models
import sql.crud as crud

from datetime import datetime

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
def startup_event():
    database.create_db_and_tables()
    
@app.on_event("shutdown")
def startup_event():
    database.shutdown()

# Create an user account 👤
@app.post("/registration")
def registrationUser(
    user: models.UserSchema,
    db: Session = Depends(database.get_db)
):
    return crud.create_user(db=db, user=user)

# 📂 Get all user information, admin side
@app.get("/users")
def get_all_users(
    db: Session = Depends(database.get_db)
):
    return crud.get_users(db=db)