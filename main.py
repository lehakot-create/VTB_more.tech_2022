from fastapi import FastAPI, BackgroundTasks

from db import RedisConnector
from schemas import Role, ListSource
from utils.app import main
from utils.init_db import initialize

app = FastAPI()
conn = RedisConnector()


@app.get("/")
def index(background_tasks: BackgroundTasks):
    # создать роль
    background_tasks.add_task(initialize, conn=conn)
    # заполнить ее источниками
    return "WELCOME TO THE FUTURE"


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


@app.get('/news/')
def parse_news(role: Role, background_tasks: BackgroundTasks):
    """
    Парсит новости для роли
    :param rule:
    :return:
    """
    background_tasks.add_task(main, role.role, conn=conn)
    return {"status": "ok"}
