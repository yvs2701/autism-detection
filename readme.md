# Autism-detection

## Introduction

## Installation

Make sure you have docker installed on your system and run the following command to build the docker image:
```
docker build -t autism:0.1 .
```

## Usage

To run the docker image, run the following command:
```
docker run -it -p 8888:8888 autism:0.1
```
This will run the main.py python file which will train the model and save it upon user input. The Keras model will be saved as a folder in `./ASD_model/`.

The saved model can be copied from the docker container to the host machine by running the following command:
```
docker cp <containerId>:/ASD_model ./ASD_model
```
