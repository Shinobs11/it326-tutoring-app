echo "Plan database migrations"
python manage.py makemigrations


echo "Apply database migrations"
python manage.py migrate


echo "Generate test data"
python manage.py setup_test_data

echo "Starting server"
python manage.py runserver 0.0.0.0:8000

