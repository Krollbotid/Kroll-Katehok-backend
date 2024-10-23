# Goods Catalog

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
            - `goods_catalog/` - директория главного приложения проекта
