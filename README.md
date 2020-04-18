# Movie-APP
This is a simple Internet Movie Database (IMDB) clone project with Django framework. It features the core  
functionalities of IMDB which include the ability to - 
* register to the site
* login as a user
* upload movies as an admin
* view available movies as a user
* vote for movies as a user
* view top movies according to user's vote
* see the list of movies a person has acted in, writes and directed.
* and lots more.

## Tech Implementation Stack
* Python Programming Language
* Django Web Framework
* PostreSQL Database

##  How to Setup
Follow the under-listed procedures to setup locally and to test this project on your local machine.

#### * Create a new directory on your local machine and setup a virtual environment inside it OR
#### * If you are using PyCharm IDE, just setup a new project environment.

#### * Activate the virtual environment

#### * Clone the project files into the directory on your local machine
git clone https://github.com/Timothy-py/Movie-APP.git

#### Install the dependencies
pip3 install -r requirements.txt

### Install PostgreSQL on your local machine
* Search online on how to install and setup PostgreSQL for your Operating System.
* After the installation is successful, create a database and a user for the database.
* Go to config/dev_settings.py in your project directory and change the NAME, USERNAME and PASSWORD value  
    of the DATABASE dictionary to the one used to configure your database.

### Database Migration
* In your project directory run the following commands  
_python manage.py makemigrations_  
_python manage.py migrate_

### Create a Superuser
* Run the command  
_python manage.py createsuperuser_

### Start the django server
* Run the command  
_python manage.py runserver_

### Go to your browser to interact with the admin page and the app
_localhost:8000/admin_
_localhost:8000/movies_

###### contact me @  adeyeyetimothy33@gmail.com
