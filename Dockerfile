# Use the official Python image as base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .

# Install dependencies using pip
RUN pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port on which your application runs
EXPOSE 5000

# Command to run your application
CMD ["python", "app.py"]
