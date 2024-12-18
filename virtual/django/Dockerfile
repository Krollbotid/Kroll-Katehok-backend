FROM python:3.12-alpine3.20

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    # pip:
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_ROOT_USER_ACTION=ignore \
    # poetry:
    POETRY_VERSION=1.8.3 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_HOME='/usr/local' \
    ADMIN_STATIC_PATH='/var/www/static-admin-panel'

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev


RUN apk --no-cache add cargo curl \
    && curl -sSL 'https://install.python-poetry.org' | python - \
    && poetry --version

WORKDIR /usr/src/app

COPY ./poetry.lock ./pyproject.toml ./
RUN poetry run pip install -U pip \
    && poetry install --no-interaction --no-ansi --sync

COPY . .
