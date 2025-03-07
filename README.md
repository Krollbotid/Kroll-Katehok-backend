# Учебный проект CRM система на Django

## Титульный лист
![Титульный лист](diargrams/png/title.png)

## Представление предметной области
Сайт-каталог товаров – это веб-ресурс, предназначенный для систематизации и представления информации о товарах или услугах с целью упрощения их поиска, выбора и покупки. Основными функциями являются: структурированное отображение категорий и товаров, удобный поиск с фильтрацией, информативные карточки товаров с описанием, ценами и отзывами, а также связь со службой поддержки через чаты. Проект включает интеграцию с и базой данных, обеспечивая безопасность, скорость.

## Описание проекта
Проект - сайт каталог товаров, можно сортировать по производителю, продавцу, цене, количеству.
Пользователи могут создавать свои карточки товаров и редактировать их, также есть возможность
создания чата с тех поддержкой, доступ к кторому имеют только создатель и суперпользователи.
При отправке сообщения в чате идет отправка письма на электронную почту через отдельный сервис.

## Планирование проекта
### ER-диаграмма
![](diargrams/png/ER.png)

### Диаграмма классов
![](diargrams/png/class.png)

### Диаграмма последовательностей
![](diargrams/png/sequence.png)

### Диаграмма ганта
![](diargrams/png/gant.png)

## How To Use It
- Install vagrant.
- Clone this repository manually
```
git clone https://gitlab.digital.mephi.ru/Katehok/goods_catalog
```
- Enter into to the "virtual" directory
- Start virtual machine
```
vagrant up
```
- Open localhost:8080
- Allow your browser open this page

## Использование уведомлений по почте
- Для нужен пароль приложения от гугла и имя пользователя, которые надо вписывать в virtual/.env
