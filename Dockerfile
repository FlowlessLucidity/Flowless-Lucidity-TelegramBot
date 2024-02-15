FROM python:3.11

# Устанавливаем Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Обновляем переменную PATH, чтобы включить исполняемые файлы Poetry
ENV PATH="/root/.poetry/bin:${PATH}"

# Копируем файлы зависимостей и устанавливаем их
COPY poetry.lock pyproject.toml /app/
WORKDIR /app
RUN poetry install

# Копируем код в контейнер
COPY . /app

# Запускаем приложение
CMD ["poetry", "run", "python", "main.py"]