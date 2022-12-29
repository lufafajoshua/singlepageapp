#installation
#Install Matplotlib separately
pip install matplotlib==3.6.2

sudo apt-get install python-matplotlib==3.6.2
#Then run the command to install all the project requirements
Run "pip3 install -r requirements.txt" 



#configuration
this application uses Mysql for the database connection
Change the database settings to your desired values inside the settings.py file

Run the project with python manage.py runserver

#Create a project superuser with python manage.py createsuperuser

Use the superuser details in the admin with the 127.0.0.1:8000/admin login link to add data to the database

After use 127.0.0.1:8000 to land on the home page

