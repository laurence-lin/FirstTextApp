# Use a Python base image
FROM python:3.10

RUN apt-get update \
    && apt-get install -y gcc \
    && apt-get clean

RUN mkdir /app
COPY . /app
WORKDIR /app

# Install dependencies
RUN /usr/local/bin/python -m pip install --no-cache-dir -r requirements.txt

# Run migrations (important!)
RUN /usr/local/bin/python manage.py makemigrations
RUN /usr/local/bin/python manage.py migrate

# Expose the port your Django app will listen on
EXPOSE 8000

# Start Gunicorn (production-ready WSGI server)
#CMD ["gunicorn", "--bind=0.0.0.0:8000", "my_django_project.wsgi"] # Replace with your WSGI path
ENTRYPOINT ["/usr/local/bin/python", "/app/manage.py", "runserver"]