FROM python:3.13.0-slim

WORKDIR /app

COPY . /app/

RUN pip install beehive

EXPOSE 80

CMD [ "python3", "app.py" ]