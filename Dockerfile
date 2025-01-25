# rename dockerfile to Dockerfile
# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Создаем директорию
RUN mkdir -p /var/autoBot
# Устанавливаем права на запись
RUN chmod 777 /var/autoBot
# Set the working directory in the container

WORKDIR /service-bot

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8080

# Run the application
CMD ["python", "bot/main.py"]
