import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

df = pd.read_csv("Autism_Data.csv")

df.replace("?", np.nan, inplace=True)
df["age"] = df["age"].astype(float)
df["age"] = df["age"].fillna(np.round(df["age"].mean(), 0))
df["age"] = df["age"].astype(int)

df["ethnicity"] = df["ethnicity"].replace("?", "Others")
df["ethnicity"] = df["ethnicity"].replace("others", "Others")
df["relation"] = df["relation"].replace("?", df["relation"].mode()[0])

df.drop(["age_desc", "contry_of_res"], axis=1, inplace=True)

X = df.drop("Class/ASD", axis=1)
Y = df["Class/ASD"]

X = pd.get_dummies(X)
Y = pd.get_dummies(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25)

input_dim = X.shape[1]
model = Sequential()
model.add(Dense(8, input_dim=input_dim, kernel_initializer="normal", activation="relu"))
model.add(Dense(5, activation="relu", kernel_initializer="normal"))
model.add(Dense(2, activation="sigmoid"))

# compiling model
model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss="binary_crossentropy",
    metrics=["accuracy"],
)

result = model.fit(
    np.asarray(X_train).astype("float32"),
    np.asarray(Y_train).astype("float32"),
    epochs=20,
    batch_size=10,
)

acc = result.history["accuracy"]
loss = result.history["loss"]

epoch = [i + 1 for i in range(len(acc))]

loss, acc = model.evaluate(
    np.asarray(X_test).astype("float32"), np.asarray(Y_test).astype("float32")
)
print(f"Accuracy on unseen data is: { np.round(acc, 2) }")
print(f"Loss on unseen data is: { np.round(loss, 2) }")

prediction = model.predict(np.asarray(X_test).astype("float32"))
prediction = np.argmax(prediction, axis=1)

print(accuracy_score(Y_test[["YES"]], prediction))
print(classification_report(Y_test[["YES"]], prediction))

# save the model
model.save("classifier", save_format="h5")
