from app import check_url


def list_description(url_feed):
    data_list = []
    data_dict = {}
    lenta = check_url(url_feed)
    i = 0
    for item_of_news in lenta['items']:
        data_list.append(item_of_news['title'].replace(",", "").split())
        for item in data_list[i]:
            if len(item) < 3:
                data_list[i].remove(item)
        data_dict[i] = frozenset(data_list[i])
        i += 1
    print(data_dict)
    return data_dict


d = list_description('https://www.glavbukh.ru/rss/news.xml')
c = list_description('https://buh.ru/rss/?chanel=news')

for i in d.values():
    for j in c.values():
        set_inter = i.intersection(j)
        if len(set_inter) > 2: # по скольким словам сравнивать новости
            print(set_inter)
