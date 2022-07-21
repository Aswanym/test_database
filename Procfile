release: python manage.py migrate --database=default
release: python manage.py migrate --database=order_db
release: python manage.py migrate --database=product_db
web: gunicorn core.wsgi