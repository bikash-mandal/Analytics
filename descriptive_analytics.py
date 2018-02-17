import pandas as pd
import display_menu as dm
import matplotlib.pyplot as plt
from scipy import stats
    
def analyticsData(comp_info_data):
    """ This method provides the user with flexibilty to select various options 
    from the Descriptive Analytics Menu """
    
    print("\nDescriptive Analytics menu")
    print("\n\tEnter 1 for Descriptive Summary of the entire dataset")
    print("\n\tEnter 2 for Summary of specific facts")
    print("\n\tEnter 3 for Data visualisation")
    print("\n\tEnter 9 to go back to the previous menu")
    print("\n\tEnter 0 to Quit")
    suboption = input("\nPlease enter your choice: ")
    
    if suboption == '1':
        overview(comp_info_data)
        analyticsData(comp_info_data)
               
    elif suboption == '2':
        summary_fact(comp_info_data)
        analyticsData(comp_info_data)
        
    elif suboption == '3':
        select_fact(comp_info_data)
        analyticsData(comp_info_data)
        
    elif suboption == '9':
        dm.sub_menu(comp_info_data)
    
    elif suboption == '0':
        dm.close()
    
    else:
        print("\nInvalid Input Please try again")
        analyticsData(comp_info_data)

def summary_fact(comp_info_data):
    """ This method gives the user flexibility to choose the fact """
    
    print("\nPlease select fact to see descriptive summary")
    print("\n\tEnter 1 for Open")
    print("\n\tEnter 2 for High")
    print("\n\tEnter 3 for Low")
    print("\n\tEnter 4 for Close")
    print("\n\tEnter 5 for Adjusted Close")
    print("\n\tEnter 6 for Volume")
    print("\n\tEnter 9 to go back to the previous menu")
    print("\n\tEnter 0 to Quit")
    suboption_choices = input("\nPlease enter your choice: ")
    
    if suboption_choices == '1':
        """ If user selects option 1 it will display the summary for Open fact """
        
        option = "Open"
        summary(comp_info_data,option)
        summary_fact(comp_info_data)
                   
    elif suboption_choices == '2':
        """ If user selects option 2 it will display the summary for High fact """
        
        option = "High"
        summary(comp_info_data,option)
        summary_fact(comp_info_data)
            
    elif suboption_choices == '3':
        """ If user selects option 3 it will display the summary for Low fact """
        
        option = "Low"
        summary(comp_info_data,option)
        summary_fact(comp_info_data)
            
    elif suboption_choices == '4':
        """ If user selects option 4 it will display the summary for Close fact """
        
        option = "Close"
        summary(comp_info_data,option)
        summary_fact(comp_info_data)
            
    elif suboption_choices == '5':
        """ If user selects option 5 it will display the summary for Adjusted Close fact """
        
        option = "Adj Close"
        summary(comp_info_data,option)
        summary_fact(comp_info_data)
            
    elif suboption_choices == '6':
        """ If user selects option 6 it will display the summary for VOlume fact """
        
        option = "Volume"
        summary(comp_info_data,option)
        summary_fact(comp_info_data)
            
    elif suboption_choices == '9':
        """ If user will be directed to the previous menu on selecting option 9 """
        
        analyticsData(comp_info_data)
    
    elif suboption_choices == '0':
        """ The application quits on selecting option 0  """
        
        dm.close()

    else:
        print("\nInvalid Input Please try again")
        summary_fact(comp_info_data)

def overview(comp_info_data):
    """It displays the overview of the entire dataset"""
    
    overview = comp_info_data.describe()
    print(overview)
    return overview
        
def mean_of_fact(comp_info_data, option):
    """ Calculates the mean of the fact selected by user """
    
    mean_of_column = comp_info_data[option].mean()    
    return mean_of_column

def median_of_fact(comp_info_data, option):
    """ Calculates the median of the fact selected by user """
    
    median_of_column = comp_info_data[option].median()    
    return median_of_column

def quartiles_of_fact(comp_info_data,option):
    """ Calculates the quantiles (25% and 75%) of the fact selected by user """
    
    lower_quartile = comp_info_data[option].quantile(0.25)
    upper_quartile = comp_info_data[option].quantile(0.75)
    return (lower_quartile, upper_quartile)

def range_of_facts(comp_info_data, option):
    """ Calculates the range of the fact selected by user """
    
    range_of_col = comp_info_data[option].max() - comp_info_data[option].min()
    return range_of_col

def standard_deviation_of_facts(comp_info_data, option):
    """ Calculates the standard deviation of the fact selected by user """
    
    sd_of_column = comp_info_data[option].std()   
    return sd_of_column

def variance_of_facts(comp_info_data, option):
    """ Calculates the variance of the fact selected by user """
    
    variance = (standard_deviation_of_facts(comp_info_data, option)) ** 2
    return variance

def coeff_of_variannce_of_facts(comp_info_data, option):
    """ Calculates the coefficient of variance the fact selected by user """
    
    coeff_of_var = standard_deviation_of_facts(comp_info_data, option) / median_of_fact(comp_info_data, option)    
    return coeff_of_var

def summary(comp_info_data,option):
    """ Prints the summary of the fact selected by user """
    
    print("\n\tSummary of {}".format(option))
    print("\n\tMean: ",mean_of_fact(comp_info_data, option))
    print("\n\tMedian: ",median_of_fact(comp_info_data, option))
    print("\n\tLower Quartile(25%): ",quartiles_of_fact(comp_info_data,option)[0])
    print("\n\tUpper Quartile(75%): ",quartiles_of_fact(comp_info_data,option)[1])
    print("\n\tRange: ",range_of_facts(comp_info_data, option))
    print("\n\tStandard Deviation:  ",standard_deviation_of_facts(comp_info_data, option))
    print("\n\tVariance:  ",variance_of_facts(comp_info_data, option))
    print("\n\tCoefficient of variance :  ",coeff_of_variannce_of_facts(comp_info_data, option))

def select_fact(comp_info_data):
    """ User will the option to select fact for Data Visualisation """
    
    print("\nSelect fact for Data Visualisation")
    print("\n\tEnter 1 for Open")
    print("\n\tEnter 2 for High")
    print("\n\tEnter 3 for Low")
    print("\n\tEnter 4 for Close")
    print("\n\tEnter 5 for Adjusted Close")
    print("\n\tEnter 6 for Volume")
    print("\n\tEnter 9 to go back to the previous menu")
    print("\n\tEnter 0 to Quit")
    
    suboption1 = input("\nPlease enter your choice for fact: ")
    
    if suboption1 == '1':
      option = "Open"
      data_visualisation(comp_info_data, option)
            
    elif suboption1 == '2':
        option = "High"
        data_visualisation(comp_info_data, option)
            
    elif suboption1 == '3':
        option = "Low"
        data_visualisation(comp_info_data, option)
            
    elif suboption1 == '4':
        option = "Close"
        data_visualisation(comp_info_data, option)
            
    elif suboption1 == '5':
        option = "Adj Close"
        data_visualisation(comp_info_data, option)
            
    elif suboption1 == '6':
        option = "Volume"
        data_visualisation(comp_info_data, option)
            
    elif suboption1 == '9':
        analyticsData(comp_info_data)
    
    elif suboption1 == '0':
        dm.close()
            
# handle invalid choice
    else:
        print("\n\tInvalid input please try again")
        select_fact(comp_info_data)


def data_visualisation(comp_info_data, option):
    """ This method is the begining of the data visualisation.
    It asks the user for the type of data visualisation wanted such as time-series, trend lines etc.. 
    It also gives the user the flexibility to select the fact in order to visualise the data"""

    print("\nTypes of Data Visualisation")
    print("\n\tEnter 1 for raw time-series")
    print("\n\tEnter 2 for trend lines")
    print("\n\tEnter 3 for moving averages")
    print("\n\tEnter 4 for exponential moving averages")
    print("\n\tEnter 5 for moving averages convergence/divergence")
    print("\n\tEnter 9 to go back to the previous menu")
    print("\n\tEnter 0 to Quit")
    
    suboption_choice = input("\nPlease enter your choice: ")
    
    if suboption_choice == '1':
      """" Raw time series of the selected fact is displayed on choosing option 1 """
      
      comp_info_data1 = raw_time_series(comp_info_data,option)
      plt.plot(comp_info_data1['Date'],comp_info_data1[option],'r')
      plt.ylabel(option)
      plt.xlabel('Date')
      plt.title('Raw Time Series for {}'.format(option))
      plt.grid(True)
      plt.show()
      data_visualisation(comp_info_data, option)
        
    elif suboption_choice == '2':
        """" Trend lines of the selected fact is displayed on choosing option 2 """
        
        comp_info_data1,y = trend_lines(comp_info_data, option)
        plt.plot(comp_info_data1['Date'],comp_info_data1[option],'r',label = 'Time Series for {}'.format(option))
        plt.plot(comp_info_data1['Date'],y,'b', label = 'Trend Line for {}'.format(option))
        plt.legend(loc='upper left')
        plt.ylabel(option)
        plt.xlabel('Date')
        plt.title('Trend Lines for {}'.format(option))
        plt.grid(True)
        plt.show()
        data_visualisation(comp_info_data, option)
                     
    elif suboption_choice == '3':
        """" Moving average of the selected fact is displayed on choosing option 3 """
        
        window = input("\nPlease enter the window size of your choice: ")
        try:
            window = int(window)
        except ValueError:
            print("Not an Integer value!!! Going back to previous menu for re-entry...")
            data_visualisation(comp_info_data, option)
            
        comp_info_data1 = moving_average(comp_info_data,option,window)
        plt.plot(comp_info_data1['Date'], comp_info_data1['Moving Average'],'b',label = 'Moving Average {}'.format(option))
        plt.plot(comp_info_data1['Date'], comp_info_data1[option], 'r',label = 'Original {}'.format(option))
        plt.legend(loc='upper left')
        plt.ylabel(option)
        plt.xlabel('Date')
        plt.title('Moving Average for {}'.format(option))
        plt.grid(True)
        plt.show()
        data_visualisation(comp_info_data, option)
    
    elif suboption_choice == '4':
        """" Exponential weighted moving average of the selected fact is displayed on choosing option 4 """    
        
        window = input("\nPlease enter the window size of your choice: ")
        try:
            window = int(window)
        except ValueError:
            print("Not an Integer value!!! Going back to previous menu for re-entry...")
            data_visualisation(comp_info_data, option)
            
        comp_info_data1 = exponential_moving_average(comp_info_data,option,window)
        plt.plot(comp_info_data1['Date'],comp_info_data1[option], 'r', label = 'Original {}'.format(option))
        plt.plot(comp_info_data1['Date'], comp_info_data1['ema'], 'b',label = 'Exponential Weighted Moving Average  for {}'.format(option))
        plt.legend(loc='upper left')
        plt.ylabel(option)
        plt.xlabel('Date')
        plt.title('Exponential Weighted Moving Average for {}'.format(option))
        plt.grid(True)
        plt.show()
        data_visualisation(comp_info_data, option)
        
    elif suboption_choice == '5':
        """ Moving average convergence/divergence of the selected fact is displayed on choosing option 5 """

        comp_info_data1 = moving_average_converg_diverg(comp_info_data,option)
        plt.plot(comp_info_data1['Date'], comp_info_data1[option], 'r',label = 'Original {}'.format(option))
        plt.plot(comp_info_data1['Date'], comp_info_data1['MACD'],'b',label = 'Moving Average Convergence/Divergence for {}'.format(option))
        plt.plot(comp_info_data1['Date'], comp_info_data1['Signal_line'],'g',label = 'Signal Line for {}'.format(option))
        plt.legend(loc='upper left')
        plt.ylabel(option)
        plt.xlabel('Date')
        plt.title('Moving Average Convergence/Divergence for {}'.format(option))
        plt.grid(True)
        plt.show()
        data_visualisation(comp_info_data, option)
                
    elif suboption_choice == '9':
        select_fact(comp_info_data)
    
    elif suboption_choice == '0':
        dm.close()

#handles invalid choice       
    else:
        print("\n\tInvalid input please try again")
        data_visualisation(comp_info_data, option)
            
def index_dataset(comp_info_data,option):
    """ Removes dates as index and set new index as days for the dataframe """
    
    comp_info_data1 = pd.DataFrame(comp_info_data[option])
    comp_info_data1['Days'] = range(0,len(comp_info_data1.index.values))
    comp_info_data1 = comp_info_data1.reset_index()
    return comp_info_data1
    
def raw_time_series(comp_info_data,option):
    """ Displays the raw time series of the fact selected by user """
    
    comp_info_data1 = index_dataset(comp_info_data,option)
    return comp_info_data1

def trend_lines(comp_info_data, option):
    """ Computes and returns the vaules for trend line along with raw-time series data  
    as numpy array for the fact selected by user """
    
    comp_info_data1 = index_dataset(comp_info_data,option)
    Date=pd.to_numeric(comp_info_data1['Date'])
    lr = stats.linregress(Date, comp_info_data1[option])    
    y = lr[1] + Date*lr[0]
    return comp_info_data1, y
    
def moving_average(comp_info_data,option,window1):
    """ Computes and displays moving average of the fact selected by user """
    
    comp_info_data1 = index_dataset(comp_info_data,option)
    comp_info_data1['Moving Average'] = comp_info_data1[option].rolling(window = window1).mean()
    #comp_info_data1['Moving Average'] = comp_info_data1[option].rolling(window = window1).mean()
    return comp_info_data1

def exponential_moving_average(comp_info_data,option,window):
    """ Computes and returns a dataframe with an additional column 'ema' i.e.
    exponential moving average for the fact selected by user """
    
    comp_info_data1 = index_dataset(comp_info_data,option)
    comp_info_data1['ema'] = comp_info_data1[option].ewm(ignore_na = False, adjust = True, min_periods = 0, span = window).mean()
    return comp_info_data1

def moving_average_converg_diverg(comp_info_data, option):
    """ Computes and returns a dataframe with additional columns such as fast, slow, 
    Moving average convergence/divergence, Signal line  for the fact selected by user """
    
    comp_info_data1 = index_dataset(comp_info_data,option)
    comp_info_data1['fast'] = comp_info_data1[option].ewm(ignore_na = False, adjust = True, min_periods = 0, span = 12).mean()
    comp_info_data1['slow'] = comp_info_data1[option].ewm(ignore_na = False, adjust = True, min_periods = 0, span = 26).mean()
    comp_info_data1['MACD'] = (comp_info_data1['fast'] - comp_info_data1['slow'])
    comp_info_data1['Signal_line'] = comp_info_data1['MACD'].ewm(ignore_na = False, adjust = True, min_periods = 0, span = 9).mean()
    return comp_info_data1