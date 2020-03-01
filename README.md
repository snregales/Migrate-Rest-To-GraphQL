# Prerequisite
- Docker/Podman
- Docker Compose
- Pyenv (optional)
- Python 3.7
    - Pipenv

# Installing

### Environment Variables

create a .env file in the project root directory. project root is where manage.py is located. 
And add the following keys to it

`DJANGO_SETTINGS_MODULE=config.settings.dev
SECRET_KEY=not-so-secret`

The `DJANGO_SETTINGS_MODULE` holds the location of the settings configuration file

### Docker Compose
Run the following command from the project root directory, to start database and database-admin containers
`docker-compose up`

### Python Dependencies

##### If you are running _pyenv_:

- Install python version 3.7 `pyenv install 3.7.x` 
- Either run `pyenv local 3.7.x` or manually create a file name _.python-version_ 
with the python version in it
- Check project python version `python -V`

##### install Pipenv
To minimize python version problems we are gonna run pip from the perspective of python self
- Update pip to the latest version `python -m pip install -U pip`
- Install Pipenv `python -m pip install pipenv`
- Create an alias MacOS and Linux `alias penv='python -m pipenv`, Windows `Set-Alias -Name penv -Value 'python -m pipenv'` 
(optional)

##### Install Application Dependencies
- Head to the project root directory
- If you are participating in the workshop, than install all dependencies with `penv install --dev` or `python -m pipenv install --dev` 
- otherwise if you are just running the system `penv isntall` or `python -m pipenv install` should be enough

# Usage

I already made our life simpler by adding the most use manage.py commands to scripts section in our Pipfile

### Start BackEnd Server

Open an separate terminal and Head to the project root directory
Here is where our alias _penv_ will become really handy

- Migrate all tables to the database `penv run migrate`
- Create super user `penv run manage createsuperuser`
    - follow the prompt
- Start server `penv run server`.
 If server port already in use, than execute `penv run server <port>` with a free port

### Migrations

If you are participating in the workshop, whenever you edit a model. you must:

- commit your created/updated model for database migrations `penv run commit`
- push created/updated migrations to the database `penv run migrate`

If you just created a new model and sequentially try to commit the changes to migrations. you will get the following 

`Loading .env environment variables…
No changes detected
` 

This is because the application label for the  where your model resides is not yet added to project install apps.
You can add the application label to `MY_APPS` list in the _base.py_ module.
