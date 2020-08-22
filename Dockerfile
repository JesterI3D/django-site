FROM django

EXPOSE 8000

COPY . /mysite/

ADD mysite /django-site/mysite

WORKDIR /django-site

RUN pip install --upgrade pip
RUN pip3 install -r mysite/requirements.txt
RUN pip3 install psycopg2 && pip3 install psycopg2-binary
RUN pip3 install django --upgrade && pip3 install djangorestframework --upgrade

ARG PYTHON_VERSION=3.7
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod a+x /docker-entrypoint.sh
ENTRYPOINT /docker-entrypoint.sh

#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mysite.wsgi:application"]