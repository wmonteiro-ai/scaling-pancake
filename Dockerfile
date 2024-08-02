FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 80
COPY ./app /code/app
CMD ["fastapi", "run", "app/main.py", "--port", "80"]
