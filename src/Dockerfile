# pull official base image
FROM python:3.11-slim-buster




# set working directory
WORKDIR /usr/src

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat-traditional gcc postgresql \
  && apt-get install --yes libxml2-dev libxslt-dev  \
  && apt-get install --yes libpq-dev \
  && apt-get clean

# install python dependencies

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .
