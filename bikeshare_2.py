import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please Enter the city.. ")
    city = city.lower()
    city = city.strip()
    
    while city != 'chicago' and city!= 'new york city' and city != 'washington':
        city = input("Invlid Input!! Please Enter the city again.. you may choose from 'chicago' or 'new york city' or 'washington'  ")
        city = city.lower()
        city = city.strip()


    # get user input for month (all, january, february, ... , june)
    month_list = ["all", "january", "february" , "march","april","may", "june"]
    month = input("Please Enter the month.. ")
    month = month.lower()
    month = month.strip()
    while month not in month_list :

        month = input("Invlid Input!! Please Enter the month.. month should be as this format'all, january, february, ... , june'")
        month = month.lower()
        month = month.strip()
 


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ["all", "monday", "tuesday" , "wednesday","thursday","friday", "saturday", "sunday"]
    day = input("Please Enter the day.. ")
    day = day.lower()
    day = day.strip()
    while day not in day_list :

        day = input("Invlid Input!! Please Enter the day.. month should be as this format (all, monday, tuesday, ... sunday) ")

        day = day.lower()
        day = day.strip()


    print('-'*40)
    return city, month, day


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
    city = city.replace(" ", "_")
    df = pd.read_csv(city+".csv")
    pd.set_option('display.max_columns', None)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    if month != 'all':
        months_list  = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months_list.index(month) + 1
        df = df[df['Start Time'].dt.month == month]
        
    
    if day != 'all':
        df['day_of_week'] = df['Start Time'].dt.day_name()
        df = df[df['day_of_week'] == day.title()] 

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['month'] = df['Start Time'].dt.month
    most_common_month = df['month'].mode()[0]
    months_list  = ['january', 'february', 'march', 'april', 'may', 'june']
    most_common_month = months_list[most_common_month - 1 ]
    print("The most common month is the month of:  " + most_common_month)
    


    # display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week is the day of : " + most_common_day_of_week )


    # display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['start_hour'].mode()[0]
    
    print("The most common start hour is : " + str(most_common_start_hour) )




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is :  " + most_commonly_used_start_station )


    # display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is :  " + most_commonly_used_end_station )


    # display most frequent combination of start station and end station trip
    df['combination_of_start_station_and_end_station'] = "From " + df['Start Station'] + " To " + df['End Station']
    combination_of_start_station_and_end_station = df['combination_of_start_station_and_end_station'].mode()[0]
    print("The most frequent combination of start station and end station trip is : " + combination_of_start_station_and_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time: " + str(total_travel_time) )
 


    # display mean travel time
    rows = len(df.axes[0])
    
    mean_travel_time = df['Trip Duration'].sum() / rows
    print("Mean travel time: "+ str(mean_travel_time) )
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User Types are: ")
    print(user_types)


    # Display counts of gender
 
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print("Gender are : ")
        print(gender)
    else:
        print("No gender data available for this city.. ")




    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
       
        most_common_year_of_birth = df['Birth Year'].mode()[0]
        print("Most common year of birth is : " + str(int(most_common_year_of_birth)))
        most_recent = df['Birth Year'].max()
        print("Most recent year is : " + str(int(most_recent)))
        earliest = df['Birth Year'].min()
        print("Earliest year is : " + str(int(earliest)))  

    else:
        print("No year of birth data available for this city.. ")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
# def useful_data(df):
#     print(df.head())
#     print(df.columns)
#     print(df.describe())
#     print(df.info())

def display_rows(df):

  
    x = input("Do you want to see 5 lines of raw data? , print 'yes' or 'no' ")
    x = x.strip()
    x = x.lower()
    if x == 'no':
        print('Thanks..we will proceed with data analysis')
       

    while x != 'yes' and x != 'no':
        print("Your input was invlid, please print 'yes' or 'no' ")
        x= input("Do you want to see 5 lines of raw data? , print 'yes' or 'no' ")
        x = x.strip()
        x = x.lower()
        if x == 'no':
            print('Thanks..we will proceed with data analysis')
            break
        
     
    counter1=0
    counter2=4
    while x == 'yes':
       
        print(df.iloc[counter1:counter2+1]) 
        counter1 += 5
        counter2 += 5

        x = input("Do you want to see more 5 lines of raw data? , print 'yes' or 'no' ")
        x = x.strip()
        x = x.lower()
        if x == 'no':
                print('Thanks..we will proceed with data analysis')
                break
        while x != 'yes' and x != 'no':
            print("Your input was invlid, please print 'yes' or 'no' ")
          
            x = input("Do you want to see more 5 lines of raw data? , print 'yes' or 'no' ")
            x = x.strip()
            x = x.lower()

            if x == 'no':
                print('Thanks..we will proceed with data analysis')
                break



    



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_rows(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        # useful_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
  
	main()
