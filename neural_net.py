# Create first network with Keras
from keras.models import Sequential
from keras.layers import Dense
import numpy
#import tensorflow as tf
import tensorflow

seed = 5000
numpy.random.seed(seed)

# load Training500 dataset
dataset = numpy.loadtxt("Training500.csv", delimiter=",", skiprows=1, ndmin=2)

# split into input (X) and output (Y) variables
X = dataset[:, 0:17]
Y = dataset[:, 17]

# create model
model = Sequential()
model.add(Dense(12, input_dim=17, kernel_initializer='uniform', activation='relu'))
model.add(Dense(8, kernel_initializer='uniform', activation='relu'))
model.add(Dense(1, kernel_initializer='uniform', activation='sigmoid'))

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(X, Y, epochs=10, batch_size=50)
# evaluate the model
scores = model.evaluate(X, Y)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))

# calculate predictions
dataset = numpy.loadtxt("scores.csv", delimiter=",", ndmin=2)
Z = dataset[:, 0:17]


predictions = model.predict(Z)
print(predictions)

# round predictions
rounded = [round(x[0]) for x in predictions]
print(rounded)

'''
def neural():
    seed = 5000
    numpy.random.seed(seed)

    # load Training500 dataset
    dataset = numpy.loadtxt("Training500.csv", delimiter=",", skiprows=1, ndmin=2)

    # split into input (X) and output (Y) variables
    X = dataset[:, 0:17]
    Y = dataset[:, 17]

    # create model
    model = Sequential()
    model.add(Dense(12, input_dim=17, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(8, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(1, kernel_initializer='uniform', activation='sigmoid'))

    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Fit the model
    model.fit(X, Y, epochs=10, batch_size=50)
    # evaluate the model
    scores = model.evaluate(X, Y)
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))

    # calculate predictions
    dataset = numpy.loadtxt("scores.csv", delimiter=",", ndmin=2)
    Z = dataset[:, 0:17]
    predictions = model.predict(Z)
    print(predictions)

    # round predictions
    rounded = [round(x[0]) for x in predictions]
    print(rounded)

    return predictions,rounded


#x,y = neural()
#print(x)
#print(y)
'''



























