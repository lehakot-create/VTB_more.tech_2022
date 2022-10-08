
# rss_channels_for_buh = {'https://www.glavbukh.ru/': 'https://www.glavbukh.ru/rss/news.xml',
#                         'https://buh.ru/news/': 'https://buh.ru/rss/?chanel=news',
#                         }

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

# rss_chanels_for_lawyers = {
#     : ,
#     : ,
#     : ,
#     : ,
#     :
# }
rss_chanels_for_lawyers = [
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
    "title": 'http://government.ru/' ,
    "rss": 'http://government.ru/all/rss/',
    },
{
    "title": 'https://pravo.ru/rss/',
    "rss": 'https://pravo.ru/rss/',
    },
]
#
# rss_chanels_for_personal = {
#     'http://government.ru/': 'http://government.ru/all/rss/',
#     'https://mintrud.gov.ru/': 'https://mintrud.gov.ru/news/rss/official'
# }
rss_chanels_for_personal ={}
#
# rss_channels_for_accountants = {
#     'https://www.glavbukh.ru/': 'https://www.glavbukh.ru/rss/news.xml',
#     'https://buh.ru/news/': 'https://buh.ru/rss/?chanel=news',
#     'https://www.buhonline.ru/': 'https://www.buhonline.ru/pub/all/rss',
#     'https://www.klerk.ru/': 'https://www.klerk.ru/xml/index.xml',
#     'https://www.audit-it.ru/': 'http://www.audit-it.ru/rss/news_all.xml',
#     'http://www.garant.ru/': 'http://www.garant.ru/rss/',
#     'http://www.consultant.ru': 'http://www.consultant.ru/rss/db.xml'
# }
rss_channels_for_accountants ={}

init_roles = [{
    'role': 'buh',
    "rss": rss_channels_for_buh
},
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
        # output_lst = []
        role = init_role.get('role')
        # print("RSS", init_role.get("rss"))
        result = [eval(el) for el in conn.get_source(role)]
        # print("result", result)
        for el in init_role.get("rss"):
            # print("el", {el.get('title'): el.get('rss')})
            if {el.get('title'): el.get('rss')} not in result:
                # print(el)
                conn.add_source(role, {
                    "name": el.get('title'),
                    "url": el.get('rss')})
                # output_lst.append({
                #     "name": el.get('title'),
                #     "url": el.get('rss')}
                # )
                # pass
        # print(role, output_lst)
        # if output_lst:
        #     conn.add_source(role, output_lst)
    # conn.add_source




def initialize(conn):
    # проверка ролей
    roles_from_db = conn.get_all_roles()
    for role in init_roles:
        if role.get("role") not in roles_from_db:
            conn.write_role(role.get("role"))

    # проверка источников для ролей
    check_source(conn)
