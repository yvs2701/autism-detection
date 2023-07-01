FROM python:3.11-slim

LABEL Maintainer="yvs2701"

WORKDIR /home/app/src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY Autism_Data.csv train.py main.py ./

CMD ["sh", "-c", "if [ ! -e \"./classifier\" ]; then \
    python3 ./train.py ; \
fi; \
streamlit run ./main.py"]

#Expose the port on which the streamlit app will run
EXPOSE 8501