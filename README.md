# Wingz Ride api
Clone Repo
 - git clone https://github.com/raphaeltorres/wingz-api.git

 Create virtualenv
 - virtualenv -p python3 wingzapi

 Activate virtualenv
 - source wingzapi/bin/activate

 Install Django
 - pip install -r requirements.txt
 - python manage.py migrate

# Create super to access the api
python manage.py createsuperuser

# Run Server
python manage.py runserver

# Login
http://localhost:8000/api/auth/login/

# API URLS
http://localhost:8000/api/users/
http://localhost:8000/api/rides/
http://localhost:8000/api/ride-event/

# Sample Filters
GET /api/rides/?status=pickup

GET /api/rides/?status=en-route&rider_email=test@gmail.com