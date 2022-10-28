echo "Plan database migrations"
py manage.py makemigrations


echo "Apply database migrations"
py manage.py migrate


echo "Generate test data"
py manage.py setup_test_data

echo "Starting server"
py manage.py runserver 0.0.0.0:8000

