# Получение данных о домах города
import requests as rq
import pandas as pd
import json
from dadata import Dadata
from bs4 import BeautifulSoup as bs
# ШАГ 0. Создаём функции
# Обработка результатов от dadata.ru
def create_line(result):
    line1 = {}
    line1.update({'value':result[0]['value']})
    line1.update({'unrestricted_value':result[0]['unrestricted_value']})
    for keys in result[0]['data'].keys():
        line1.update({keys:result[0]['data'][keys]})
    return line1
# Получение кодов 
def parser(site):
    source = rq.get(site).content
    soup = bs(source, 'html.parser')

    table_label = soup.findAll('th')
    table_data = soup.findAll('td')

    table_data_list = []
    for item in list(table_data):
        table_data_list.append(item.string)
    result = {}
    for k in range(0, len(table_data_list), 6):
        result.update({table_data_list[k]:table_data_list[k+2:k+6]})

    return result
def houses_by_street(site):
    source = rq.get(site).text
    soup = bs(source)
    href = []
    for item in soup.findAll('a', class_="kladrs-objects__number"):
        attr = item.attrs
        href.append(attr['href'])
    return href
# ШАГ 1. Получаем коды улиц города
# alta.ru Улицы по коду города
source = rq.get('https://www.alta.ru/fias/73b29372-242c-42c5-89cd-8814bc2368af/').text
soup = bs(source)
href = []
for item in soup.findAll('a', class_="jFastSearch_key"):
    attr = item.attrs
    href.append(attr['href'])
fias_streets = []
for item in href:
    fias_streets.append(item[6:-1])
del([item, soup, source, href])
# ШАГ 2. Получаем коды домов по кодам улиц
# alta.ru Дома по коду улицы
fias_houses = []
for street_code in fias_streets:
    site = 'https://www.alta.ru/fias/' + street_code + '/'
    fias_houses.append(houses_by_street(site))
fias_houses_all = []
for item in fias_houses:
    for elem in item:
        fias_houses_all.append(elem)
fias_houses_codes = []
for item in fias_houses_all:
    fias_houses_codes.append(item[6:-1])
# ШАГ 3. Получаем данные по кодам домов
# dadata.ru Поиск данных по коду дома
token = str(open('E:/CODE/BUILDINGS_OF_DIMITROVGRAD/access_3.txt', 'r').read())
dadata = Dadata(token)

full_info = []
for code in fias_houses_codes:
    result = dadata.find_by_id("address", code)
    full_info.append(create_line(result))
