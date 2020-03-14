
# Load dependencies
from matplotlib import pyplot
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Load data
dataset = np.loadtxt('./MLP_in336_out48.csv', delimiter=',', skiprows=1)
dataset = dataset.astype('float32')

# Shuffle dataset
np.random.shuffle(dataset)


print(dataset.shape)

# Separate features and targets
X = dataset[:, :-48]
Y = dataset[:, -48:]

# Set the input shape
input_shape = (336,)
print(f'Feature shape: {input_shape}')

print(X.shape)
print (Y.shape)

# Create the model
model = Sequential()
model.add(Dense(128, input_shape=input_shape, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(48, activation='linear'))

# Configure the model and start training
model.compile(loss='mean_absolute_error', optimizer='adam', metrics=['mean_absolute_percentage_error','mean_squared_error'])
history=model.fit(X, Y, epochs=250, batch_size=25, verbose=1, validation_split=0.2)
model.save("model_MLP_128_64_250_25.h5")
print("Saved model to disk")

pyplot.plot(history.history['loss'], label='train')
pyplot.plot(history.history['val_loss'], label='test')
pyplot.legend()
pyplot.savefig("temp_epoch_loss.png")
