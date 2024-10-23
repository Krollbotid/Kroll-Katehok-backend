# Developement environment

## Python local interpreter
```
pyenv install 3.12
pyenv local 3.12
```
Файл `.python-version` будет создан автоматически в папке проекта, чтобы хранить информацию о версии Python, используемой локально.

## Tell poetry to use the correct version of the interpreter
Определяем, где находится интересующий интерпретатор
```
pyenv which python
```
Указываем `poetry` использовать этот интерпретатор (если не сделали этого ранее)
```
poetry env use <path_to_the_interpreter>
```

## Install dependencies
Устанавливаем зависимости из `pyproject.toml`
```
poetry install
```

## Run env
Запускаем окружение
```
poetry shell
```

## Run dev server
Внутри окружения переходим в директорию django-проекта


Запускаем сервер:
```
python manage.py runserver
```

## Close env
Выполнить:
```
exit
```