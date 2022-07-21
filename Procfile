release: python manage.py migrate --database=default
release: python manage.py migrate --database=order
release: python manage.py migrate --database=product
web: gunicorn core.wsgi