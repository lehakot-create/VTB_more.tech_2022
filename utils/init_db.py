rss_channels_for_buh = [
    {
        "title": 'https://www.glavbukh.ru/',
        "rss": 'https://www.glavbukh.ru/rss/news.xml'
    },
    {
        "title": 'https://buh.ru/news/',
        "rss": 'https://buh.ru/rss/?chanel=news',
    },
]

rss_channels_for_leaders = [
    {
        "title": 'http://www.consultant.ru/fd',
        "rss": 'http://www.consultant.ru/rss/fd.xml',
    },
    {
        "title": 'http://www.consultant.ru/',
        "rss": 'http://www.consultant.ru/rss/nw.xml',
    },
    {
        "title": 'http://www.garant.ru/',
        "rss": 'http://www.garant.ru/rss/',
    },
    {
        "title": 'http://government.ru/',
        "rss": 'http://government.ru/all/rss/',
    },
    {
        "title": 'https://pravo.ru/rss/',
        "rss": 'https://pravo.ru/rss/',
    },
]

rss_channels_for_personal = [
    {
        "title": 'http://government.ru/',
        "rss": 'http://government.ru/all/rss/',
    },
    {
        "title": 'https://mintrud.gov.ru/',
        "rss": 'https://mintrud.gov.ru/news/rss/official',
    },
]

rss_channels_for_accountants = [
    {
        "title": 'https://www.glavbukh.ru/',
        "rss": 'https://www.glavbukh.ru/rss/news.xml',
    },
    {
        "title": 'https://buh.ru/news/',
        "rss": 'https://buh.ru/rss/?chanel=news',
    },
    {
        "title": 'https://www.buhonline.ru/',
        "rss": 'https://www.buhonline.ru/pub/all/rss',
    },
    {
        "title": 'https://www.klerk.ru/',
        "rss": 'https://www.klerk.ru/xml/index.xml',
    },
    {
        "title": 'https://www.audit-it.ru/',
        "rss": 'http://www.audit-it.ru/rss/news_all.xml',
    },
    {
        "title": 'http://www.garant.ru/',
        "rss": 'http://www.garant.ru/rss/',
    },
    {
        "title": 'http://www.consultant.ru',
        "rss": 'http://www.consultant.ru/rss/db.xml',
    },
]

init_roles = [{
    'role': 'buh',
    "rss": rss_channels_for_buh
},
    {
        'role': 'lawyers',
        "rss": rss_channels_for_leaders,
    },
    {
        'role': 'personal',
        "rss": rss_channels_for_personal,
    },
    {
        'role': 'accountants',
        "rss": rss_channels_for_accountants,
    }]


def check_source(conn):
    for init_role in init_roles:
        role = init_role.get('role')
        result = [eval(el) for el in conn.get_source(role)]
        for el in init_role.get("rss"):
            if {el.get('title'): el.get('rss')} not in result:
                conn.add_source(role, [{
                    "name": el.get('title'),
                    "url": el.get('rss')}])


def initialize(conn):
    # проверка ролей
    roles_from_db = conn.get_all_roles()
    for role in init_roles:
        if role.get("role") not in roles_from_db:
            conn.write_role(role.get("role"))

    # проверка источников для ролей
    check_source(conn)
