FROM python:3.11-slim

LABEL Maintainer="yvs2701"

#Any working directory can be chosen as per choice like '/' or '/home' etc
WORKDIR /home/app/src

#RUN instruction is used to execute any command during the build process of the docker image
RUN pip3 install numpy scipy matplotlib pandas scikit-learn keras
RUN pip3 install streamlit streamlit-option-menu
RUN pip3 install tensorflow

#COPY instruction is used to copy files from host machine to the container
COPY requirements.txt ./
COPY Autism_Data.csv ./
COPY train.py ./
COPY main.py ./

RUN ["python3", "./train.py"]

#CMD instruction should be used to run the software
CMD ["python", "./main.py"]