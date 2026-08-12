FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1

WORKDIR /app

# Install system deps and Python requirements
RUN apt-get update && apt-get install -y --no-install-recommends \
	build-essential \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . /app

EXPOSE 5000

# Use gunicorn as the production server; module points to `src.app:app`
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "src.app:app"]

