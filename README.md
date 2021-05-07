# ASD API

## Prerequisites

* Must have installed Python **2.7** or **3.5+**

## Local Setup

By opening your command line, execute the following:

### 1. Install [Poetry CLI](https://python-poetry.org/) (Package Manager)

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

Verify that the `poetry` command is available

```
poetry --version
// Should be on version 1.1.6

// Otherwise update poetry CLI
poetry self:update
```

### 2. Install project dependencies
```
poetry install
```

### 3. Activate virtualenv
```
poetry shell
```

### 4. Install database migrations
```
./manage.py migrate
```

### 5. Load initial data to DB
```
./manage.py loaddata manifesto/fixtures
```

### 6. Setup Django Secret Key

First, generate a random value for our secret key

```
./generate_secret.py
```

Then, go to `asd_api` folder and duplicate `.env.tpl` to `.env` and copy/paste the random value generated to `DJANGO_SECRET_KEY`
```
DJANGO_SECRET_KEY=<your-random-value>
```

### 7. Run the server
```
./manage.py runserver
```

## Transacting with the API

For this project, we used token based authentication whenever we do an API request.

*Make sure you have a user registered in DB*, otherwise you can create your first super user account:

```
./manage.py createsuperuser
```

Create a token related to the account, it should print out the token value right after execution


```
./manage.py drf_create_token <your-username>
```

You can now send API request by adding this header in your request

```
Authorization: Token <your-token-key>
```
