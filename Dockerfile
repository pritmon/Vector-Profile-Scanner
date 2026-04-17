FROM python:3.9-slim

# Set environment variables for better performance
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Set working directory
WORKDIR /app

# Install system dependencies and create a non-root user for security
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && useradd -m -r appuser \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install dependencies first for caching purposes
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .
RUN pip install -e .

# Create models directory and set permissions for appuser
RUN mkdir -p /app/models && chown -m 755 -R appuser:appuser /app

# Switch to the non-root user
USER appuser

# Train the model so the container has the model artifacts built-in
RUN PYTHONPATH=. python -m src.train

# Expose the API port
EXPOSE 8000

# Start the FastAPI server using Uvicorn
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]

