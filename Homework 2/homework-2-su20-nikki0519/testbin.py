import numpy as np
import matplotlib.pyplot as plt
from problem2 import *

data = np.loadtxt('input.txt')
lo = min(data)
hi = max(data)

print('Uncomment the first segment to verify the histogram you have generated')

histo=plt.hist(data,10,(lo,hi))[0]
print(histo)



print('Uncomment the second segment to verify the normalized histogram you have generated')

norm_h=norm_histogram(histo)
print(norm_h)


print('Uncomment the third segment to verify the J value you have generated')

ch=computeJ(plt.hist(data, 5,(lo,hi))[0],(hi-lo)/5)
print(ch)


print('Uncomment the fourth segment to verify the sweep of J values you have generated')

ro=sweepN(data, lo, hi, 1, 100)
print(ro)


print('Uncomment the fifth segment to verify the min J score you have generated')

minV=findMin(sweepN(data, lo, hi, 1, 100))
print(minV)
