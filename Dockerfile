# Step 1: Use an official Python runtime as a parent image
FROM python:3.9-slim

RUN pip install gunicorn
# Step 2: Set the working directory in the container
WORKDIR /usr/src/app

# Step 3: Copy the current directory contents into the container at /usr/src/app
COPY . .

# Step 4: Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_ENV production

# Step 5: Make port 5000 available to the world outside this container
EXPOSE 5000

# Step 7: Run app.py when the container launches
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

