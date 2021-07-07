#*********************************************#
# Name: Abdulhay Mulla - Date 2021-05-27      #
# Programe Name : Explore US Bikeshare Data   #
# Description : A filter method to show number#
# of statistics DATA for 3 main DATA sets in  #
# Excel Sheets contating large amount of DATA #
#*********************************************#

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new_york_city': 'new_york_city.csv',
              'washington': 'washington.csv' }


#to start filter the tables based on the giving information
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')

#to choose one of the 3 Cities
    while True:
        city= input('Please write the display data for chicago, new york city or washington?').lower()
        cities = ['chicago','new york city','washington']
        if city not in cities:
            print('Please Choose the city from above')

        else:
            break

#to choose the Month
    while True:
        month = input("Please choose any of : january', 'february', 'march', 'april', 'may', 'june','all'?").lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june','all']
        if month != 'all' and month not in months:
            print('Please choose the month from the above')
        else:
            break

#to choose a day
    while True:
        day = input("Please choose any of : 'sunday','monday','tuesday','wednesday','thursday','friday','saturday','all'?").lower()
        days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']
        if day !='all' and day not in days:
            print('Please choose a day from the above')
        else:
            break


    print('-'*40)
    return city, month, day


#Start load the required DATA file
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # finding the required city DATA and uplaode it
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # create the new column
        df = df[df['month'] == month]

    # filter by day
    if day != 'all':
        # create the new column
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    Common_Month = df['month'].mode()[0]

    print('Most Common Month:', Common_Month)

    # display the most common day of week
    Common_Day_Of_Week = df['day_of_week'].mode()[0]

    print('Most Day Of The Week:', Common_Day_Of_Week)

    # display the most common start hour
    Common_Start_Hour = df['hour'].mode()[0]

    print('Most Common Starting Hour:', Common_Start_Hour)

    #display the overall processing time in seconds
    print("\nTime for this took",(time.time() - start_time), "seconds.")
    print('-'*40)

#Prepare statistics
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    #Prepare reading Time
    start_time = time.time()

    # display most commonly used start station
    Common_Start_Station = df['Start Station'].mode()[0]

    print('Most Start Station:', Common_Start_Station)

    # display most commonly used end station
    Common_End_Station = df['End Station'].mode()[0]

    print('Most End Station:', Common_End_Station)

    # display most frequent combination of start station and end station trip
    group_field=df.groupby(['Start Station','End Station'])
    Most_Frequent_Combination_Station = group_field.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of Start Station and End Station trip:\n', Most_Frequent_Combination_Station)

    #display the overall processing time in seconds
    print("\nTime for this took",(time.time() - start_time), "seconds.")
    print('-'*40)

#prepare for trip duration statistics
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    #Prepare reading Time
    start_time = time.time()

    # display total travel time
    Total_Travel_Time = df['Trip Duration'].sum()

    print('Total Travel Time:', Total_Travel_Time)

    # display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()

    print('Mean Travel Time:', Mean_Travel_Time)

    #display the overall processing time in seconds
    print("\nTime for this took",(time.time() - start_time), "seconds.")
    print('-'*40)


#Prepare User statistics
def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    #Prepare reading time (converting)
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Type Stats:')
    print(df['User Type'].value_counts())
    #Because it's not giving
    if city != 'washington':
        # Display counts of gender
        print('Gender Stats:')
        print(df['Gender'].value_counts())
        # Display earliest, most recent, and most common year of birth
        print('Birth Year Stats:')
        Most_Common_Year = df['Birth Year'].mode()[0]
        print('Most Common Year:',Most_Common_Year)
        Most_Recent_Year = df['Birth Year'].max()
        print('Most Recent Year:',Most_Recent_Year)
        Earliest_Year = df['Birth Year'].min()
        print('Earliest Year:',Earliest_Year)
    #display the overall processing time in seconds
    print("\nTime for this took",(time.time() - start_time), "seconds.")
    print('-'*40)


def display_raw_data(df):
    """ Your docstring here """
    i = 0
    # TO DO: convert the user input to lower case using lower() function
    raw = input("\nwould you like to display 5 rows of current selection?\n").lower()
    pd.set_option('display.max_columns',200)

    while True:
        if raw == 'no':
            break
        elif raw == 'yes':
            # TO DO: appropriately subset/slice your dataframe to display next five rows
            print(df[i:i+5])
            raw = input("\nWould you like to display next 5 rows?. Please enter only 'yes' or 'no'\n") # TO                 DO: convert the user input to lower case using lower() function
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
