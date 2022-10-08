import csv

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

    # header = ['title', 'description', 'link', 'published']
    # with open('output.csv', 'w',encoding='utf-8-sig') as csvfile:
    #     writer = csv.writer(csvfile, delimiter=';')
    #     writer.writerow(i for i in header)
    #
    #     for el in all_data:
    #         writer.writerow((
    #             el.get('title'),
    #             el.get('description'),
    #             el.get('link'),
    #             el.get('published')
    #             ))

    # with open('tmp.json', 'w') as f:
    #     js = {"obj": all_data}
    #     to_json = json.dumps(js, ensure_ascii=False)
    #     f.write(to_json)
    # print(json.dumps(all_data, ensure_ascii=False))


# if __name__ == "__main__":
#     main(our_feeds)
