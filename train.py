"""
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1dpOEfF3zcGJl2wJd243o4TQKpFPsC_t5

### Childhood Autistic Spectrum Disorder Screening using Machine Learning

The early diagnosis of neurodevelopment disorders can improve treatment and significantly decrease the associated
healthcare costs. In this project, we will use supervised learning to diagnose Autistic Spectrum Disorder
(ASD) based on behavioural features and individual characteristics. More specifically, we will build and deploy a neural network using the Keras API. \
This project will use a dataset provided by the SmartBridge. The dataset is saved at: [GDrive link](https://drive.google.com/file/d/1MbSfEStcGwMkqSz8Md3HUHUPilJ4RA3Z/view?usp=sharing)
"""

import sys
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split

# import the dataset
file = "Autism_Data.csv"

# read the csv
data = pd.read_csv(file, sep=",", index_col=None)

# drop unwanted columns
data = data.drop(["result", "age_desc"], axis=1)

# create X and Y datasets for training
data.rename(columns={"Class/ASD": "Class"}, inplace=True)
x = data.drop(columns=["Class"])
y = data["Class"]

# convert the data to categorical values - one-hot-encoded vectors
X = pd.get_dummies(x)

# convert the class data to categorical values - one-hot-encoded vectors
Y = pd.get_dummies(y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

# define a function to build the keras model
def create_model():
    # create model
    model = Sequential()
    model.add(Dense(8, input_dim=150, kernel_initializer="normal", activation="relu"))
    model.add(Dense(4, kernel_initializer="normal", activation="relu"))
    model.add(Dense(2, activation="sigmoid"))

    # compile model
    adam = Adam(learning_rate=0.001)
    model.compile(loss="categorical_crossentropy", optimizer=adam, metrics=["accuracy"])
    return model


model = create_model()


# fit the model to the training data
model.fit(
    np.asarray(X_train).astype("float32"),
    np.asarray(Y_train).astype("float32"),
    epochs=50,
    batch_size=10,
    verbose=1,
)

predictions = model.predict(np.asarray(X_test).astype("float32"))

print("Results for Categorical Model")
print(
    model.evaluate(
        np.asarray(X_test).astype("float32"), np.asarray(Y_test).astype("float32")
    )
)

model.save("classifier", overwrite=True, save_format="h5")
print("Model saved successfully!")

# save the model by taking user input
# save = input("Do you want to save the model? (y/n): ")
# if save == "y":
#     model.save("ASD_model", overwrite=True, save_format="keras")
#     print("Model saved successfully!")
# else:
#     print("Model was not saved!")
#     sys.exit()
