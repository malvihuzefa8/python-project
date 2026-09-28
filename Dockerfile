# 1. Base image: small official Python image
FROM python:3.12-slim

# 2. Working directory inside the container
WORKDIR /app

# 3. Install dependencies first (Docker caches this layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the application code
COPY app.py .

# 5. Document the port the app listens on
EXPOSE 5000

# 6. Run with gunicorn (production server) instead of Flask's dev server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
