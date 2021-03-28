FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN python manage.py migrate
RUN python manage.py collectstatic
COPY . /code/
# CMD gunicorn coach.wsgi:application --bind 0.0.0.0:$PORT
