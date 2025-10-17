# social_media_api

Simple Social Media API (Django + DRF) - Accounts & Authentication

## Setup
1. Create and activate virtualenv
2. Install dependencies:
   pip install -r requirements.txt
   # or pip install django djangorestframework djangorestframework-authtoken pillow

3. Set `AUTH_USER_MODEL = 'accounts.User'` in settings.py (before migrations)
4. Run migrations:
   python manage.py makemigrations
   python manage.py migrate
   python manage.py migrate authtoken

5. Create superuser:
   python manage.py createsuperuser

6. Run server:
   python manage.py runserver

## Endpoints
- POST /api/accounts/register/  -> Register new user (returns token)
- POST /api/accounts/login/     -> Login (returns token)
- GET/PUT /api/accounts/profile/   -> Get / update current user's profile (requires token)
- POST /api/accounts/users/<username>/follow/ -> Follow/unfollow user (requires token)

## Notes
- Authentication: TokenAuthentication (DRF authtoken).
- Use `Authorization: Token <key>` header to access protected endpoints.
- For production: use HTTPS, configure CORS, use proper media storage (S3), and consider switching to JWT or short-lived tokens.
