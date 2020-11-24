FROM python:3.8

ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code
COPY . /code/

RUN pip install -r requirements.txt
RUN python app/manage.py collectstatic --no-input \
    && python app/manage.py makemigrations \
    && python app/manage.py migrate

CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "app", "MoneyLifeBack.wsgi:application"]

EXPOSE 8000