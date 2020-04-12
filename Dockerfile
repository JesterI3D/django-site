FROM django

ADD mysite /django-site/mysite

WORKDIR /django-site

EXPOSE 8000

RUN pip install -U pip

RUN pip3 install --upgrade django
RUN pip3 install -r requirements.txt

ARG PYTHON_VERSION=3.8
ENV PYTHON_VERSION=$PYTHON_VERSION
ENV PYTHON=python${PYTHON_VERSION}

ENTRYPOINT ["python3.8", ". /manage.py"]

CMD ["runserver", " 0.0.0.0:8000"]
