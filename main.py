from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from models import User, Gender, Role

app = FastAPI()

#banco provisório
db: List[User] = [
    User(
        id=uuid4(), #ajustar, ID deve ser salvo e fixo e não gerado toda vez que atualiza
        first_name="Tainara", 
        middle_name=None,
        last_name="Melara", 
        gender=Gender.female, 
        roles=[Role.student]
    ),
    User(
        id=uuid4(), 
        first_name="Neto", 
        middle_name=None,
        last_name="Poluceno", 
        gender=Gender.male, 
        roles=[Role.admin, Role.user]
    ),
    User(
        id=uuid4(), 
        first_name="Marcelo", 
        middle_name=None,
        last_name="Martins", 
        gender=Gender.male, 
        roles=[Role.user]
    )
]

@app.get("/")
async def root():
    return {"Edworld Predict Plataform"}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user:User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            #talvez inserir uma validação para o tamanho do ID passado, pois, caso não seja encontrado, está retornando 422
            return 
    raise HTTPException(
        status_code = 404,
        detail = f"User id: {user_id} does not exists"
    )

#criar endpoints para patch e put