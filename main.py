from fastapi import FastAPI, Request
from pydantic import BaseModel

from db import RedisConnector

app = FastAPI()
conn = RedisConnector()


class Role(BaseModel):
    role: str


@app.post("/role/")
def write_new_role(role: Role):
    """
    Создает новую роль
    :param role:
    :param request: название роли
    :return:
    """
    role = role.role
    if role:
        conn.write_role(role)
        return {"status": "ok"}
    else:
        return {"error": "Укажите роль в параметрах"}


@app.get("/role/")
def get_all_roles():
    """
    Возвращает все роли
    :return:
    """
    result = conn.get_all_roles()
    return result