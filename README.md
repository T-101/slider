# Slider
Web app for image uploads and a slideshow
***
Deployment:
1. Create `.env` files in project root directory and change settings where needed. There are examples provided.
2. `docker compose build`
3. Uncomment preferred command in `docker-compose.yml`
4. `docker compose up` and surf to localhost:8000

It's a Django, so always helpful to run the usual commands to apply database migrations and create a superuser.
1. `docker compose run --rm app bash`
2. `python manage.py migrate`
3. `python manage.py createsuperuser`

Upload view is at localhost:8000 and slideshow is at localhost:8000/slider/
