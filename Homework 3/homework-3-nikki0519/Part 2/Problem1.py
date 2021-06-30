from scipy import stats
import numpy as np
import math

def readFile(filename):
	file = open(filename, 'r')
	data = file.readlines()
	file.close()

	return([float(i) for i in data])

def questionOne():
	print("Null Hypothesis: Mean Engagement of the Students who become knowledgeable in the course is 0.75")
	print("Alternate Hypothesis: Mean Engagement of the Students who become knowledgeable in the course is not 0.75")
	print("The type of test that can be used is the z-test as we have more than 30 datapoints in our sample based on the rule of thumb")

def questionTwo(data, pop_mean):
	std = np.std(data, ddof = 1)
	print("Standard Deviation of Sample is ", str(std))

	print("The Sample size is ", str(len(data)))
	print("The Sample mean is ", str(np.mean(data)))

	SE = std / math.sqrt(len(data))
	print("Standard Error of Sample is ", str(SE))
	
	z_score = (np.mean(data) - pop_mean) / SE
	print("The Sample mean is ", str(np.mean(data)))
	print("z-score of Sample is ", str(z_score))

	p_value = 2 * stats.norm.cdf(-abs(z_score))
	print("p-value of Sample is ", str(p_value))

	if(p_value < 0.1 and p_value > 0.05):
		print("The result is significant at an alpha value of 0.1. Therefore we can reject the Null Hypothesis and the average is not 0.75")
	elif(p_value > 0.01 and p_value < 0.05):
		print("The result is significant at an alpha value of 0.01. Therefore we can reject the Null Hypothesis and the average is not 0.75")
	elif(p_value > 0.05 and p_value < 0.1):
		print("The result is significant at an alpha value of 0.05. Therefore we can reject the Null Hypothesis and the average is not 0.75")
	else:
		print("The alternate hypothesis can be rejected")


def questionThree(data, alpha, pop_mean):
	z_c = stats.norm.ppf(alpha / 2)
	print("z-score of sample where 0.05 is significant is ", str(z_c))
	std = np.std(data, ddof = 1)
	print("Standard Deviation of sample is ", str(std))

	SE = (np.mean(data) - pop_mean) / z_c
	print("Standard Error of sample is ", str(SE))

	min_size_sample = int(np.ceil((std / SE) ** 2))
	print("Minimum number of data points in the sample needed to be significant at 0.05 is ", str(min_size_sample))


def questionFour():
	print("The Null Hypothesis is the mean in engagement between the students who become knowledgeable and the students who do not will be different")
	print("The Alternate Hypothesis is the mean in engagement between the students who become knowledgeable and the students who do not will not be different")
	print("The type of test that can be used is the z-test as we have more than 30 datapoints in our sample based on the rule of thumb")


def questionFive(data0, data1, pop_mean):
	std0 = np.std(data0, ddof = 1)
	std1 = np.std(data1, ddof = 1)

	print("The sample size of eng0 is ", str(len(data0)), " and the sample size of eng1 is ", str(len(data1)))

	overall_mean = np.mean(data0) - np.mean(data1)
	overall_std = math.sqrt(((std0**2) / len(data0)) + ((std1**2) / len(data1)))

	z_score = (overall_mean - pop_mean) / overall_std 

	p_value = 2 * stats.norm.cdf(-abs(z_score))

	print("The mean is ", str(overall_mean))
	print("The standard deviation is ", str(overall_std))
	print("The z-score is", str(z_score))
	print("p_value is ", str(p_value))

	print("The Null Hypothesis can be rejected")

	

if(__name__ == '__main__'):
	data0 = readFile('eng0.txt')
	data1 = readFile('eng1.txt')

	print("Answer to Question 1: ")
	questionOne()

	print("Answer to Question 2: ")
	questionTwo(data1, 0.75)

	print("Answer to Question 3: ")
	questionThree(data1, 0.05, 0.75)

	print("Answer to Question 4: ")
	questionFour()

	print("Answer to Question 5")
	questionFive(data0, data1, 0.75)


