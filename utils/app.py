import feedparser


# our_feeds = {'https://www.glavbukh.ru/': 'https://www.glavbukh.ru/rss/news.xml',
#              'https://buh.ru/news/': 'https://buh.ru/rss/?chanel=news',
#              }  # пример словаря RSS-лент


def check_url(url_feed):  # функция получает линк на рсс ленту, возвращает
    # распаршенную ленту с помощью feedpaeser
    return feedparser.parse(url_feed)


def getData(url_feed: str):
    data = []
    lenta = check_url(url_feed)
    for item_of_news in lenta['items']:
        data.append({
            "title": item_of_news['title'],
            "description": item_of_news['description'],
            "link": item_of_news['link'],
            "published": item_of_news['published']
        })
    return data


def get_source(role: str, conn):
    return conn.get_source(role)


def main(role: str, conn):
    all_data = []
    result = get_source(role, conn)

    for el in result:
        print(str(eval(el).values()))
        print(type(eval(el)))
        all_data.extend(getData(eval(el).values()))
    # source = {'https://www.glavbukh.ru/': 'https://www.glavbukh.ru/rss/news.xml',
    #              'https://buh.ru/news/': 'https://buh.ru/rss/?chanel=news',
    #              }  # пример словаря RSS-лент

    # for value in source.values():
    #     all_data.extend(getData(value))

    # print(all_data)


# if __name__ == "__main__":
#     main(our_feeds)
