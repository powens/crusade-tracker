FROM python:3-stretch
ENV PYTHONUNBUFFERED=1
WORKDIR /server

RUN pip install poetry
COPY poetry.lock pyproject.toml /server/
#RUN poetry config virtualenvs.create false \
RUN poetry install --no-dev --no-interaction --no-ansi

COPY . /server/