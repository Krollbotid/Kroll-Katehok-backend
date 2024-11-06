# Developement environment

Для запуска виртуального окружения необходимо перейти в директорию `/project/`:
```
cd project
```

## Python local interpreter

Если файл `/project/.python-version` отсутствует, необходимо выполнить:
```
pyenv install 3.12
pyenv local 3.12
```
Файл `/project/.python-version` будет создан автоматически, чтобы хранить информацию о версии Python, используемой локально.

## Tell poetry to use the correct version of the interpreter

Определяем, где находится интересующий интерпретатор:
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

Внутри окружения переходим в директорию django-проекта:
```
cd goods_catalog/
```

## Migrations

Если сервер запускается впервые или с последнего его запуска была обнавлена система моделей, необходимо создать и выполнить миграции:
```
python manage.py makemigrations
python manage.py migrate
```

## Add ticket statuses*

Для корректной работы необходимо убедиться, что модель `support.models.TicketStatus` содержит два обязательных статуса: `Ожидание` и `Отвечено`

Запустить командную оболочку `python`, импортировать модель `support.models.TicketStatus`
```
python manage.py shell
from support.models import TicketStatus
```

Вывести все записи модели:
```
TicketStatus.objects.all()
```

Если в выводе отсутствуют статусы `Ожидание` и/или `Отвечено`, добавить их:
```
TicketStatus.objects.create(name="Ожидание", description="Ожидание ответа сотрудника")
TicketStatus.objects.create(name="Отвечено", description="Получен ответ сотрудника")
```

Выйти из оболочки:
```
quit()
```

## Run dev server

Запускаем сервер:
```
python manage.py runserver
```

## Stop dev server

Для остановки тестового ссервера используйте горячие клавиши `Ctrl`+`C`

## Close env

Для выхода из виртуального окружения выполнить:
```
exit
```