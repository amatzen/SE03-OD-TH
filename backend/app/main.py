from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from fastapi import FastAPI, Form
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response

from pydantic import BaseModel

# DB
DATABASE_URL = 'mysql://root:password@database/database'

engine = create_engine(DATABASE_URL)
Base = declarative_base()

app = FastAPI()

class Person(Base):
    __tablename__ = 'people'
    PersonID = Column(Integer, primary_key=True, autoincrement=True)
    Firstname = Column(String(255))
    Lastname = Column(String(255))


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

@app.get('/persons')
def persons():
    return JSONResponse(jsonable_encoder(session.query(Person).all()))


@app.post('/person')
def new_person(firstname: str = Form(...), lastname: str = Form(...)):
    person = Person(Firstname = firstname, Lastname = lastname)
    session.add(person)
    session.commit()
    return Response(status_code=200)
