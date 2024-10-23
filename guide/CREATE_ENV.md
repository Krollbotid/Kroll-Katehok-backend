# Creation dev environment

## Install tools
[Follow this guide](./INSTALL_DEV_ENV_TOOLS.md)

## Python local interpreter
```
pyenv install 3.10.4
pyenv local 3.10.4
```
Файл `.python-version` будет создан автоматически в папке проекта, чтобы хранить информацию о версии Python, используемой локально.

## Init env
Запустить инициализацию окружения
```
poetry init
```
Выбрать необходимые параметры (два последних пункта - no)

Создастся `pyproject.toml`, описывающий все зависимости проекта

## Tell poetry to use the correct version of the interpreter
Определяем, где находится интересующий интерпретатор
```
pyenv which python
```
Указываем `poetry` использовать этот интерпретатор
```
poetry env use <path_to_the_interpreter>
```

## Add Django
Запустить 
```
poetry add django
```
В `pyproject.toml` добавится зависимость `django`

## Run env
Запускаем окружение
```
poetry shell
```

## Create django-project
Создаем проект `django`
```
django-admin startproject goods_catalog
```

## Close env
Выполнить:
```
exit
```