# Homework 6
## Due: 07.24.2020, Extended Deadline: 07.29.2020
This homework asks you to fill in portions of classes that you can then use to perform k-means and tf-idf analysis.

# Goals

In this assignment you will:
* Get familiar with using objects and classes by defining some methods and using objects to perform a computation
* Implement k-means
* Compute TF-IDF scores for a set of documents, then find the most distinctive words.

# Background

## Classes and Objects

Please see the class notes on classes and objects.

## k-means

Please see the class notes on clustering and k means.

## TF-IDF

We discussed TF-IDF as a metric to find the "most distinctive" words in documents. In this homework, we will compute TF-IDF scores for a set of documents and use that to determine the most distinctive word in each document. 

## NLTK

NLTK is the Natural Language Toolkit, a set of common text-processing tools for Python. You can install NLTK using:

```
> python3 -mpip install --user nltk
```

We will use NLTK to clean and *stem* the documents before processing the documents. To clean the documents, we will:

1) Remove *stop words* from each document
2) Remove punctuation from the document (you may use the `remove_punc` helper method in `helper.py` to help with this)
2) Make the words lower case
4) Stem the words

There are examples of steps 1 and 3 in the notebook referred to as nltk on BrightSpace.

# Instructions

## 0) Set up your repository for this homework.

Use the link to set up Homework 6. 

The repository should contain the following files:

1. This README.
2. `cluster.py` which contains the definition of the `Cluster` class and some testing code.
3. `point.py` which contains the definition of the `Point` class and some testing code.
4. `kmeans.py` which contains the skeleton of the kmeans algorithm and some testing code.
5. 2. Two starter files with some function stubs called `hw9_1.py` and `hw9_2.py`
3. A helper file called `helper.py` (this contains code to remove punctuation from a string)
6. A directory, `lecs/` that contains 14 text files. These are the documents you will process for Problem 4
## 1) Problem 1: Complete Point class

Complete the missing portions of the `Point` class, defined in `point.py`:

1. `distFrom`, which calculates the (Euclidean) distance between the current point and the target point. Be sure to account for the fact that a point may be in more than two dimensions (Euclidean distance generalizes: square the difference in each dimension and take the square root of the sum). It is okay to use `math.sqrt()` to calculate the square root.
2. `makePointList`, which takes in a data p-by-k input matrix `data` and returns a list of p `Point` objects. Hint: Instantiate a point object for every row in the input, `data`.

If you test your code by running `python3 point.py`, you should get the following:

```
[Point: [0.5 2.5], Point: [0.3 4.5], Point: [-0.5  3. ], Point: [0.  1.2], Point: [10. -5.], Point: [11.  -4.5], Point: [ 8. -3.]]
2.009975124224178
```

(Your floating point numbers may be a little off due to rounding)

## 2) Problem 2: Complete Cluster class

Complete the missing portions of the `Cluster` class, defined in `cluster.py`:

1. `avgDistance`, which computes the average distance from the center of the cluster (stored in `self.center`) to all of the points currently in the cluster (stored in `self.points`). This can most easily be done by summing the distances between each point and the current center and then dividing the sum by the total number of points.
2. `updateCenter`, which updates the center of the cluster (stored in `self.center`) to be the average position of all the points in the cluster. Note that if there are no points in the cluster, you should return without updating (i.e., if there are no points, just type the command `return`.

> Note that we have defined `dim` and `coords` as properties that return information about the center of the cluster -- this means that if you pass a cluster into a method that is expecting a point, operations that access `dim` and `coords` will use the center of the cluster. Think about how that might be useful in conjunction with the `closest` method defined for `Point`.

If you test your code by running `python3 cluster.py`, you should get the following:

```
Cluster: 0 points and center = [0.5, 3.5]
Cluster: 2 points and center = [0.5, 3.5]
1.4976761962286425
Cluster: 2 points and center = [1.75, 2.75]
0.3535533905932738
```

(Your floating point numbers may be a little off due to rounding)

## 3) Problem 3: Implement k-means

Use the methods in `Point` and `Cluster` to implement the missing `kmeans` method in `kmeans.py`. The basic recommended procedure is outlined in `kmeans.py`.

If you test your code by running `python3 kmeans.py`, you should get the following:

```
Cluster: 4 points and center = [0.075 2.8  ]
   [0.3 4.5]
   [0.  1.2]
   [0.5 2.5]
   [-0.5  3. ]
Cluster: 3 points and center = [ 9.66666667 -4.16666667]
   [ 8. -3.]
   [10. -5.]
   [11.  -4.5]
```

(Your floating point numbers may be a little off due to rounding)


## 4) Problem 4: TF-IDF

For this problem, we will compute the tf-idf scores for all the terms in each document in the `lecs/` folder.

Fill in the missing functions in `tf_idf.py`, according to their specifications. You may find the lecture notes helpful on how to construct a doc-word matrix.

Note that even after installing nltk and importing it, you may need to add the following below your nltk import statement:
```
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
```
See the Jupyter notebook on this material for a good walkthrough of how to generally use nltk for the purposes of this assignment.

While we will test you using our own tests, at the end of `tf_idf.py` are some good test cases to check your code as you go. Feel free to uncomment and recomment them where convenient for you as you write the different functions. The output to those should be:
```
*** Testing readAndCleanDoc ***
['let', "'s", 'look', 'wifi', "'s"]
*** Testing buildDocWordMatrix ***
(2, 429)
429
[2. 9. 2. 1. 1. 1. 3. 2. 1. 4.]
["'re", "'s", "'ve", '.11', '1', '1.2', '100', '11', '1997', '1999']
[ 6. 11.  0.  0.  0.  0.  0.  0.  0.  0.]
*** Testing buildTFMatrix ***
[0.00305344 0.01374046 0.00305344 0.00152672 0.00152672 0.00152672
 0.00458015 0.00305344 0.00152672 0.00610687]
[0.01438849 0.0263789  0.         0.         0.         0.
 0.         0.         0.         0.        ]
[1. 1.]
*** Testing buildIDFMatrix ***
[0.      0.      0.30103 0.30103 0.30103 0.30103 0.30103 0.30103 0.30103
 0.30103]
*** Testing buildTFIDFMatrix ***
(2, 429)
[0.         0.         0.00091918 0.00045959 0.00045959 0.00045959
 0.00137876 0.00091918 0.00045959 0.00183835]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
*** Testing findDistinctiveWords ***
{'lecs/1_vidText.txt': array(['second', 'per', 'megabit'], dtype='<U12'), 'lecs/2_vidText.txt': array(['point', 'router', 'set'], dtype='<U12')}
```


# What you need to submit

Push your completed versions of `kmeans.py`, `cluster.py`, `point.py` and `tf_idf.py`.
