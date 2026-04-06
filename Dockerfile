# WHY: Every Dockerfile starts with FROM
# This sets the base image — the foundation we build on top of
# python:3.11-slim is an official Python image, slim = smaller size
FROM python:3.11-slim

# WHY: Sets the working directory inside the container
# All following commands run from this location
# Like doing 'cd /app' inside the container
WORKDIR /app

# WHY: Copy requirements file into container first
# We copy this BEFORE copying app code — explained below
COPY requirements.txt .

# WHY: Install Python dependencies inside the container
# This runs pip install inside the container, not on your machine
RUN pip install -r requirements.txt

# WHY: Now copy the actual application code
# Done AFTER installing dependencies for build speed reasons
COPY app.py .

# WHY: Tell Docker which port this app uses
# This is documentation — doesn't actually open the port
EXPOSE 5000

# WHY: The command that runs when container starts
# This starts the Flask application
CMD ["python", "app.py"]
