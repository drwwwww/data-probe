import pandas as pd
import numpy as np
from colorama import init, Fore, Back, Style
import os
import time
import sys
import calc

def analyze():
    pass


def calcnum():
    print(Fore.BLUE + Style.BRIGHT + "----- Calculate Numeric Columns -----" + Style.RESET_ALL)
    print()
    
    for name in data.columns:
        print(Fore.MAGENTA + Style.BRIGHT + name + Style.RESET_ALL)

    print()
    col = input(Fore.BLUE + Style.BRIGHT + "Which column would you like to calculate? (Only numerical data can be calculated): " + Style.RESET_ALL)

    if col == "/end":
        sys.exit()
    
    if col not in data.columns:
        print()
        print(Fore.RED + Style.BRIGHT + "Please Select a Valid Column" + Style.RESET_ALL)
        print()
        time.sleep(0.5)
        calcnum()

    elif data[col].dtype != "int64" and data[col].dtype != "float64":
        print()
        print(Fore.RED + Style.BRIGHT + "Please Select a Column With Numerical Data" + Style.RESET_ALL)
        print()
        time.sleep(0.5)
        calcnum()
    
    else:
        calc.calc(data, col)





def dataHandling():
    print(Fore.GREEN + Style.BRIGHT + "What would you like to do with your data?" + Style.RESET_ALL)
    print()
    print(Fore.BLUE + Style.BRIGHT + "Calculate Numeric Columns" + Fore.RESET + Fore.RED + "        Analyze a Column"  + Fore.RESET + Fore.MAGENTA + "        Clean Data" + Style.RESET_ALL)
    print()
    step = input(Fore.GREEN + Style.BRIGHT + "Select an option: " + Style.RESET_ALL)

    if step == "/end":
        sys.exit()
    
    elif step == "Calculate Numeric Columns" or step == "calculate numeric columns" or step == "calculate" or step == "1":
        print()
        calcnum()

    elif step == "Analyze a Column" or step == "analyze a column" or step == "analyze" or step == "2":
        print()
        analyze()

    else:
        print()
        print(Fore.RED + Style.BRIGHT + "Please Select a Given Option" + Style.RESET_ALL)
        print()
        time.sleep(0.5)
        dataHandling()
        



def main():
    init()

    print(Fore.BLUE + Style.BRIGHT + "----- Welcome to my Data Probe Project | A simple python terminal app to allow users to analyze and clean CSV data -----")
    print()

    try:
        file = input("Type or paste the path to your file here or enter '/end' to end the program: " + Style.RESET_ALL).strip().strip('"').strip("'")
    
    except OSError:
        print()
        print(Fore.RED + Style.BRIGHT + "Issue With File Path" + Style.RESET_ALL)
        print()
        time.sleep(0.5)
        main()

    except FileNotFoundError:
        print()
        print(Fore.RED + Style.BRIGHT + "Could Not Find File" + Style.RESET_ALL)
        print()
        time.sleep(0.5)
        main()

    if file == "/end":
        sys.exit()

    elif file == int or file == float:
        print()
        print(Fore.RED + Style.BRIGHT + "Please Enter a Valid File Path" + Style.RESET_ALL)
        print()
        time.sleep(0.5)
        main()

    else: # Main actual working part of the code
        try:
            print()
            global data
            data = pd.read_csv(file)
            print(Fore.GREEN + Style.BRIGHT + "----- File Found! | Here is your data -----" + Style.RESET_ALL)
            print()
            print(data)
            dataHandling()
            return data

        
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "Please Enter a Valid CSV File" + Style.RESET_ALL)
            print()
            time.sleep(0.5)
            main()

        except FileNotFoundError:
            print(Fore.RED + Style.BRIGHT + "Could Not Find File" + Style.RESET_ALL)
            print()
            time.sleep(0.5)
            main()


main()