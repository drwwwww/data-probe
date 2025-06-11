import pandas as pd
import numpy as np
from colorama import init, Fore, Back, Style
import os
import time
import sys

def calc(data, col):
    newCol = data[col].to_numpy()
    print()
    print(Fore.BLUE + Style.BRIGHT + "What calculations would you like to do?" + Style.RESET_ALL)
    print()
    print(Fore.MAGENTA + Style.BRIGHT + "Mean" + "   Median" + "   Standard Deviation" + "   Find Minimum Value" + "   Find Maximum Value" + "   Count missing values" + Style.RESET_ALL)
    print()
    step = input(Fore.BLUE + Style.BRIGHT + "Select an Option: " + Style.RESET_ALL)
    print()

    if step == "/end":
        sys.exit()

    if step == "mean" or step == "Mean":
        m = str(np.nanmean(newCol))
        print(Fore.BLUE + Style.BRIGHT + "The mean of this column is " + m + Style.RESET_ALL)
        time.sleep(2)
        calc(data, col)

    if step == "median" or step == "Median":
        m = str(np.nanmedian(newCol))
        print(Fore.BLUE + Style.BRIGHT + "The median of this column is " + m + Style.RESET_ALL)
        time.sleep(2)
        calc(data, col)
    
    if step == "standard" or step == "standard deviation":
        m = str(np.nanstd(newCol))
        print(Fore.BLUE + Style.BRIGHT + "The standard deviation of this column is " + m + Style.RESET_ALL)
        time.sleep(2)
        calc(data, col)

    if step == "find minimum value" or step == "Find Minimum Value" or step == "find minimum" or step == "find min"  or step == "min":
        m = str(np.nanmin(newCol))
        print(Fore.BLUE + Style.BRIGHT + "The minimum value of this column is " + m + Style.RESET_ALL)
        time.sleep(2)
        calc(data, col)
    
    if step == "find maximum value" or step == "Find Maximum Value" or step == "find maximum" or step == "find max"  or step == "max":
        m = str(np.nanmax(newCol))
        print(Fore.BLUE + Style.BRIGHT + "The maximum value of this column is " + m + Style.RESET_ALL)
        time.sleep(2)
        calc(data, col)

    if step == "count" or step == "Count" or step == "Count missing values" or step == "Count Missing Values" or step == "count missing values":
        nanCount = 0
        

        for num in newCol:
            if np.isnan(num) == False:
                pass
            else:
                nanCount += 1

        print(Fore.BLUE + Style.BRIGHT + "The amount of nan values in this column is " + str(nanCount) + Style.RESET_ALL)
        time.sleep(2)
        calc(data, col)

def analyze(data, col):
    newCol = data[col]
    print()
    print(Fore.RED + Style.BRIGHT + "----- Analytics of " + col + " -----" + Style.RESET_ALL)
    print()
    print(newCol)
    print()
    print(Fore.RED + Style.BRIGHT + "Data Type: " + str(newCol.dtype))
    print()
    print(Fore.RED + Style.BRIGHT + "Number of Unique values: " + str(newCol.nunique()))
    print()
    print(Fore.RED + Style.BRIGHT + "Top 5 Most Frequent Values: " + str(newCol.value_counts().head(5)))
    return

def clean(data, col):
    newData = data.dropna()
    newData.to_csv('myData.csv', index=False)

