#!/bin/bash
# Collect static files
# echo "Collect static files"
# python manage.py collectstatic --noinput




sleep 5

# paranoia
su root

#uncomment when starting to clear DB and run migrations on launch
echo "Clearing database and migrations"
python manage.py reset_db --no-input


echo "Revert all database migrations"
python manage.py migrate api zero

# Plan database migrations
echo "Plan database migrations"
python manage.py makemigrations api

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# TODOS: Need to install dependencies to make this work, might not have it be in docker container
# #generate graph of models
# echo "Generating model graph"
# python manage.py graph_models -a -o ./api_models.png

# Generate test data
echo "Generate test data"
python manage.py setup_test_data

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000

