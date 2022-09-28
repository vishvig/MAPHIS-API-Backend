# Building backend on top of Python 3.8 base image
FROM python:3.8

# Running OS updates and installing OpenCV system dependencies
RUN apt-get update && apt-get install -y python3-opencv

# Adding a non-root user
RUN useradd -ms /bin/bash maphis

# Creating a working directory for the application
RUN mkdir -p /opt/code

# Giving permissions of working directory to non-root user
# RUN chown maphis /opt/code

# Assuming non-root user permissions
# USER maphis

# Switching the working directory to the created one from the previous step
WORKDIR /opt/code

# Creating an empty directory called assets which will be n EFS mounted volume
RUN mkdir -p assets

# Copying all the contents of the codebase
COPY . .

# Installing code's python dependencies
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python", "main.py"]
