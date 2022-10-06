from fastapi import FastAPI, Request

from db import RedisConnector
from schemas import Role, ListSource

app = FastAPI()
conn = RedisConnector()


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


@app.post("/source/")
def post_new_source(source: ListSource):
    """
    Добавляет источники RSS-лент к роли
    :param source:
    :return:
    """
    conn.add_source(source.role.role, source.lstSource)
    return {"status": "ok"}


@app.get("/source/")
def get_source(role: Role):
    """
    Возвращает все источники для роли
    :param role:
    :return:
    """
    result = conn.get_source(role.role)
    return result
