# Use the official Python image as base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .

# Install pipenv
RUN pip install pipenv

# Install dependencies using pipenv
RUN pipenv install --system --deploy

# Copy the rest of the application code to the container
COPY . .

# Expose the port on which your Flask app will run
EXPOSE 5000

# Command to run your Flask application
CMD ["python", "app.py"]
