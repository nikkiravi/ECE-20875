import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn import linear_model
import matplotlib.pyplot as plt


def main():
    #Importing dataset
    diamonds = pd.read_csv('diamonds.csv')

    #Feature and target matrices
    X = diamonds[['carat', 'depth', 'table', 'x', 'y', 'z', 'clarity', 'cut', 'color']]
    y = diamonds[['price']]

    #Training and testing split, with 25% of the data reserved as the test set
    X = X.to_numpy()
    y = y.to_numpy()
    [X_train, X_test, y_train, y_test] = train_test_split(X, y, test_size=0.25, random_state=101)

    #Normalizing training and testing data
    [X_train, trn_mean, trn_std] = normalize_train(X_train)
    X_test = normalize_test(X_test, trn_mean, trn_std)

    #Define the range of lambda to test
    lmbda = np.logspace(start=-1.00, stop=2.00, endpoint=True, base=10, num=101)

    MODEL = []
    MSE = []
    for l in lmbda:
        #Train the regression model using a regularization parameter of l
        model = train_model(X_train,y_train,l)

        #Evaluate the MSE on the test set
        mse = error(X_test,y_test,model)

        #Store the model and mse in lists for further processing
        MODEL.append(model)
        MSE.append(mse)

    #Plot the MSE as a function of lmbda
    plt.plot(lmbda, MSE, 'k-', label='True')#fill in
    plt.xlabel('Lambda')
    plt.ylabel('Mean Squared Error')
    plt.title('MSE vs. Lambda')
    plt.show()

    #Find best value of lmbda in terms of MSE
    ind = MSE.index(min(MSE))
    [lmda_best,MSE_best,model_best] = [lmbda[ind],MSE[ind],MODEL[ind]]

    print('Best lambda tested is ' + str(lmda_best) + ', which yields an MSE of ' + str(MSE_best))

    tmp_list = [0.25, 60, 55, 4, 3, 2, 5, 3, 3]
    new_list = []

    price = 0
    for i in range(len(tmp_list)):
        new_list.append((tmp_list[i] - trn_mean[i]) / trn_std[i])

    coeff = model_best.coef_

    for i in range(len(new_list)):
        price += coeff[0, i] * new_list[i]

    price += model_best.intercept_[0]

    print("The predicted price is %d" % price)

    return model_best


#Function that normalizes features in training set to zero mean and unit variance.
#Input: training data X_train
#Output: the normalized version of the feature matrix: X, the mean of each column in
#training set: trn_mean, the std dev of each column in training set: trn_std.
def normalize_train(X_train):

    #fill in
    mean = []
    std = []

    for i in range(len(X_train[0])):
        feature = X_train[:, i]
        mean.append(np.mean(feature))
        std.append(np.std(feature))

    X = []
    for item in range(len(X_train)):
        tmp = []
        for i in range(len(X_train[0])):
            tmp.append(((X_train[item, i] - mean[i]) / std[i]))
        
        X.append(tmp)

    X = np.array(X)


    return X, mean, std


#Function that normalizes testing set according to mean and std of training set
#Input: testing data: X_test, mean of each column in training set: trn_mean, standard deviation of each
#column in training set: trn_std
#Output: X, the normalized version of the feature matrix, X_test.
def normalize_test(X_test, trn_mean, trn_std):

    #fill in
    X = []
    for item in range(len(X_test)):
        tmp = []
        for i in range(len(X_test[0])):
            tmp.append(((X_test[item, i] - trn_mean[i]) / trn_std[i]))

        X.append(tmp)

    X = np.array(X)

    return X



#Function that trains a ridge regression model on the input dataset with lambda=l.
#Input: Feature matrix X, target variable vector y, regularization parameter l.
#Output: model, a numpy object containing the trained model.
def train_model(X,y,l):

    #fill in
    model = linear_model.Ridge(alpha = l, fit_intercept = True)
    model.fit(X, y)

    return model


#Function that calculates the mean squared error of the model on the input dataset.
#Input: Feature matrix X, target variable vector y, numpy model object
#Output: mse, the mean squared error
def error(X,y,model):

    #Fill in
    y_hat = model.predict(X)
    sum = 0

    for i in range(len(y)):
        sum += (y[i] - y_hat[i]) ** 2

    mse = sum / len(y)

    return mse

if(__name__ == '__main__'):
    model_best = main()
    print(model_best.coef_)
    print(model_best.intercept_)
