# Use an official Python runtime as a base image
FROM python:3.8


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Set the working directory in the container
WORKDIR /usr/src/app


# Copy the requirements file into the container at /usr/src/app
COPY requirements.txt .

RUN python -m venv venv
RUN /usr/src/app/venv/bin/pip install --no-cache-dir --upgrade pip
RUN /usr/src/app/venv/bin/pip install --no-cache-dir django-phonenumber-field[phonenumbers]
RUN /usr/src/app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Copy the current directory contents into the container at /usr/src/app
COPY src/ .


# Expose the port that Django will run on
EXPOSE 8000


# Define the command to run your application
CMD ["/usr/src/app/venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]