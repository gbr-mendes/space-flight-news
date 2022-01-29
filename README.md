
# Space Flight News - Challenge
This is an API clone of the Space Flight News Api that aggregate news of the space built with python.

This is a challenge by [@coodesh](https://coodesh.com/)


## Authors

- [@gabrielmendes](https://www.github.com/gbr-mendes)


## Installation with Docker
- Make sure that you have docker an docker-compose installed:
    - docker --version
        - Expect output: Docker version 20.10.12, build e91ed57
    - docker-compose --version
        - Expect output: docker-compose version 1.29.2, build 5becea4c

- Clone this repo to somewhere on your computer:
    - git clone https://github.com/gbr-mendes/space-flight-news.git

- Change workspace to cloned repo:
    - cd space-flight-news

- Build the container
    - docker-compose up

- Access the application:
    - [127.0.0.1:8000](http://127.0.0.1:8000)

## Installation with virtualenv
- Make sure tha yoy have python and virtualenv installed
    - python --verison
        - Python 3.8.10
    - virtualenv --version
        - Expect output: virtualenv 20.0.17

- Clone this repo to somewhere on your computer:
    - git clone https://github.com/gbr-mendes/space-flight-news.git

- Change workspace to cloned repo:
    - cd space-flight-news

- Create a virtualenv to aggregate the dependencies:
    - virtualenv .venv

- Active the virtualenv:
    - source .venv/bin/activate

- Install the dependencies:
    pip install -r local_requirements.txt

- Define your DB:
    - Open the directory with a code editor:(Exemple with vs code)
        - code .
    - Go to app/app/settings/base.py and navigate to databases section
        - Comment the defined database config
        - Uncomment the database system that you want to use. You can use the dafault database system of dango(dbsqlite) or postgres in case you have it installed on your machine.
    - Run python manage.py migrate
    - Run python manage.py runserver
    - Access your application - [127.0.0.1:8000](http://127.0.0.1:8000)


## API Reference

#### Get all Articles from db

```http
  GET /articles/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `limit` | `int` | Get the articles with limit as page size|

#### Get An especific article


```http
  GET /articles/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `uuid` | **Required**. Id of item to fetch |


#### Create a new article
```http
  POST /articles/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `uuid` | Id of item to fetch - Autogenerated |
| `featured`      | `bool` | Default is false |
| `title`      | `string` | **Required**. Title for article |
| `url`      | `string` | **Required**, url to link to the article |
| `imageUrl`      | `string` | **Required** url to the image of the article |
| `newsSite`      | `string` | **Required** Name of the news site of the article |
| `summary`      | `string` | **Required** Summary for the article |
| `publishedAt`      | `string` | Publish date of the article - Autogenerated|
| `launches`      | `list` | List of launchs |
| `event`      | `list` | List of launchs |


#### Update an especific article
```http
  PUT /articles/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `featured`      | `bool` | Default is false |
| `title`      | `string` | **Required**. Title for article |
| `url`      | `string` | **Required**, url to link to the article |
| `imageUrl`      | `string` | **Required** url to the image of the article |
| `newsSite`      | `string` | **Required** Name of the news site of the article |
| `summary`      | `string` | **Required** Summary for the article |
| `publishedAt`      | `string` | Publish date of the article - Autogenerated|
| `launches`      | `list` | List of launchs |
| `event`      | `list` | List of events |


#### Delete an especific article
```http
  DELETE /articles/${id}
```

#### You can try all the methods in https://agile-eyrie-93985.herokuapp.com/articles. Ps: Use raw data

## Addition commands

You can populate your database with either docker or virtualenv:

- virtualenv
    - With your venv active run:
        - python manage.py filldb

- docker
    - Stop your container and run:
        - docker-compose run --rm app sh -c "python manage.py filldb"
    - Re-run the container:
        - docker-compose up


## Atention

Considering the challenge requirements, and when it comes to the cron definition, I could not define it in the container or in prod. However, the script has been defined and can be activated with virtualenv:

- With your venv active run:
    - python manage.py crontab add
