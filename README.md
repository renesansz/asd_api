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

### 6. Run the server
```
./manage.py runserver
```
