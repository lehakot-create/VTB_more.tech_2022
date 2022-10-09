from fastapi import FastAPI, BackgroundTasks

from db import RedisConnector
from schemas import Role, ListSource
from utils.app import main, collect_role
from utils.init_db import initialize
from utils.trends import news_trends

app = FastAPI()
conn = RedisConnector()


@app.get("/")
def index(background_tasks: BackgroundTasks):
    background_tasks.add_task(initialize, conn=conn)
    background_tasks.add_task(collect_role, conn=conn)
    background_tasks.add_task(news_trends, conn=conn)
    return "WELCOME TO THE FUTURE"


@app.get("/trends/")
def get_trends():
    result = conn.get_trends()
    return result


@app.post("/role/")
def write_new_role(role: Role):
    """
    Создает новую роль
    :param role: название роли
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
def get_source(role: str):
    """
    Возвращает все источники для роли
    :param role:
    :return:
    """
    result = conn.get_source(role)
    return result


@app.get('/news/')
def parse_news(role: str, background_tasks: BackgroundTasks):
    """
    Парсит новости для роли
    :param role:
    :return:
    """
    # background_tasks.add_task(main, role, conn=conn)
    result = conn.get_news(role)
    return result
