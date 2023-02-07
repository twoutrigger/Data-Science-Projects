# specify base image
FROM python:3.8

# specify the container's working directory
WORKDIR /code

# copy dependencies from requirements
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy contents to the working directory
COPY . .

# command to run on container start
CMD [ "python", "./app.py" ]