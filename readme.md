# Autism-detection

Group Members:
- Yashvardhan Singh (20BAI10135)
- Siddharth Maratha (20BAI10257)
- Priyaranjan Mishra (20BCE10121)
- Suryakant Patwardhan (20BCE10783)

## Installation

Get inside the `src` folder by running the following command:
```bash
cd src
```

Make sure you have docker installed on your system and run the following command to build the docker image:
```bash
docker image build -t aut-classifier:1.0 .
```

Alternatively you can install the required packages on your system from the requirements.txt file.

## Usage

To run the docker image, run the following command:
```bash
docker run -it -p 8501:8501 --name autism-screening aut-classifier:1.0
```
This will run the train.py python file which will train the model and save it upon user input. The Keras model will be saved as a folder in `./classifier/`.
Then main.py file will run which will open the streamlit app on port 8501. The app can be accessed by going to `http://localhost:8501/` in your browser.

The saved model can be copied from the docker container to the host machine by running the following command:
```bash
docker cp <containerId>:/classifier ./classifier
```

If you had downloaded the required packages on your system manually, you can train the model by running the following command:
```bash
python3 train.py
```
Then, you can run the main.py file directly by running the following command:
```bash
python3 main.py
```
