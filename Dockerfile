# Use official Python image
FROM python:3.11

# Set working directory inside container
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements-dev.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements-dev.txt

# Copy the actual code
COPY . .

# Expose the port
EXPOSE 8000

# Start the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
