# **Project Title**

## Overview


## User Experience (UX)


## Data Model Design


### Features Left to Implement


## Testing


### Version Control

### Set Up Locally
## Install Django & Supporting Libraries:
    1   fork the repository from GitHub
    2   pip3 install 'django<4' gunicorn
    3   pip3 install dj_database_url psycopg2 (libraries needed for postgres)
    4   pip3 install djangorestframework
    5   set up env.py, import os and copy in the secret key
    5   pip3 freeze –local > requirements.txt
    6   python3 manage.py makemigrations
    7   python3 manage.py migrate
    8   double check requirements.txt has the following:
        *  asgiref==3.5.2
        *  dj-database-url==0.5.0
        *  Django==3.2.13
        *  djangorestframework==3.13.1
        *  gunicorn==20.1.0
        *  psycopg2==2.9.3
        *  pytz==2022.1
        *  sqlparse==0.4.2 
    9   open up local host and go to /admin & use superuser login details


## Credits
### Research Links
