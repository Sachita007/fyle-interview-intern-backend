# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=core/server.py

RUN rm core/store.sqlite3
RUN flask db upgrade -d core/migrations/

RUN pytest -vvv -s tests/

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable




# # Run the command to start the server
# CMD ["bash run.sh"]
