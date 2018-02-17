import matplotlib.pyplot as plt
import pandas as pd
import datetime
from scipy import stats
import display_menu as dsp
from sklearn.metrics import mean_squared_error
from math import sqrt


#######################################################################################################
#This portion of code is used to caluclate the prediction of the stock fact for a particular date value
#The date value for prediction could be past or future date.
#######################################################################################################

#Function for predicting the fact for any specific date
def linear_regression(date, fact, pd_date):
    lr = stats.linregress(date, fact)
    print("The slope for the training data set is {} and Intercept {}".format(lr[0], lr[1]))
    y_value = lr[1] + date * lr[0]
    pred_value = lr[1] + pd_date * lr[0]
    print("The Rsquare value for the model is {}".format(lr[2]**2))
    rms = sqrt(mean_squared_error(fact, y_value))
    print("The RMSE of the model is {}".format(rms))
    date_conv = pd.to_datetime(date)

    # plotting curve for linear regression model
    plt.plot(date_conv, fact, 'o', label='original data')
    # plt.plot(date_conv, lr[1] + date*lr[0], 'r', label='fitted line')
    plt.plot(date_conv, y_value, 'r', label='fitted line')
    plt.legend()
    plt.show()

    return pred_value

#######################################################################################
# this method prints fact choices and returns the selected choice taken from user input
#######################################################################################
def pred_factchoice_menu():
    print("On which fact data do you want to predict??")
    print("\n\tPress 1 for Open")
    print("\n\tPress 2 for High")
    print("\n\tPress 3 for Low")
    print("\n\tPress 4 for Close")
    print("\n\tPress 5 for Adj Close")
    print("\n\tPress 6 for Volume")
    print("\n\tEnter 9 to go back to previous menu")
    print("\n\tEnter 0 to quit")

    choice = input("Enter your choice:")
    return choice

####################################################################################################
# this method gives two choices to user to opt for another prediction or to go back to previous menu
####################################################################################################
def prediction_choices():
    print("Do you want to predict another fact?")
    choice = input("\n\t Press Y to continue with same date and N to go back to previous menu: ")
    return choice.strip().upper()

########################################################################################################
# this method is the primary function of predictive analysis which passes webdata, dataframe received
# from display_menu module, and prediction date as None as input parameters
#######################################################################################################
def prediction(webdata, prediction_date):
    s = pd.Series(webdata.index)
    Date = pd.to_numeric(s)

#Prediction Date input from user and its Validation
    if prediction_date is None:
        try:
            pred_date = input("Enter date for prediction in YYYY-MM-DD format: ")
            pred_date = dsp.validate_date(pred_date, True)[0]
            date_string = pred_date.strftime('%Y-%m-%d')
            year, month, day = map(int, date_string.split('-'))
            prediction_date = datetime.date(year, month, day)
        except Exception as exp:
            print(exp)
            print("Invalid input date. Please try again")
            prediction(webdata, prediction_date)

    pred = pd.Timestamp(prediction_date) #Converting prediction date ti Timestamp.
    predict_date_series = pd.Series(pred) #Creating series of prediction date.
    predict_date = pd.to_numeric(predict_date_series) #Converting predicted date series to numeric from timestamp.

    choice = pred_factchoice_menu()

    #choice = input("Enter your choice:")
    if choice == '1':
        Open = webdata['Open'] #Fetching Open fact from dataframe and storing it in variable Open
        predicted_value = linear_regression(Date, Open, predict_date) #Passing start to end dates, fact with prediction date in function
        print("The predicted value for Open on {} is {}".format(prediction_date, predicted_value[0]))

        if prediction_choices() == 'Y':
            prediction(webdata,prediction_date) #Calling prediction function for calculating new predictions.
        else:
            dsp.sub_menu(webdata)

    elif choice == '2':
        High = webdata['High']
        predicted_value = linear_regression(Date, High, predict_date)
        print("The predicted value for High on {} is {}".format(prediction_date, predicted_value[0]))

        if prediction_choices() == 'Y':
            prediction(webdata,prediction_date) #Calling prediction function for calculating new predictions.
        else:
            dsp.sub_menu(webdata)

    elif choice == '3':
        Low = webdata['Low']
        predicted_value = linear_regression(Date, Low, predict_date)
        print("The predicted value for Low on {} is {}".format(prediction_date, predicted_value[0]))

        if prediction_choices() == 'Y':
            prediction(webdata,prediction_date) #Calling prediction function for calculating new predictions.
        else:
            dsp.sub_menu(webdata)

    elif choice == '4':
        Close = webdata['Close']
        predicted_value = linear_regression(Date, Close, predict_date)
        print("The predicted value for Close on {} is {}".format(prediction_date, predicted_value[0]))

        if prediction_choices() == 'Y':
            prediction(webdata,prediction_date) #Calling prediction function for calculating new predictions.
        else:
            dsp.sub_menu(webdata)

    elif choice == '5':
        adjusted_close = webdata['Adj Close']
        predicted_value = linear_regression(Date, adjusted_close, predict_date)
        print("The predicted value for Adjusted Close on {} is {}".format(prediction_date, predicted_value[0]))

        if prediction_choices() == 'Y':
            prediction(webdata,prediction_date) #Calling prediction function for calculating new predictions.
        else:
            dsp.sub_menu(webdata)

    elif choice == '6':
        Volume = webdata['Volume']
        predicted_value = linear_regression(Date, Volume, predict_date)
        print("The predicted value for Volume on {} is {}".format(prediction_date, predicted_value[0]))

        if prediction_choices() == 'Y':
            prediction(webdata,prediction_date) #Calling prediction function for calculating new predictions.
        else:
            dsp.sub_menu(webdata)

    elif choice == '9':
        dsp.sub_menu(webdata)

    elif choice == '0' :
        dsp.close()

    else:
        print("Invalid Choice!!!!!!!!!!!")
        prediction(webdata, prediction_date)