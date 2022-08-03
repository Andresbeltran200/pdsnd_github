import time
import pandas as pd
import numpy as np

#Update of datesets

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
          city = input("\n Please, write a city name ('New York City', 'Chicago', 'Washington')\n")
          if city not in ('New York City', 'Chicago', 'Washington'):
            print("Sorry, I didn't find the city")
            continue
          else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
          month = input("\n Please, write a month or all (January', 'February', 'March', 'April', 'May', 'June')\n")
          if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
            print("Sorry, I didn't find the month")
            continue
          else:
            break
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
          day = input("\n Please, write a day of week or all( Monday, Tuesday, ... Sunday\n")
          if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
            print("Sorry, I didn't find the day")
            continue
          else:
            break
    #print('-'*40)
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
    City = city.lower()
    df_city = pd.read_csv(City+'.csv')
    df = df_city.copy()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

   
    if month != 'all':
        dic_month ={'January': 1 , 'February': 2, 'March' : 3, 'April' : 4, 'May' : 5, 'June' : 6}
        month2 = dic_month[month]
        df = df[df['month'] == month2]

    return df
    



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    commonly_month = df['month'].mode()[0]
    print('Most common month',commonly_month)

    # TO DO: display the most common day of week
    commonly_day = df['day_of_week'].mode()[0]
    print('Most common day of week',commonly_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common start hour',common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('Most commonly used start station',start_station)
    # TO DO: display most commonly used end station
    
    end_station = df['End Station'].value_counts().idxmax()
    print('Most commonly used End station',end_station)
    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] =  df['Start Station'] + df['End Station'] 
    combination = df['combination'].value_counts().idxmax()
    print('most frequent combination of start station and end station trip',combination)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('Total travel time ', total_travel_time)
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time ', mean_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User types', user_types) 

    # TO DO: Display counts of gender
    gender_types = df['Gender'].value_counts()
    print('counts of gender', gender_types)

    # TO DO: Display earliest, most recent, and most common year of birth

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
