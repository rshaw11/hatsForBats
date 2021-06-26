import os
import sys
import pandas 
import argparse
import matplotlib.pyplot as plt
import numpy as np

def main():
    #get data file
    parser = argparse.ArgumentParser(description='Data Mine Mark 1 Data Sets.')
    parser.add_argument('log_file', help='Mark 1 Data log file to parse')
    args = parser.parse_args()

    log_file = args.log_file
    #print(log_file)

    #put into pandas

    allData = pandas.read_excel(log_file)
    print(allData)
 


if __name__ == '__main__':
    main()
