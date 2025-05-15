FROM python:3.10

# Встановимо змінну середовища
ENV APP_HOME /app

WORKDIR $APP_HOME

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "pr_1/main.py"]