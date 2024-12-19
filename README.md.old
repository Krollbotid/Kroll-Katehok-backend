# Goods Catalog

## Deploy

### Install `pyenv` and `poetry`

В проекте используются утилиты `pyenv` - для управления версиями интерпретатора `python` и `poetry` - пакетный менеджер для зависимостей проекта.

[Install `pyenv` and `poetry` | Guide for Windows](./guide/INSTALL_DEV_ENV_TOOLS.md)

### Run Django dev-server

Протестировать работоспособность проекта можно при помощи тестового веб-сервера django.

[Set up environmets and run dev-server | Guide](./guide/README.md)

## Repo Structure
- `/`
    - `README.md` - о пректе
    - `.gitignore` - исключения `git`
    - `guide/` - гайды по настройке окружения разработки
    - `diagrams/` - UML-диаграммы проекта
        - `drawio/` - исходники (`.drawio`)
        - `png/` - изображения (`.png`)
    - `project/` - директория разработки проекта
        - `.python-version` - версия интерпретатора `python`
        - `pyproject.toml` - зависимости проекта
        - `poetry.lock` - полный список зависимостей `poetry`
        - `goods_catalog/` - директория `django`-проекта
            - `db.sqlite3` - (временная) база данных проекта
            - `manage.py` - скрипт управления проектом
            - `goods_catalog/` - директория приложения настроек проекта
            - `users/` - директория приложения аутентификации/авторизации пользователей проекта
            - `catalog/` - директория приложения каталога проекта
            - `support/` - директория приложения службы поддержки проекта
