FROM python:3.11-slim

LABEL Maintainer="yvs2701"

#Any working directory can be chosen as per choice like '/' or '/home' etc
WORKDIR /home/app/src

#COPY instruction is used to copy files from host machine to the container
COPY requirements.txt Autism_Data.csv train.py main.py ./

#RUN instruction is used to execute any command during the build process of the docker image
RUN pip install --no-cache-dir -r requirements.txt

#Expose the port on which the streamlit app will run
EXPOSE 8501

CMD ["sh", "-c", "python3 ./train.py && streamlit run ./main.py"]