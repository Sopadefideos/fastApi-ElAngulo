import fastapi as api
from ..utils.sql import mycursor, mydb
from pydantic import BaseModel
import json


class UserForm(BaseModel):
    username: str
    email: str
    password: str


router = api.APIRouter(prefix="/users",
                       tags=["User"],)


@router.get('/')
async def allUsers():
    mycursor.execute("SELECT * FROM users")
    myresult = mycursor.fetchall()
    result = []
    for row in myresult:
        result.append(
            {"id": row[0], "username": row[1], "mail": row[2], "password": row[3]})
    return result


@router.get('/{id}')
async def getUserById(id, email: str | None = None):
    mycursor.execute("SELECT * FROM users WHERE ID='"+id+"'")
    myresult = mycursor.fetchall()
    result = []
    for row in myresult:
        result.append(
            {"id": row[0], "username": row[1], "mail": row[2], "password": row[3]})
    return result


@router.post("/")
async def create_item(user: UserForm):
    sql = "INSERT INTO users (username, mail, password) VALUES (%s, %s, %s)"
    val = (user.username, user.email, user.password)
    mycursor.execute(sql, val)
    mydb.commit()
