# Use official lightweight Python image
FROM python:3.12-slim

# Prevent Python from writing .pyc files & enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8080

WORKDIR /app

# Install system dependencies for Pillow and SQLite
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy repository code
COPY . /app/

# Set working directory to Django project root
WORKDIR /app/AlumniManagement

# Run database migrations and collect static files
RUN python manage.py migrate --noinput
RUN python manage.py collectstatic --noinput

# Run seed data if database is fresh
RUN python seed_data.py || true

# Expose port (Cloud Run sets $PORT dynamically, default 8080)
EXPOSE 8080

# Launch Gunicorn WSGI server
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 0 AlumniManagement.wsgi:application
