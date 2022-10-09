import pandas as pd
import numpy as np
import re
from tqdm import tqdm

import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime, timedelta


def news_trends(conn):
    news = pd.read_csv('utils/news.csv')


    # Преобразуем дату

    month_dict = {
        'января': 1,
        'февраля': 2,
        'марта': 3,
        'апреля': 4,
        'мая': 5,
        'июня': 6,
        'июля': 7,
        'августа': 8,
        'сентября': 9,
        'октября': 10,
        'ноября': 11,
        'декабря': 12
    }

    def date_month(d):
        try: d = datetime.strptime(d, '%Y-%m-%d')
        except:
            d = d.split(' ')
            d = str(d[2])+'-'+str(month_dict[d[1]])+'-'+str(d[0])
            d = datetime.strptime(d, '%Y-%m-%d')

        return d

    news['date_format'] = news['date'].apply(date_month)

    news['year'] = news['date_format'].apply(lambda dt: dt.year)
    news['month'] = news['date_format'].apply(lambda dt: dt.month)


    news[news['buh_importance_news']>0.5].sort_values(['year', 'month'])[:25]

    news_buh = news[news['buh_importance_news']>0.5].sort_values(['year', 'month']).copy().reset_index(drop=True)

    set(re.sub(r'\s+', ' ', re.sub("[^a-zA-Zа-яА-Я]", " ", news_buh['lem_title'][0])).strip().split(' '))

    news_buh['set_lem_title'] = news_buh['lem_title'].apply(lambda text: set(re.sub(r'\s+', ' ', re.sub("[^a-zA-Zа-яА-Я]", " ", text)).strip().split(' ')))
    news_buh['set_lem_title']


    for i in range(len(news_buh)):
        n_1 = news_buh['set_lem_title'].iloc[i]
        news_buh['ind_'+str(i)]  = news_buh['set_lem_title'].apply(lambda n_2: len(n_1 & n_2) / len(n_1 | n_2))

    news_buh[['year','month','date_format', 'title', 'ind_580']][news_buh['ind_580']>0.24].sort_values(['year', 'month'], ascending=False)[:20]

    news_lst = []
    for news in news_buh[-7:]["title"]:
        news_lst.append(news)
    conn.write_trends(news_lst)
