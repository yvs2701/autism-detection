FROM python:3.11-slim

LABEL Maintainer="yvs2701"

#Any working directory can be chosen as per choice like '/' or '/home' etc
WORKDIR /home/app/src


RUN pip3 install numpy scipy matplotlib pandas scikit-learn keras
RUN pip3 install tensorflow

#to COPY the remote file at working directory in container
COPY main.py ./
COPY Autism_Data.csv ./
COPY requirements.txt ./

#CMD instruction should be used to run the software
#contained by your image, along with any arguments.
CMD ["python", "./main.py"]