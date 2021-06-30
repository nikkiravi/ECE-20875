# Homework 2

### Due Friday, June 26

## Goals

This homework has several objectives:

1. Get familiar with the different data structures available in Python.
2. Leverage the concept of functions to write modular code.
3. Build up a complex analysis code by building smaller functions first

# Instructions

## 0) Set up your repository for this homework

The repository should contain 6 files:

1. This README
2. 1 input data file: `input.txt`, which you will use in problem2.
3. Two tester codes: `testaddress.py` and `testbin.py`.
4. Two skeleton codes with instructions for each problem: `problem1.py` and `problem2.py`.


## Problem 1: Creating a dictionary

Create a function called `addressbook` that takes as input two dictionaries, `name_to_phone` and `name_to_address`, and combines them into a single dictionary `address_to_all` that contains the phone number of, and the names of all the people who live at, a given address. Specifically, your function should:

1. Have input arguments `addressbook(name_to_phone, name_to_address)`, expecting `name_to_phone` as a dictionary mapping a name (string) to a home phone number (integer or string), and `name_to_address` as a dictionary mapping a name to an address (string).
2. Create a new dictionary `address_to_all` where the keys are all the addresses contained in `name_to_address`, and the value `address_to_all[address]` for `address` is of the format `([name1,name2,...], phone)`, with `[name1,name2,...]` being the list of names living at `address` and `phone` being the home phone number for `address`. **Note**: the *value* we want in this new dictionary is a *tuple*, where the first element of the tuple is a *list* of names, and the second element of the tuple is the phone number. (Remember that while a tuple itself is immutable, a list within a tuple can be changed dynamically.) 
3. Handle the case where multiple people at the same address have different listed home phone numbers as follows: Keep the first number found, and print warning messages with the names of each person whose number was discarded.
4. Return `address_to_all`.

For example, typing in

```
name_to_phone = {'alice': 5678982231, 'bob': '111-234-5678', 'christine': 5556412237, 'daniel': '959-201-3198', 'edward': 5678982231}
name_to_address = {'alice': '11 hillview ave', 'bob': '25 arbor way', 'christine': '11 hillview ave', 'daniel': '180 ways court', 'edward': '11 hillview ave'}
address_to_all = addressbook(name_to_phone, name_to_address)
print(address_to_all)
```

should return

```
Warning: christine has a different number for 11 hillview ave than alice. Using the number for alice.
{'11 hillview ave': (['alice', 'christine', 'edward'], 5678982231), '25 arbor way': (['bob'], '111-234-5678'), '180 ways court': (['daniel'], '959-201-3198')}
```
Your message should match exactly as shown above. If more than one person has a different phone number at the same address then use a `,` to separate the names.

Note that the specific order you get these elements back may not be the same, because sets and dictionaries do not preserve order. That is OK!

And yes, we know people rarely use home phone numbers anymore, but that doesn't change this problem being a good Python coding exercise! :)

## Problem 2: Histogram Bin Width Optimization

### Incremental Development

In this problem, we will ask you to write a fairly complex piece of code: finding the number of histogram bins that results in the lowest error for a given data set. When you need to write complex code like this, your goal should be to break the problem down into smaller pieces. Write functions that solve each of the smaller pieces, then figure out how to connect those functions together (some of them might call other functions you write) to solve the overall problem.

This approach makes it much easier to write complex code, both because you do not have to solve the problem all in one go, and because it makes it easier to *test* your code: you can test each of your smaller pieces individually to make sure that they work properly.

In this homework, we will walk you through one particular way you can break down the problem (and, in fact, we want you to solve the problem in this way -- we will test the individual pieces for partial credit).
Please be mindful that variables declared in a function can only be accessed when that particular function is being called.

You will use the histogram function in `matplotlib.pyplot`, accessed as `matplotlib.pyplot.hist` or `plt.hist` if you `import matplotlib.pyplot as plt`. Please read the documentation: [`matplotlib.pyplot.hist`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html). (Note in particular that the function returns three variables: `n`, `bins`, and `patches`, but you only need `n`, so be sure to unpack the output accordingly.)

We have broken the problem down into smaller pieces for you. `problem1.py` has four functions for you to fill in. **Keep the signatures of these functions the same as you are filling them in; we will use these to assign partial credit**. 

### Background

1. `norm_histogram` takes a histogram of counts and creates a histogram of probabilities. 
2. `computeJ` computes the value of J for a given histogram and bin width.
3. `sweepN` computes the `computeJ` score for each of a range of *numbers of buckets* and returns a list of the associated `computeJ` scores. This function should use `computeJ` in its implementation (this function should use `matplotlib.pyplot.hist` in its implementation. note that `sweepN` cares about the number of buckets while `computJ` cares about the width of the buckets -- make sure to do the conversion!).
4. `findMin` is a generic function that takes a list of numbers and returns a tuple containing the smallest number in that list and the index of that smallest number.

You can use `input.txt`, provided in the repository, as test data. To test each function individually please refer to `testbin.py`. There are instructions available to test each portion of your code. 

Within `testbin.py` if:
1. `norm_histogram` runs correctly then the output will be `[0.0080000000000000002, 0.035999999999999997, 0.097000000000000003, 0.188, 0.254, 0.216, 0.13, 0.042999999999999997, 0.021000000000000001, 0.0070000000000000001]`
2. `computeJ` works then the output will be `[0.0080000000000000002, 0.035999999999999997, 0.097000000000000003, 0.188, 0.254, 0.216, 0.13, 0.042999999999999997, 0.021000000000000001, 0.0070000000000000001]`
3. `sweepN` works then the output should be `[-0.015621363151391314, -0.016021413220440317, -0.02550678608199591, -0.024879428353681995, -0.026044109747591276, -0.026750231483504514, -0.027167499453420379, -0.027149436278873323, -0.027354861457578164, -0.027317921202626164, -0.027374051528178144, -0.027707797026252572, -0.027561538753433142, -0.027663406084742367, -0.027554432393618267, -0.02748152237849167, -0.027714308366937675, -0.027440512406606232, -0.02758148002552039, -0.027607494677192507, -0.027561288061046702, -0.02740194418356845, -0.027517053645908011, -0.02755114505835041, -0.027327938421293253, -0.027569677718190008, -0.02762843768678348, -0.02741753402252755, -0.027598728918921553, -0.027351104167907748, -0.027436943198773649, -0.027448463508443287, -0.027344436050659133, -0.027374770830185122, -0.027558657980169224, -0.027363313037242078, -0.027297540624656655, -0.027302518131996887, -0.027318984675006475, -0.027186751165074966, -0.027287554117057883, -0.027275971134291605, -0.027333103228621283, -0.027156071871161633, -0.027312598211404568, -0.027342087748524379, -0.027181679491719797, -0.027399376337951583, -0.027287585172140166, -0.027146367048483572, -0.027235868796442981, -0.027262008669212311, -0.027051261531327898, -0.027355423545185602, -0.027252491772002077, -0.02715895158110955, -0.027010470633814579, -0.027035859180000621, -0.027080876133174892, -0.027089078083768384, -0.027168186480659048, -0.027165212448326224, -0.027070858320301816, -0.026999670095261902, -0.026969804832302467, -0.026851658695807488, -0.026809646986418339, -0.027026717727164036, -0.026799910983561982, -0.027067790184502078, -0.026956593818902443, -0.027059024645149133, -0.026714979649280896, -0.027023023517152224, -0.026547652895581281, -0.026961101622032132, -0.026751794526765679, -0.02695759536876215, -0.026741808081714884, -0.026744719440951109, -0.026754455349985468, -0.026535412314410659, -0.026495247616205409, -0.026846023183500867, -0.026412570324222156, -0.026634462077210576, -0.026361323527639501, -0.026570661865632252, -0.026507613011911256, -0.026704022271616713, -0.026556323956179306, -0.026683986833514542, -0.026496562124986151, -0.026737330958379511, -0.026346672409073509, -0.026614989883853853, -0.026749508616261519, -0.026331927531054612, -0.026287599231367011, -0.026550000009304027]`
4. `findMin` executes then your output should be `(-0.027714308366937675, 16)`


If your functions all work, and you run the test code that is included in `problem2.py`, you should produce the following output: `(-0.027714308366937675, 16)`

> The `if __name__ == '__main__'` line in `problem2.py` is a useful way to write tests for your code: this is code that will *only* run if you run this file as the main script; if this file is included from another script, this test code will not run.


# Testing

We have provided two test programs for you, that recreate the examples from above, in `testaddress.py` and `testbin.py` , which test problems 1 and 2, respectively. Note that these test programs will only work "out of the box" if you have your solution in `problem1.py` and `problem2.py`.


# What to Submit

You should submit `problem1.py` and `problem2.py` for this homework. 

Once you have a version of this file (that you have `commit`ted using `git commit` and `push`ed using `git push`) that you are happy with, you are done!
