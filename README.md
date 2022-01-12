# Buildings of Dimitrovgrad (EN)

## What is this?

This project was created to collect data of all buildings located in Dimitrovgrad, Ulyanovsk region, Russia.

## Some words for search

**The table of keys**

|Key|Value|
|---|---|
|Country|Russia|
|Region|Ulyanovsk Oblast|
|ISO 3166-1|RU|
|ISO 3166-2|RU-ULY|
|Code ОКАТО|73405|
|Code ОКТМО|73705000001|
|Name|Dimitrovgrad|

## What I use?

* *TMP* Open Data of alta.ru: [alta.ru](https://www.alta.ru)
* Open Data of Reforma GKH: [reformagkh.ru](https://www.reformagkh.ru/opendata)
* Open Street Map: [openstreetmap.org](https://www.openstreetmap.org)
* *TMP* Datata API: [dadata.ru](https://dadata.ru)
* Federal Information Address System: [fias.nalog.ru](https://fias.nalog.ru)
* *TMP* Open Data from [dom.mingkh.ru](https://dom.mingkh.ru)

## Features
*[Under construction | Read ru version* ⬇ *]*

## What I have to do
*[Under construction | Read ru version* ⬇ *]*

## What I want to see as a result
*[Under construction | Read ru version* ⬇ *]*

## Thanks
To the project [how-old-is-this.house](how-old-is-this.house).
# Дома Димитровграда (RU)

## Что это такое?

Этот проект создан для того, чтобы собрать данные по всем домам города Димитровграда, Ульяновская область, Россия.

## Несколько слов для поиска

**Таблица ключей**

|Ключ|Значение|
|---|---|
|Страна|Россия|
|Область|Ульяновская область|
|Код страны по ISO 3166-1|RU|
|Код региона по ISO 3166-2|RU-ULY|
|Код ОКАТО|73405|
|Код ОКТМО|73705000001|
|Название|Димитровград|

## Что я использую?

* *TMP* Общедоступные данные с сайта [alta.ru](https://www.alta.ru)
* Открытые данные с сайта Реформы ЖКХ: [reformagkh.ru](https://www.reformagkh.ru/opendata)
* Open Street Map: [openstreetmap.org](https://www.openstreetmap.org)
* *TMP* Datata API: [dadata.ru](https://dadata.ru)
* Федеральная Информационная Адресная Система: [fias.nalog.ru](https://fias.nalog.ru)
* *TMP* Данные сайта [dom.mingkh.ru](https://dom.mingkh.ru)

## Реализовано

* Сбор информации с сайта [alta.ru](https://www.alta.ru). Теперь у нас есть коды ФИАС по домам Димитровграда (естественно, только те, что есть на этом сайте).
* [Увы, у dadata поменялись условия: DEPRECATED] *С помощью библиотеки [dadata](https://dadata.ru) получаем кучу хорошей инфы. Главное из всего этого - это точка на карте и адрес.*
* На сайте [dom.mingkh.ru](https://dom.mingkh.ru) есть данные по годам постройки некоторых домов. Собираем их оттуда.
* Из файлика [OSM](https://www.openstreetmap.org) достаём свойства и координаты домов, всячески обрабатываем эти данные.

## Что надо сделать

* Перестать мучить сайт [alta.ru](https://www.alta.ru), перейти на свой экземпляр ФИАС.
* Убить использование dadata и смочь без них.
* Обработка ФИАС.
* Создание БД.
* Соединение БД ФИАСа с программой.

## Какой я хочу результат?

1. Собраны все возможные данные по домам города:
   * Весь ФИАС,
   * Год постройки дома,
   * Архитектор,
   * Объекты культурного наследия,
   * Аварийные дома,
   * Расселяемые,
   * Частные,
   * Многоквартирные,
   * Может, ещё что-то))
2. Создана БД с данными ФИАС, [dom.mingkh.ru](https://dom.mingkh.ru) и другими.
3. Создано веб-приложение / сайт с интерактивной картой.
4. Веб-приложение доступно в сети.

## Спасибо за вдохновление меня

Проекту [how-old-is-this.house](how-old-is-this.house). Их прекрасные работы завораживают и цепляют на долгие часы, дни и недели - тут уже у кого как получится.