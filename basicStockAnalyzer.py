import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout


def cleanData(dataset, parameter):
    dataset["Volume"] = dataset["Volume"].astype(float)
    dataset = dataset.drop(columns="OpenInt")
    dataset = dataset[12000:]
    return pd.DataFrame(dataset[parameter])

def featureScale(input, start, end):
    sc = MinMaxScaler(feature_range = (0, 1))
    return sc, sc.fit_transform(training_set)

def buildTimeSteps(dataset, timesteps):

    X_train = []
    y_train = []
    for i in range(timesteps, dataset.shape[0]):
        X_train.append(dataset[i-timesteps:i, 0])
        y_train.append(dataset[i, 0])

    return np.array(X_train), np.array(y_train)

def buildModel(input_shape):

    lstm_model = Sequential()

    #Make stateful later
    lstm_model.add(LSTM(units=50, input_shape = input_shape, return_sequences = True, kernel_initializer='random_uniform'))
    lstm_model.add(Dropout(0.2))
    lstm_model.add(LSTM(units = 50, return_sequences = True))
    lstm_model.add(Dropout(0.2))
    lstm_model.add(LSTM(units = 50))
    lstm_model.add(Dropout(0.2))
    lstm_model.add(Dense(20,activation='relu'))
    lstm_model.add(Dense(1,activation='sigmoid'))

    return lstm_model

def displayPlots(real_stock_price, predicted_stock_price):
    plt.plot(real_stock_price, color = 'red', label = 'Real GE Stock Price')
    plt.plot(predicted_stock_price, color = 'blue', label = 'Predicted GE Stock Price')
    plt.title('GE Stock Price Prediction')
    plt.xlabel('Time')
    plt.ylabel('GE Stock Price')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    '''
    Get the data and shape it
    '''
    dataset = pd.read_csv('SourceData/Stocks/ge.us.txt', index_col="Date", parse_dates=True)
    training_set=cleanData(dataset, parameter='Open')
    sc, training_set_scaled = featureScale(input=training_set, start=0, end=1)
    X_train, y_train = buildTimeSteps(training_set_scaled, timesteps=60)
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

    '''
    Build and compile model
    '''
    model=buildModel(input_shape=(X_train.shape[1], 1))
    model.compile(optimizer = 'adam', loss = 'mean_squared_error')
    model.fit(X_train, y_train, epochs = 100, batch_size = 32)


    '''
    Get test data
    '''
    dataset_test = pd.read_csv('SourceData/Stocks/ge.us.test.csv',index_col="Date",parse_dates=True)
    real_stock_price = dataset_test.iloc[:, 0:1].values
    test_set=dataset_test['Open']
    test_set=pd.DataFrame(test_set)

    '''
    Transform data for predictions
    '''

    dataset_total = pd.concat((dataset['Open'], dataset_test['Open']), axis = 0)
    inputs = dataset_total[len(dataset_total) - len(dataset_test) - 60:].values
    inputs = inputs.reshape(-1,1)
    inputs = sc.transform(inputs)
    X_test = []
    for i in range(60, test_set.shape[0]):
        X_test.append(inputs[i-60:i, 0])
    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    predicted_stock_price = model.predict(X_test)
    predicted_stock_price = sc.inverse_transform(predicted_stock_price)

    predicted_stock_price=pd.DataFrame(predicted_stock_price)

    '''
    Plots and visualization
    '''
    displayPlots(real_stock_price, predicted_stock_price)
