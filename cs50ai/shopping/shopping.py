import csv
import sys
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    # Importing the dataset
    dataset = pd.read_csv('shopping.csv')
    X = dataset.iloc[:, 0:17].values
    Y = dataset.iloc[:, 17].values

    # Encoding categorical data
    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    from sklearn.compose import ColumnTransformer
    
    le = LabelEncoder()
    X[:, 10] = le.fit_transform(X[:, 10])
    X[:, 15] = le.fit_transform(X[:, 15])
    X[:, 16] = le.fit_transform(X[:, 16])
    Y = le.fit_transform(Y)

    return (X.tolist(), Y.tolist())
    
    

    

def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier()
    return model.fit(evidence, labels)
    

def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificty).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    # Vairbles to compute accuracy
    sensitvity_correct = 0 # True
    total1 = 0
    specificity_correct = 0 # False
    total2 = 0

    for label, prediction in zip(labels, predictions):
        if (label == prediction) and (prediction == 1):
            sensitvity_correct += 1
            total1 += 1
        elif (label != prediction) and (prediction == 1):
            total1 += 1
        elif (label == prediction) and (prediction == 0):
            specificity_correct += 1
            total2 += 1
        else:
            total2 += 1
            
    return (sensitvity_correct / total1, specificity_correct / total2)

def better_train_model(X_train, Y_train, X_test):
    
    # Importing the Keras libraries and packages
    #import keras
    #from keras.models import Sequential
    #from keras.layers import Dense, Dropout
    
    # Initialising the ANN
    model = Sequential()
    
    # Adding the input layer and the first hidden layer
    model.add(Dense(units = 10, kernel_initializer = 'uniform', activation = 'relu', input_dim = 17))
    
    # Adding the second hidden layer
    model.add(Dense(units = 5, kernel_initializer = 'uniform', activation = 'relu'))

    # Adding the output layer
    model.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))
    
    # Compiling the ANN
    model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

    # Fitting the ANN to the Training set
    model.fit(X_train, Y_train, batch_size = 32, epochs = 15)

    #Predicting the Test set results
    Y_pred = model.predict(X_test)
    
    return (Y_pred > .5)

     
if __name__ == "__main__":
    main()
