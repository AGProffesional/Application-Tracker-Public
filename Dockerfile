# Use official Python image
FROM python:3.11-slim

# Install build tools
RUN apt-get update && apt-get install -y gcc g++ build-essential

# Set working directory inside container
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the actual code
COPY . .

# Expose the port
EXPOSE 8000

# Start the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
