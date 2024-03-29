FROM python:3.11

# Устанавливаем Poetry
RUN pip install poetry

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