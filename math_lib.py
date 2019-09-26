import sys
import os

def list_mean(L):
    try:
        mean = sum(L)/len(L)
    except ValueError:
         print('must be int')
         sys.exit(1)
    except IndexError:
         print('bound error')
         sys.exit(1)
    #print('mean', mean)
    mean_str = str(mean)
    return mean_str
    

def list_stdev(L):
    try:
        mean = sum(L)/len(L)
    except ValueError:
         print('must be int')
         sys.exit(1)
    except IndexError:
         print('bound error')
         sys.exit(1)
    vector_stdev = L
    vector_stdev[:] = [(x-mean) ** (2) for x in vector_stdev]
    stdev = ((sum(vector_stdev))/len(vector_stdev)) ** (0.5)
    #print('stdev', stdev)
    std_str = str(stdev)
    return std_str

