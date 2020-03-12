
# Load dependencies
from matplotlib import pyplot
from keras.models import Sequential
from keras.layers import Dense
import numpy as np

# Load data
dataset = np.loadtxt('./MLP.csv', delimiter=',', skiprows=1)

# Shuffle dataset
np.random.shuffle(dataset)

dataset.shape

# Separate features and targets
X = dataset[:, 0:338]
Y = dataset[:, 338]

# Set the input shape
input_shape = (338,)
print(f'Feature shape: {input_shape}')

print(X.shape)
print (Y.shape)

# Create the model
model = Sequential()
model.add(Dense(120, input_shape=input_shape, activation='relu'))
model.add(Dense(60, activation='relu'))
model.add(Dense(1, activation='linear'))

# Configure the model and start training
model.compile(loss='mean_absolute_error', optimizer='adam', metrics=['mean_absolute_error'])
history=model.fit(X, Y, epochs=20, batch_size=1, verbose=1, validation_split=0.2)
model.save("model_MLP.h5")
print("Saved model to disk")

pyplot.plot(history.history['loss'], label='train')
pyplot.plot(history.history['val_loss'], label='test')
pyplot.legend()
pyplot.show()