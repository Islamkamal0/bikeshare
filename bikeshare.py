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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city data would you like to explore?(Please input one of these three cities:'chicago', 'new york city', 'washington')")
        city = city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Please enter a valid city.")    

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:    
        month = input("Which moth would you like to explore?(Please enter one of these: 'january', 'february', 'march', 'april', 'may', 'june', 'all')")
        month = month.lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("Please enter a valid month or 'all' to choose all the months.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day of the week would you like to explore?(Please enter on of the following: 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all')")
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("Please enter a valid day or 'all' to choose all the days of the week.")

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
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = df['Start Time'].astype('datetime64')

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    # TO DO: display the most common month
    print("The most common month is " + str(months[df['month'].value_counts().idxmax()-1]))

    # TO DO: display the most common day of week
    print("The most common day of the week is " + str(df['day_of_week'].value_counts().idxmax()))

    # TO DO: display the most common start hour
    print("The most common start hour is " + str(df['Start Time'].dt.hour.value_counts().idxmax()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common start station is " + str(df['Start Station'].value_counts().idxmax()))

    # TO DO: display most commonly used end station
    print("The most common end station is " + str(df['End Station'].value_counts().idxmax()))
    

    # TO DO: display most frequent combination of start station and end station trip
    df['comp'] = df['Start Station'] + ' and ' + df['End Station']
    print("The most common compination of start station and end station is " + str(df['comp'].value_counts().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is " + str(df['Trip Duration'].sum()))


    # TO DO: display mean travel time
    print("The mean travel time is " + str(df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
        # TO DO: Display counts of user types
    print("The user types count is\n" + str(df['User Type'].value_counts()));

    if 'Gender' in df.columns:
        # TO DO: Display counts of gender
        print("The gender count is\n" + str(df['Gender'].value_counts()));
    else:
        print("There is no Gender data in this city.")
    if 'Birth Year' in df.columns:
        # TO DO: Display earliest, most recent, and most common year of birth
        print("The earliest year of birth is " + str(df['Birth Year'].min()))
        print("The most recent year of birth is " + str(df['Birth Year'].max()))
        print("The most common year of birth is " + str(df['Birth Year'].value_counts().idxmax()))
    else:
        print("There is no Birth Year data in this city.")

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
        count = 0
        while True:
            inp = input('\nWould you like to see some raw data? Enter "yes" or "no".\n')
            if inp.lower() == 'yes':
                print(df[count:count+10])
                count+=10
            elif inp.lower() != 'no':
                print("Please enter a valid input.")
            else:
                break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()