# Importing required libraries and modules
import pandas as pd
import pandas_datareader as web
from datetime import datetime, date
import predictive_analytics as predict
import descriptive_analytics as ad

################################################################################################################
# This method validates the date format and also checks whether given date
# is greater than the current date and raise exception accordingly
# takes argument date and a flag to indicate whether the date is used to load data or to use as prediction date.
################################################################################################################
def validate_date(date_entry, pred_indc_flg):
    flg_valid = False #This flag is used in the calling method to handle further processing.
    try:
        #This formats the date into the YYY-MM-DD format else raise expcetion
        date_entry = datetime.strptime(date_entry.strip(), '%Y-%m-%d').date()

        #checks whether entered date greater/less than the current date.
        # and condition is used to bypass the check when predictiond date is validated as prediction date would be
        # greater than current date
        if date_entry > date.today() and not pred_indc_flg:
            flg_valid = False
            raise ValueError('Input date should not be greater than today') #Raising exception based on condition
        else:
            flg_valid = True
    except ValueError as exp:
        print(exp)
    return date_entry, flg_valid

######################################################################################
#This method asks the user to enter start and end date and calls validate_date method
#checks the start date < end date and handles accordintly
#If exception found then calls itself recursively
######################################################################################
def check_date():
    str_dt = input("\nEnter start date, YYYY-MM-DD: ")
    end_dt = input("\nEnter end date, YYYY-MM-DD: ")
    try:
        start_date, startdate_flag = validate_date(str_dt, False)
        end_date, enddate_flag = validate_date(end_dt, False)
        if startdate_flag and enddate_flag:
            if start_date > end_date:
                raise ValueError('start date can not be greater than end date')
            else:
                return start_date, end_date
        else:
            raise ValueError("Invalid date!!!!")
    except ValueError as exp:
        print(exp)
        start_date, end_date = check_date()
        return start_date, end_date

###############################################################################################################
# this method loads and return stock data of a particular company according to the input ticket passed as input
# parameter, also handles any exception occurred during accessing data from the URL
###############################################################################################################
def compinfo_load(ticker):
    # check if ticker exists in companylist.csv
    if ticker.upper() in trad_companies.index.values:
        comp_info = ''
        try:
            start_date, end_date = check_date()
        except:
            print("Error in date format!!!")

        try:
            comp_info = web.DataReader(ticker, "yahoo", start_date, end_date)   # load data from 'yahoo'
        except Exception as exp:                                          # handles exception and start from start menu
            print("Error loading data from URL, try after sometime...")
            start_menu()
        #change the number of rows display
        # pd.set_option('display.max_rows', 500)
        return comp_info
    # if the entered ticket does not exist in companylist.csv, throws message and back to start menu
    else:
        print("\nNot a valid Ticker; Enter again or Get help from Start menu")
        start_menu()

######################################
# view company date in tabular format
######################################
def compinfoView(comp_info):
    print(comp_info)

######################################################################################################################
# this method takes ticker as input parameter and call compinfo_load method which loads company data by passing ticker
# and returns company data
######################################################################################################################
def enterTicker(ticker):
    comp_info = compinfo_load(ticker)
    return comp_info

#############################################################################################
# this method shows the list of two columns which contain tickers and related company names
#############################################################################################
def helpTicker():
    ticker_list = trad_companies.iloc[:, 0:1]   # returns all rows and 1st two column from dataframe
    print(ticker_list)

############################################################################################
# this method provides choices to go to different functionalities e.g. viewing company data,
# analytical data, prediction or to go back or quit
############################################################################################
def sub_menu(comp_info):
    print("\n\tEnter 1 for Tabular view")
    print("\n\tEnter 2 for Descriptive Analytics")
    print("\n\tEnter 3 for Predictive Analytics")
    print("\n\tEnter 9 to go back to Start menu")
    print("\n\tEnter 0 to quit")

    suboption = input("\nPlease enter your choice: ")

    # View company data as tabular format
    if suboption == '1':
        compinfoView(comp_info)
        sub_menu(comp_info)

    # Goto descriptive_analytics module to view statistical data
    elif suboption == '2':
        ad.analyticsData(comp_info)
        sub_menu(comp_info)

    # Goto prediction module to view prediction of any date
    elif suboption == '3':
        predict.prediction(comp_info, None)
        sub_menu(comp_info)

    # Go back to start menu
    elif suboption == '9':
        start_menu()

    # Quit from programme
    elif suboption == '0':
        close()

    # Handle invalid input and return to submenu
    else:
        print("Invalid choice!!!!!!!!!!!")
        sub_menu(comp_info)

#######################################
# exit from the main TRADING programme
#######################################
def close():
    quit()

#######################################################################################################################
# Start menu of the TRADING programme. It provides three choices, 1. to enter ticker 2. to get help for viewing tickers
# from companylist.csv and 3. Quit from main programme
#######################################################################################################################
def start_menu():
    # Print Start Screen Menu to provide choices
    print("WELCOME TO TRADING \n")
    print("Please choose any of the following options: \n")
    print("\t1. Enter Company Ticker \n")
    print("\t2. Get Assistance Guide for Ticker Code \n")
    print("\t0. Quit")

    option = input("\nEnter your choice please: ")

    # ask user to enter ticker and then calls enterticker method for further processing
    if option == '1':
        input_symbol = input("\nEnter ticker please: ")
        comp_info = enterTicker(input_symbol.strip())

        sub_menu(comp_info)

    # help user to view ticker and related company list from companylist.csv, then back to start menu
    elif option == '2':
        helpTicker()
        start_menu()

    # quit from TRADING programme
    elif option == '0':
        close()

    # handles invalid choice and back to start menu
    else:
        print("Invalid choice!!!!!!!!!!!!!")
        start_menu()

#####################################################################################################################
# Main or starting point of TRADING programme. It loads companylist.csv into dataframe, set 'Symbol' column as the
# index to search ticker through the column, and launch start menu
#####################################################################################################################
if __name__ == "__main__":
# Loading companylist.csv into dataframe
    df = pd.read_csv("companylist.csv")
    trad_companies = df.set_index(['Symbol'])

    # Launch start menu
    start_menu()
