# **Weather API**

## Overview
This application is a proof of concept REST API that aims to receive weather data from various sensors in different locations that report metrics such as temperature, humidity and wind speed on specific dates.

By using the Django Rest Framework, this application allows full CRUD by allowing the user to GET, Post, Put & Delete the sensors data.

Please follow the instructions below for forking and running this application locally.

Important enpoints include:

    *   /sensors.json
    *   /admin
    *   /sensors
    *   /sensors/1
    *   /sensors/2

## User Stories
1   As a user I would like to be able to navigate to the site so that I can view the api data from the sensors in json format.

2   As a user I would like to be able to register sensors by id and store it’s metadata such as country name and city name so that I can view the specific sensors by these categories.

3   As a user, once a sensor has been registered, the application can receive new metric values as the weather changes around the sensor via an API call.

4   As a user I would like to query sensor data so that I can find one or more sensors by id and the average metrics associated with each sensor.

5   As a user I would like to query sensor data by a date range (between one day and a month.


### User Experience in this Application
This application takes the users stories mentioned above into consideration to create a positive UX.  The user’s experience is discussed in more detail below with examples of how they can achieve each one.

*   Using Django’s Rest Framework, format_suffix_patterns was imported to create a url pattern to allow the endpoint to show the data for the user in json format when /sensors.json is used.

*   By going to the /admin endpoint, signing into Django’s build in GUI for admin users and navigating to the sensors section on the left:

a)	Users can view all the sensors with their meta data listed.

b)	There is also the option to add or register a sensor by id and include meta data such as country & city.

c)	Users can also select a specific sensor to view the metrics associated with that sensor.

d)	After selecting a specific sensor, users can then update the data or delete the sensor and it’s data altogether.

e)	Here on the right hand side, there is a customised filer panel that will allow the user to filter sensor by id and/or by date range.

*   By going to the endpoint /sensors will give the user the Django Rest Framework built in GUI the user can:

a.	View the list of sensors by id, including all metadata and metrics associated with it.  

b.	Users can then add sensors here and include all relevant data associated with that new sensor.

*   By including the sensors id in the endpoint, for example /sensors/1 the user can:
a)	View this sensor’s data and update accordingly by using PUT.

b)	Delete this sensor and it’s associated data.

*   Django comes with it’s own input validation and exception handling on the /admin site once the data entered in the model is placed as required.  Users are given feedback through statements and flash messages when they sign in, input data and sign out.

*   Try / Except statements were used throughout the views to ensure the user was given the status error and a message when an exception occurred such as 400 when a bad request is made, 404 if an item is not found on search, and 201 when item created.

If you would like to view some of the features mentioned above please view this [Walk Through Video](static/media/readme/weatherapi-video.mp4)

### Features Left to Implement:

As this was a proof of concept project not all features were implemented at this stage.  Features that could be worked on at a later date include:

*   Customising the frontend design for the user by editing django’s built in template files that are displaying at the moment and linking up a base.html page for the home page could be achieved easily.

*   Future development could also include using a Fetch request on a site such as Met Eireann, save the data as raw, create a clean up function to prepare it for presentation and then feed it into a charting library such as www.chartjs.org

*   As mentioned below further full testing is needed. 


## Testing
### Manual Testing:

*   Errors or warnings were fixed as they appeared such as indentation errors, lines too long or extra space issues. This helped keep the code clean and readable so other errors or bugs that arose were identified more easily.

*   Testing inputs were used to ensure user inputs would be handled correctly and appropriate feedback to the user was shown on screen.  For example, through the /admin section test data was Created, Read, Updated & Deleted to ensure functionality and Django’s flash messages appeared correctly for the user when required.


*   In the browser, Dev Tools was used to view the network and inspect that the status was 200 and the data was being displayed correctly.

*   The README.md was proofread, passed through Grammarly and all links were checked before final submission.

### Automated Testing:
*   Testing was completed using pytest.  Full test coverage was not achieved due to time constraints but given more time this would be achieved in full.


### Validator Testing:
*   Pep8 online was used for validating the python files. Not all python files were checked due to time constraints but the sterilizers.py file was deemed the most important to check at this point.


### Framework & Language:
*   Django Framework
*   Django Rest Framework
*   Python
*   Pytest


## Set Up Locally

    1   fork the repository from GitHub
    2   pip3 install 'django<4' gunicorn
    3   pip3 install dj_database_url psycopg2 (libraries needed for postgres)
    4   pip3 install djangorestframework
    5   pip3 install pytest django
    6   set up env.py, import os and copy in the secret key
    5   pip3 freeze –local > requirements.txt
    6   python3 manage.py makemigrations
    7   python3 manage.py migrate
    8   double check requirements.txt has the following:

        *  asgiref==3.5.2
        *   dj-database-url==0.5.0
        *   Django==3.2.13
        *   djangorestframework==3.13.1
        *   gunicorn==20.1.0
        *   iniconfig==1.1.1
        *   pluggy==1.0.0
        *   psycopg2==2.9.3
        *   py==1.11.0
        *   pytest==7.1.2
        *   pytest-django==4.5.2
        *   pytz==2022.1
        *   sqlparse==0.4.2

    9   open up local host and go to /admin & use superuser login details


## Credits
### Research Links
*   [Django Rest Framework Docs](https://www.django-rest-framework.org/)
*   [Django Framework Docs](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/)
*   [Django Rest API - GeeksforGeeks](https://www.geeksforgeeks.org/how-to-create-a-basic-api-using-django-rest-framework/)
*   [Building Django Crud - Article](https://www.sankalpjonna.com/learn-django/building-a-django-crud-application-in-minutes)
*   [Build Django Framework API - YouTube](https://www.youtube.com/watch?v=i5JykvxUk_A)
*   [Testing in Djago Rest - Article](https://tamerlan.dev/how-to-test-drf-apis/)
*   [Testing with Pytest](https://djangostars.com/blog/django-pytest-testing/)
*   [Generic Views in Django Rest](https://www.django-rest-framework.org/api-guide/generic-views/)
*   [Simple Restful API - YouTube](https://www.youtube.com/watch?v=BSHRftLtPEg)
