FROM python:2.7

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE "coinsdashboard.settings.test"

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt

COPY . /code/

RUN chmod +x wait-for-it.sh
RUN chmod +x start_server.sh

EXPOSE 8000

CMD [ "./start_server.sh"]