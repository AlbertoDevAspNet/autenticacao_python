from pydantic import BaseModel

# Esquema de entrada
class UserCreate(BaseModel):
    username: str
    password: str
    role: str = "user"

# Esquema de saida (nunca devolve a senha)
class UserOut(BaseModel):
    id: int
    username: str
    role: str

# "Banco" em memoria
fake_users_db: dict = {}
next_id = 1

def add_user(username: str, hashed_password: str, role: str = "user") -> dict:
    global next_id
    user = {"id": next_id, "username": username,
            "hashed_password": hashed_password, "role": role}
    fake_users_db[next_id] = user
    next_id += 1
    return user
