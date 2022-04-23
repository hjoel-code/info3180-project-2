release: flask db migrate --directory migrations
web: gunicorn -w 4 -b "0.0.0.0:$PORT" app:app