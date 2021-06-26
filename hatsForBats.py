import os
import sys
import pandas 
import argparse
import matplotlib.pyplot as plt
import numpy as np

def DataV1(data):
    # Mean, Median, Mode for relative data: 
    df_mean_elo_pre = data[["elo1_pre", "elo2_pre"]].mean()
    df_mean_eloPreDiff = data[["eloPreDiff"]].mean()
    df_mean_eloProbDiff = data[["eloProbDiff"]].mean()
    print(df_mean_elo_pre)
    print(df_mean_eloPreDiff)
    print(df_mean_eloProbDiff)

def DataV2(data):
    # indivual overal score:
    eloYes = 0
    eloNo = 0

    for row in range(data.shape[0]):
        if data["binaryEloProb1"][row] == data["result1"][row]:
            eloYes+=1
        else: 
            eloNo+=1

    print(eloYes, eloNo)
    
    ratingYes = 0
    ratingNo = 0

    for row in range(data.shape[0]):
        if data["binaryRatingProb1"][row] == data["result1"][row]:
            ratingYes+=1
        else: 
            ratingNo+=1
    print(ratingYes, ratingNo)

    eloWrongRatingRightYes = 0
    eloWrongRatingRightNO = 0

    eloRightRatingWrongYes = 0
    eloRightRatingWrongNO = 0

    for row in range(data.shape[0]):
        if data["binaryEloProb1"][row] == data["result1"][row] & data["binaryRatingProb1"][row] != data["result1"][row]:
            eloRightRatingWrongYes+=1
        if data["binaryEloProb1"][row] != data["result1"][row]: 
            eloRightRatingWrongNO+=1
    print(eloRightRatingWrongYes, eloRightRatingWrongNO)

    elRightRatingRightYes = 0
    eloRightRatingRightNO = 0

    for row in range(data.shape[0]):
        if data["binaryEloProb1"][row] == data["result1"][row] & data["binaryRatingProb1"][row] == data["result1"][row]:
            elRightRatingRightYes+=1
        if data["binaryEloProb1"][row] != data["result1"][row] & data["binaryRatingProb1"][row] != data["result1"][row]: 
            eloRightRatingRightNO+=1
    print(elRightRatingRightYes, eloRightRatingRightNO)

def main():
    #get data file
    parser = argparse.ArgumentParser(description='Data Mine Mark 1 Data Sets.')
    parser.add_argument('log_file', help='Mark 1 Data log file to parse')
    args = parser.parse_args()

    log_file = args.log_file
    #print(log_file)

    #put into pandas

    allData = pandas.read_excel(log_file)
    binaryData = allData[["binaryEloProb1", "binaryEloProb2", "binaryRatingProb1", "binaryRatingProb2", "result1", "result2"]]

    DataV1(allData)
    DataV2(binaryData)
 


if __name__ == '__main__':
    main()
