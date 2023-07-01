# Autism-detection

Group Members:
- Yashvardhan Singh (20BAI10135)
- Siddharth Maratha (20BAI10257)
- Priyaranjan Mishra (20BCE10121)
- Suryakant Patwardhan (20BCE10783)

### Data Dictionary 

| Column   | Atrribute Name  	| Definition                                                                                                                                          | Data Type    |
|----------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| 1        | A1_Score        	| Question 1 Answer: Binary (0, 1)                                                                                                                    | Quantitative |
| 2        | A2_Score        	| Question 2 Answer: Binary (0, 1)                                                                                                                    | Quantitative |
| 3        | A3_Score        	| Question 3 Answer: Binary (0, 1)                                                                                                                    | Quantitative |
| 4        | A4_Score        	| Question 4 Answer: Binary (0, 1)                                                                                                                    | Quantitative |
| 5        | A5_Score        	| Question 5 Answer: Binary (0, 1)                                                                                                                    | Quantitative |
| 6        | A6_Score        	| Question 6 Answer: Binary (0, 1)                                                                                                                    | Quantitative |
| 7        | A7_Score        	| Question 7 Answer: Binary (0, 1)                                                                                                                    | Quantitative |
| 8        | A8_Score        	| Question 8 Answer: Binary (0, 1)                                                                                                                    | Quantitative |
| 9        | A9_Score        	| Question 9 Answer: Binary (0, 1)                                                                                                                    | Quantitative |
| 10       | A10_Score       	| Question 10 Answer: Binary (0,   1)                                                                                                                 | Quantitative |
| 11       | Age             	| Age in years                                                                                                                                        | Quantitative |
| 12       | Gender          	| Gender (m: Male, f: Female)                                                                                                                         | Qualitative  |
| 13       | Ethnicity       	| List of common ethnicities   (White-European, Latino, Others, Black, Asian, Middle Eastern, Pasifika,   South Asian, Hispanic, Turkish)             | Qualitative  |
| 14       | Jundice         	| Whether the case was born with   Jundice (Yes, No)                                                                                                  | Qualitative  |
| 15       | Austim          	| Whether any immediate family   member has a PDD (Yes, No)                                                                                           | Qualitative  |
| 16       | Country_of_res  	| Country of residence (List of   countries)                                                                                                          | Qualitative  |
| 17       | Used_app_before 	| Whether the user has used the   screening app before (Yes, No)                                                                                      | Qualitative  |
| 18       | Result          	| Screening score: The final score   obtained based on the scoring algorithm of the screening method used. This   was computed in an automated manner | Quantitative |
| 19       | Age_desc        	| Age description                                                                                                                                     | Qualitative  |
| 20       | Relation        	| Who is completing the test   (Self, Parent, Health care professional, Relative, etc)                                                                | Qualitative  |
| 21       | Class/ASD       	| yes, no                                                                                                                                             | Qualitative  |


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

## Video Link - 
https://drive.google.com/file/d/1eyaDznEfEg0ffFC8R2SS6nHikzOfZGOL/view?usp=sharing
