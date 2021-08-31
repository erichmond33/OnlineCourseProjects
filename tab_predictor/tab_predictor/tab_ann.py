# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 22:12:55 2020

@author: eeric
"""



# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

# Importing the dataset
dataset = pd.read_csv('data.csv')
X = dataset.iloc[:885, 3:43].values
Y = dataset.iloc[:885, 0:1].values
X = np.delete(X, [5, 6, 17, 18, 19, 20, 21,22,23,24,25,26,27], 1)



#Take Care of Missing Data '''SimpleImputer is the updated version of Imputer'''
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'constant')
imputer.fit(X[:, 0:15])
X[:, 0:15] = imputer.transform(X[:, 0:15])

imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputer.fit(X[:, 15:28])
X[:, 15:28] = imputer.transform(X[:, 15:28])

    

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

labelencoder_X_1 = LabelEncoder()
X[:, 4] = labelencoder_X_1.fit_transform(X[:, 4])
X[:, 5] = labelencoder_X_1.fit_transform(X[:, 5])
X[:, 6] = labelencoder_X_1.fit_transform(X[:, 6])
X[:, 7] = labelencoder_X_1.fit_transform(X[:, 7])
X[:, 8] = labelencoder_X_1.fit_transform(X[:, 8])
X[:, 9] = labelencoder_X_1.fit_transform(X[:, 9])
X[:, 10] = labelencoder_X_1.fit_transform(X[:, 10])
X[:, 11] = labelencoder_X_1.fit_transform(X[:, 11])
X[:, 12] = labelencoder_X_1.fit_transform(X[:, 12])
X[:, 13] = labelencoder_X_1.fit_transform(X[:, 13])
X[:, 14] = labelencoder_X_1.fit_transform(X[:, 14])



labelencoder_Y_1 = LabelEncoder()
Y[:, 0] = labelencoder_Y_1.fit_transform(Y[:, 0])



column_transformer = ColumnTransformer(transformers = [('encode', OneHotEncoder(),[4,5,6,7,8,9,10,11,12,13,14])],remainder='passthrough')
X = column_transformer.fit_transform(X).toarray()

onehotencoder = OneHotEncoder()
#X = onehotencoder.fit_transform(X).toarray()
#X = X[:, 4:14]
Y = onehotencoder.fit_transform(Y).toarray()
Y = Y[:, 0:]



# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)


#Feature Scaling
from sklearn.preprocessing import StandardScaler
scale_X = StandardScaler()
X_train = scale_X.fit_transform(X_train)
X_test = scale_X.transform(X_test)
y_test = scale_X.fit_transform(y_test)
y_train = scale_X.transform(y_train)
#Don't need to scale Y values





# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout

# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(units = 2000, kernel_initializer = 'uniform', activation = 'relu', input_dim = 1291))
classifier.add(Dropout(.40))
# Adding the second hidden layer
classifier.add(Dense(units = 1500, kernel_initializer = 'uniform', activation = 'relu'))
classifier.add(Dropout(.40))

classifier.add(Dense(units = 1500, kernel_initializer = 'uniform', activation = 'relu'))
classifier.add(Dropout(.40))


classifier.add(Dense(units = 1000, kernel_initializer = 'uniform', activation = 'relu'))
classifier.add(Dropout(.40))

classifier.add(Dense(units = 1000, kernel_initializer = 'uniform', activation = 'relu'))
classifier.add(Dropout(.40))


classifier.add(Dense(units = 500, kernel_initializer = 'uniform', activation = 'relu'))
classifier.add(Dropout(.40))


# Adding the output layer
classifier.add(Dense(units = 154, kernel_initializer = 'uniform', activation = 'softmax'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 10, epochs = 15)

# Part 3 - Making predictions and evaluating the model

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

y_test = (y_test > .5)
X_test = (X_test > .5)



# Evaluate the model on the test data using `evaluate`
print("Evaluate on test data")
results = classifier.evaluate(X_test, y_test, batch_size=128)
print("test loss, test acc:", results)

# Generate predictions (probabilities -- the output of the last layer)
# on new data using `predict`
print("Generate predictions for 3 samples")
predictions = classifier.predict(X_test[3:6])
print("predictions shape:", predictions.shape)




# evaluate the model
	scores = classifier.evaluate(X_test, y_test, verbose=0)
	print("%s: %.2f%%" % (classifier.metrics_names[1], scores[1]*100))
    
    print(scores)
    
    
	cvscores.append(scores[1] * 100)
print("%.2f%% (+/- %.2f%%)" % (numpy.mean(cvscores), numpy.std(cvscores)))

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)



new_prediction = classifier.predict(np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]]))