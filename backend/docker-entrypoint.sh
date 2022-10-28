#!/bin/bash
# Collect static files
# echo "Collect static files"
# python manage.py collectstatic --noinput


#Flush database
echo "Flushing database"
python manage.py flush --no-input

# Plan database migrations
echo "Plan database migrations"
python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Generate test data
echo "Generate test data"
python manage.py setup_test_data

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000

