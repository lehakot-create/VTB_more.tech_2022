import pathlib

from tensorflow import keras
import pandas as pd
import numpy as np
import re
import json
import pickle
import pymorphy2  # лемматизация текста
import nltk
from nltk.corpus import stopwords


nltk.download('stopwords')  # Подгружаем стоп слова

# Загружаем сохраненную модель
model = keras.models.load_model('utils/best_model.hdf5')


# Предобработка данных

# Внутренние функции

def preprocess_text(text):
    # оставляем только буквы
    text = re.sub("[^a-zA-Zа-яА-Я]", " ", text)  # [^a-zA-Zа-яА-Я\d+]

    # Удаляем лишние пробелы
    text = re.sub(r'\s+', ' ', text)

    # Приводим к нижнему регистру
    text = text.lower()

    return text


def stop_words(x):
    x = list(x.split())
    russian_stopwords = stopwords.words('russian')
    new_x = []
    for w in x:
        if w not in russian_stopwords:
            new_x.append(w)
    return new_x


def data_prepocessing(value):
    text_title = value['title']

    text_description = value['description']
    autor = value['link'].lstrip('htps://w.').split('.')[0]

    # отчистка от символов - оставляем только буквы
    text_title = preprocess_text(text_title)
    text_description = preprocess_text(text_description)

    # Приводим к нормализованным формам
    morph = pymorphy2.MorphAnalyzer()
    text_title = morph.parse(text_title)[0].normal_form
    text_description = morph.parse(text_description)[0].normal_form

    # Удаляем стоп-слова
    text_title = stop_words(text_title)
    text_description = stop_words(text_description)

    # Токенизируем текст
    abspath = pathlib.Path("tokenizer.pickle").absolute()
    print(abspath)
    with open('/app/utils/tokenizer.pickle', 'rb') as f:
        tokenizer = pickle.load(f)
    text_title = tokenizer.texts_to_sequences([text_title])
    text_description = tokenizer.texts_to_sequences([text_description])

    # Указываем здесь, так как модель обучалась на такой ширине датасета
    max_words = 19
    text_title = keras.preprocessing.sequence.pad_sequences(text_title, maxlen=max_words, padding='post',
                                                            truncating='post')
    text_description = keras.preprocessing.sequence.pad_sequences(text_description, maxlen=max_words, padding='post',
                                                                  truncating='post')

    return text_title, text_description, autor


def data_prepocessing(value):
    text_title = value['title']
    text_description = value['description']
    autor = value['link'].lstrip('htps://w.').split('.')[0]

    # отчистка от символов - оставляем только буквы
    text_title = preprocess_text(text_title)
    text_description = preprocess_text(text_description)

    # Приводим к нормализованным формам
    morph = pymorphy2.MorphAnalyzer()
    text_title = morph.parse(text_title)[0].normal_form
    text_description = morph.parse(text_description)[0].normal_form

    # Удаляем стоп-слова
    text_title = stop_words(text_title)
    text_description = stop_words(text_description)

    # Токенизируем текст
    with open('utils/tokenizer.pickle', 'rb') as f:
        tokenizer = pickle.load(f)
    text_title = tokenizer.texts_to_sequences([text_title])
    text_description = tokenizer.texts_to_sequences([text_description])

    # Указываем здесь, так как модель обучалась на такой ширине датасета
    max_words = 19
    text_title = keras.preprocessing.sequence.pad_sequences(text_title, maxlen=max_words, padding='post',
                                                            truncating='post')
    text_description = keras.preprocessing.sequence.pad_sequences(text_description, maxlen=max_words, padding='post',
                                                                  truncating='post')

    return text_title, text_description, autor


def prediction_news(model, data):
    """ Предсказания важности новости. Диапозон значений от 0 до 1.
        Индекс для:
        0 - buh_importance_news
        1 - ruk_importance_news
    """
    pred = model.predict(data, verbose=0)
    return pred


def super_news(value):
    """
    Проверка - выдача результата:
    :param value:
    :return:
    """
    pred = []

    for i in range(len(value)):
        data = data_prepocessing(value[i])[0]
        result = prediction_news(model, data)[0]
        pred.append({'val_buh': result[0],
                     'val_ruk': result[1]})

    index_new_buh = pd.DataFrame(pred).sort_values(['val_buh'], ascending=False).index
    index_new_ruk = pd.DataFrame(pred).sort_values(['val_ruk'], ascending=False).index

    # -----------
    news_buh = [value[index_new_buh[0]], value[index_new_buh[1]], value[index_new_buh[2]]]
    news_ruk = [value[index_new_ruk[0]], value[index_new_ruk[1]], value[index_new_ruk[2]]]

    return news_buh, news_ruk


def main_neuro(value, conn):
    value = value[:50]

    top_news = super_news(value)
    buh = top_news[0]
    ruk = top_news[1]
    # print("buh", buh)
    # print("ruk", ruk[:2])
    conn.write_news('buh', ruk[:2])
    # print("buh", ruk[1:])
    conn.write_news("leaders", ruk[1:])


# if __name__ == "__main__":
#     # Здесь берется значение value из файла tmp.txt
#     value = value[:50]
#
#     top_news = super_news(value)
#     buh = top_news[0]
#     ruk = top_news[1]
#     print("buh", buh)
#     print("ruk", ruk)