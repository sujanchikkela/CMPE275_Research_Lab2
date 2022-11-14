# import ctypes python and c/c++ binding library.
import ctypes
import time
import numpy as np
from maxprofitpython import *

# generate .so file from the .c file and invike the .so file in the .py file
librefObject = ctypes.CDLL('/home/rakshith/maxprofit.so')

# using numpy randint function generate a list of random integers which is used as the input for the algorithm.
prices= np.random.randint(100,1000,500)

sample_size = len(prices)

def toArray(list):
        pythonctypesarray=len(list) * ctypes.c_int
        integerarray=pythonctypesarray()
        current=0
        for element in list:
                integerarray[int(current)]=int(element)
                current=current+1
        return integerarray

prices = toArray(prices)

# Invoke the maxprofit function signature.
maxprofit = librefObject.maxprofit

# define the input arguments syntax
maxprofit.argtypes = [ctypes.c_void_p]
# define the return type of the function
maxprofit.restype= ctypes.c_int

# Get the time stamp before the function execution.
start_time = time.time()

# function call
profit = maxprofit(prices,sample_size)

print("the max profit calculated is " , profit)

# Get the time stamp after the function execution.
print("--- time taken in Python ctypes is %s seconds---" % (time.time() - start_time))

# Get the time stamp before the function execution.
start_time_python = time.time()

# function call
maxProfit(prices)
# Get the time stamp after the function execution.
print("--- time taken in pure Python is %s seconds ---" % (time.time() - start_time_python))
