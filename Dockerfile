FROM python:3.6-stretch

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run app.py when the container launches
CMD ["python", "index.py"]