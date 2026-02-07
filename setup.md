# Instructions on how to deploy the site


## Part 1: New Postgres on Render.com

Create a new Postgres on Render.com

Name the postgres and database

Choose the Free plan and press Create Database

Copy the Internal Database URL to your clipboard (you'll need it shortly)


<br>

## Part 2: New Web Service on Render.com

Create a new Web Service on Render.com

Select the Git repository where you committed your files.

Give your web service a name

### Additional settings:

Root Directory:

fanfic_site/  (Note: This depends on what folder you upload to Github and may not be necessary)

Build Command:

uv sync && uv run manage.py collectstatic && uv run manage.py migrate && uv run manage.py ensure_adminuser

Start Command:

gunicorn fanfic_site.wsgi:application


## Part 3: Environment variables

Create the following environment variables.

CLOUDINARY_API_KEY - Create a Cloudinary account to get this

CLOUDINARY_API_SECRET - Same as above

CLOUDINARY_CLOUD_NAME - Same as above

DATABASE_URL - Paste in the Internal Database URL from the Postgres

DEBUG - FALSE

DJANGO_SUPERUSER_EMAIL - Add your email here

DJANGO_SUPERUSER_PASSWORD - Add/generate a password here

DJANGO_SUPERUSER_USERNAME - Choose a username

EMAIL_HOST_USER - Use a Gmail account

EMAIL_HOST_PASSWORD - Add the Gmail app password here (this only works on a paid Render plan) 

SECRET_KEY - Generate a secret key