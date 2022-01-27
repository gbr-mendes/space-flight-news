FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
# Install pre-requisites to pillow and psycopg
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

# Install project requirements
RUN pip install -r /requirements.txt

# Delete temp files
RUN apk del .tmp-build-deps

# Define app workdir
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# Add and switch for a non root user
RUN adduser -D user
USER user