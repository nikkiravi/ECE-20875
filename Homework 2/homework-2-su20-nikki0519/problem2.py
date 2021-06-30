import numpy as np
import matplotlib.pyplot as plt


def norm_histogram(hist):
    """
    takes a histogram of counts and creates a histogram of probabilities

    :param hist: list
    :return: list
    """

    norm_hist = [(i/sum(hist)) for i in hist]
    return(norm_hist)

    pass


def computeJ(histo, width):
    """
    takes histogram of counts, uses norm_histogram to convert to probabilties, then calculates computeJ for one bin width

    :param histo: list 
    :param width: float
    :return: float
    """

    norm_hist = norm_histogram(histo)

    sum_prob = sum(map(lambda i: i**2, norm_hist))

    J = (2 / (((sum(histo) - 1) * width))) - (((sum(histo) + 1) / ((sum(histo) - 1) * width)) * sum_prob)

    return(J)

    pass


def sweepN (data, minimum, maximum, min_bins, max_bins):
    """
    find the optimal bin
    calculate computeJ for a full sweep [min_bins to max_bins]

    :param data: list
    :param minimum: int
    :param maximum: int
    :param min_bins: int
    :param max_bins: int
    :return: list
    """

    optimal_bin_width = []
    for i in range(min_bins, max_bins + 1, 1):
    	(n, bins, patch) = plt.hist(data, i)
    	bin_width = bins[1] - bins[0]

    	optimal_bin_width.append(computeJ(n, bin_width))


    return(optimal_bin_width)


    pass


def findMin (l):
    """
    generic function that takes a list of numbers and returns smallest number in that list its index.
    return optimal value and the index of the optimal value as a tuple.

    :param l: list
    :return: tuple
    """

    min_width = (min(l), l.index(min(l)))

    return(min_width)

    pass


if __name__ == '__main__':
    data = np.loadtxt('input.txt')  # reads data from inp.txt
    lo = min(data)
    hi = max(data)
    bin_l=1
    bin_h=100
    js = sweepN(data, lo, hi, bin_l,bin_h)

    # the values bin_l and bin_h represent the lower and higher bound of the range of bins.
    # They will change when we test your code and you should be mindful of that.
    
    print(findMin(js))

    # Include code here to plot js vs. the bin range
	