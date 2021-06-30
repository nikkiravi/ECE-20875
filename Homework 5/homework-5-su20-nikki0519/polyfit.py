import numpy as np
import matplotlib.pyplot as plt

#Return fitted model parameters to the dataset at datapath for each choice in degrees.
#Input: datapath as a string specifying a .txt file, degrees as a list of positive integers.
#Output: paramFits, a list with the same length as degrees, where paramFits[i] is the list of
#coefficients when fitting a polynomial of d = degrees[i].
def main(datapath, degrees):
    paramFits = []

    #fill in
    #read the input file, assuming it has two columns, where each row is of the form [x y] as
    #in poly.txt.
    #iterate through each n in degrees, calling the feature_matrix and least_squares functions to solve
    #for the model parameters in each case. Append the result to paramFits each time.

    file = open(datapath, "r")
    x_value = []
    y_value = []

    for i in file:
        [x_val, y_val] = i.split()
        x_value.append(float(x_val))
        y_value.append(float(y_val))

    file.close()

    plt.plot(x_value, y_value, 'kx', label = 'The Data')

    for n in degrees:
        paramFits.append(list(least_squares(feature_matrix(x_value, n), y_value)))


    x_value.sort()
    y_dict = {}

    for i in range(len(paramFits)):
        for j in x_value:
            y_dict.setdefault(str(i), []).append(get_equation(paramFits[i], degrees[i], j))


    colors = ['b-', 'g-', 'c-', 'm-', 'y-', 'r-']

    for key, val in y_dict.items():
        plt.plot(x_value, val, colors[int(key)], label = 'Polynomial Degree: %d' % degrees[int(key)])


    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("Prediction Model")
    plt.show()

    return paramFits

def get_equation(coeff, degree, x):
    value = 0
    idx = 0

    for n in range(degree, -1, -1):
        value += coeff[idx] * (x ** n)
        idx += 1

    return value

#Return the feature matrix for fitting a polynomial of degree d based on the explanatory variable
#samples in x.
#Input: x as a list of the independent variable samples, and d as an integer.
#Output: X, a list of features for each sample, where X[i][j] corresponds to the jth coefficient
#for the ith sample. Viewed as a matrix, X should have dimension #samples by d+1.
def feature_matrix(x, d):

    #fill in
    #There are several ways to write this function. The most efficient would be a nested list comprehension
    #which for each sample in x calculates x^d, x^(d-1), ..., x^0.

    X = [[float(x[j] ** i) for i in range(d, -1, -1)] for j in range(len(x))]

    return X


#Return the least squares solution based on the feature matrix X and corresponding target variable samples in y.
#Input: X as a list of features for each sample, and y as a list of target variable samples.
#Output: B, a list of the fitted model parameters based on the least squares solution.
def least_squares(X, y):
    X = np.array(X)
    y = np.array(y)

    #fill in
    #Use the matrix algebra functions in numpy to solve the least squares equations. This can be done in just one line.
    B = np.dot(np.linalg.inv(np.dot(np.transpose(X), X)), np.dot(np.transpose(X), y))


    return B


if __name__ == '__main__':
    datapath = 'poly.txt'
    degrees = [1, 2, 3, 4, 5]

    paramFits = main(datapath, degrees)
    print(paramFits)
