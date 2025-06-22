FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \ 
    gcc \
    g++\
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src
COPY README.md .

# Create necessary directories
RUN mkdir -p data logs

# Set environment variables
ENV PYTHONPATH=/app/src
ENV PYTHONUNBUFFERED=1

# Default command
CMD ["python", "-m", "src.crawler", "IPO", "--days", "7", "--pages", "2"]
