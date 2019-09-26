import get_data
import math_lib
import argparse
import matplotlib.pyplot as plt
import sys
import os 

def boxplot(L, out_file_name):
    plt.figure()
    plt.boxplot(L)
    plt.xlabel('List')
    plt.ylabel('Signal')
    title_str_mean = math_lib.list_mean(L)
    title_str_stdev = math_lib.list_stdev(L)
    plt.title('mean: '+title_str_mean+ ' | stdev: '+title_str_stdev)
    plt.savefig(out_file_name+'.png')
    pass

def histogram(L, out_file_name1):
    plt.figure()
    plt.hist(L)
    plt.xlabel('Signal')
    plt.ylabel('Counts')
    title_str_mean = math_lib.list_mean(L)
    title_str_stdev = math_lib.list_stdev(L)
    plt.title('mean: '+title_str_mean+ ' | stdev: '+title_str_stdev)
    plt.savefig(out_file_name1+'.png')
    pass

def combo(L, out_file_name2):
    pass

def main():
    parser = argparse.ArgumentParser(
             description='input file and column number; returns the mean & std',
             prog='input arg')

    parser.add_argument('--col_num', type=int, help='The column number')

    args = parser.parse_args()

    col_index = 1 #integer specifying column index
    L = get_data.read_stdin_col(col_index)
    L1 = L[:]
    out_file_name = 'boxplot'
    out_file_name1 = 'histogram'
    out_file_name2 = 'boxplot_histogram'
    boxplot(L,out_file_name)
    histogram(L1,out_file_name1)

if __name__ == '__main__':
    main()