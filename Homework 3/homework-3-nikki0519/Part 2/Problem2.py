from scipy import stats
import numpy as np
import math

def confidence_interval(data, confidence):
	t_score = stats.t.ppf(1 - (1 - confidence) / 2, len(data) - 1)
	mean = np.mean(data)
	SE = np.std(data, ddof = 1) / math.sqrt(len(data))
	offset = SE * t_score

	return(mean - offset, mean + offset)

def questionOne(data, confidence):
	print("For this sample of data a t-test is required as it has less than 30 datapoints")

	sample_mean = float(np.mean(data))
	std = np.std(data, ddof = 1)
	SE = std / math.sqrt(len(data))

	print("Sample Mean is ", str(sample_mean))
	print("Standard Deviation is ", str(std))
	print("Standard Error is ", str(SE))

	#t_score = stats.t.ppf(confidence, df = len(data) - 1)

	interval = list(confidence_interval(data, confidence))

	print("95% Confidence interval: (", str(interval[0]), ", ", str(interval[1]), ")")


def questionTwo(data, confidence):
	t_score = stats.t.ppf(0.95, df = len(data) - 1)

	interval = list(confidence_interval(data, confidence))

	print("90% Confidence interval: (", str(interval[0]), ", ", str(interval[1]), ")") 
	print("The t_score and interval decreased because the confidence decreased by 5%")

def questionThree(data, pop_std):
	print("A standard distribution is used because the population standard deviation is given")

	mean = np.mean(data)
	SE = pop_std / math.sqrt(len(data))
	print("Standard Error is ", str(SE))

	z_score = stats.norm.ppf(0.975)
	confidenceInterval = (mean - z_score * SE, mean + z_score * SE)
	print("Confidence interval: (", str(confidenceInterval[0]), ", ", str(confidenceInterval[1]), ")") 

def questionFour(data):
	t_score = np.mean(data) / ((np.std(data, ddof=1) / math.sqrt(len(data))))
	confidence = 1 - (2 * stats.t.cdf(-abs(t_score), df=len(data)-1))

	print('Confidence Level is ', str(confidence))
	print('Confidence Interval is ' + str([0, np.mean(data) + (t_score * (np.std(data, ddof=1) / math.sqrt(len(data))))]))
	print('The confidence level is 0.82 so we are 82 percent confident that the team will win over average')


if(__name__ == '__main__'):
	data = [3, -3, 3, 12, 15, -16, 17, 19, 23, -24, 32]

	print("Answer to Question One")
	questionOne(data, 0.95)
	print("--------------------------------------------------")

	print("Answer to Question Two")
	questionTwo(data, 0.9)	
	print("--------------------------------------------------")


	print("Answer to Question Three")
	questionThree(data, 16.836)
	print("--------------------------------------------------")

	print("Answer to Question Four")
	questionFour(data)
	print("--------------------------------------------------")
