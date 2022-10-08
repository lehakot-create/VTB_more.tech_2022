import feedparser


def check_url(url_feed):
    """
    функция получает линк на рсс ленту, возвращает распаршенную ленту с помощью feedpaeser
    :param url_feed:
    :return:
    """
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
        value = list(eval(el).values())[0]
        all_data.extend(getData(value))
    print(all_data)



# if __name__ == "__main__":
#     main(our_feeds)
