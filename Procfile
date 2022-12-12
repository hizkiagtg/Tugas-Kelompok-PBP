release: python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('adminwazzt', 'wazzt@gmail.com', 'wazzt123', is_admin = True)" &&
python manage.py migrate --run-syncdb
web: gunicorn project_django.wsgi --log-file -