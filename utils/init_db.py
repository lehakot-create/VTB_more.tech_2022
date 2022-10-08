

rss_channels_for_buh = {'https://www.glavbukh.ru/': 'https://www.glavbukh.ru/rss/news.xml',
                        'https://buh.ru/news/': 'https://buh.ru/rss/?chanel=news',
                        }

rss_chanels_for_lawyers = {
    'http://www.consultant.ru/fd': 'http://www.consultant.ru/rss/fd.xml',
    'http://www.consultant.ru/': 'http://www.consultant.ru/rss/nw.xml',
    'http://www.garant.ru/': 'http://www.garant.ru/rss/',
    'http://government.ru/': 'http://government.ru/all/rss/',
    'https://pravo.ru/rss/': 'https://pravo.ru/rss/'
}

rss_chanels_for_personal = {
    'http://government.ru/': 'http://government.ru/all/rss/',
    'https://mintrud.gov.ru/': 'https://mintrud.gov.ru/news/rss/official'
}

rss_channels_for_accountants = {
    'https://www.glavbukh.ru/': 'https://www.glavbukh.ru/rss/news.xml',
    'https://buh.ru/news/': 'https://buh.ru/rss/?chanel=news',
    'https://www.buhonline.ru/': 'https://www.buhonline.ru/pub/all/rss',
    'https://www.klerk.ru/': 'https://www.klerk.ru/xml/index.xml',
    'https://www.audit-it.ru/': 'http://www.audit-it.ru/rss/news_all.xml',
    'http://www.garant.ru/': 'http://www.garant.ru/rss/',
    'http://www.consultant.ru': 'http://www.consultant.ru/rss/db.xml'
}

# init_roles = [{'buh': rss_channels_for_buh},
#               {'lawyers': rss_chanels_for_lawyers},
#               {'personal': rss_chanels_for_personal},
#               {'accountants': rss_channels_for_accountants}]

init_roles = [{
    'role': 'buh',
    "rss": rss_channels_for_buh},
    {
        'role':  'lawyers',
        "rss": rss_chanels_for_lawyers,
    },
    {
        'role': 'personal',
        "rss": rss_chanels_for_personal,
    },
    {
        'role': 'accountants',
        "rss": rss_channels_for_accountants,
    }]


def check_source(conn):
    for init_role in init_roles:
        print(init_role.get("rss"))


def initialize(conn):
    # проверка ролей
    # roles_from_db = conn.get_all_roles()
    # for role in init_roles:
    #     if role.get("role") not in roles_from_db:
    #         conn.write_role(role.get("role"))

    # проверка источников для ролей
    check_source(conn)




