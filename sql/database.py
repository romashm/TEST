from sqlmodel import Session, SQLModel, create_engine
from pathlib import Path
import os

engine = create_engine(
    "sqlite:///base/User.db", 
    connect_args={"check_same_thread": False}
)

def get_db():
    with Session(engine) as session:
        yield session
        
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    
# Shutdown a databese
def shutdown():
    os.remove(os.path.join(Path.cwd().resolve(), [file for file in os.listdir() if file.endswith(".db")][0]))