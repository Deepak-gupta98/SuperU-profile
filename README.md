# SuperU-profile
This Repository is for SuperU. I have created Django End point to get, create and update SuperU profile.
Profile model contain 4 fields <ol> <li>name </li> <li> email </li> <li> bio </li> <li> profile_picture</li> </ol>

How to run this program
<p> step-1: Download this repository through git clone</p>
<p> step-2: Install all dependencies using "pip install -r requirements.txt " command </p>
<p> step-3: Run " python manage.py makemigrations " and then " python manage.py migrate " command to fetch all the Django models. </p>
<p> step-4: Run the Django testing server through "python manage.py runserver " command </p>

I have used JWT Authentication. here access value will be add in Bearer Token which is created through 

<a>
curl --location 'http://127.0.0.1:8000/api/token/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username":"xxxxxxx",
    "password": "xxxxxx"
}'
</a>
<p> We will create username and password through " python manage.py createsuperuser " command</p>

<p> Now, We can create SuperU profile object and can update.Also we fetch all the Profile records using GET request</p>

=======================================================
<p>If you have any queries. you can contact me <b>Email: deepak953459@gmail.com </b> </P>
