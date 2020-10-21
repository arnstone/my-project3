import time
import pandas as pd


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
    print('='*65)
    print('Hello! Welcome to explore some US bikeshare data!')
    print('='*65)
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA.keys():
        print("\nPlease enter city (chicago, new york city or washington):")
        #Taking user input and converting into lower to standardize them
        city = input().lower()

        if city not in CITY_DATA.keys():
            print("\nInvalid input. Please try again in the accepted input format.")

    # get user input for month (all, january, february, ... , june)
    #Creating a dictionary to store all the months including the 'all' option
    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in MONTH_DATA.keys():
        print("\nPlease enter the month (between January and June) or all, for which you're seeking data:")
        month = input().lower()

        if month not in MONTH_DATA.keys():
            print("\nInvalid input. Please try again in the accepted input format.")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    #Creating a list to store all the days including the 'all' option
    DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in DAY_DATA:
        print("\nPlease enter a day in the week or all, for which you're seeking data:")
        day = input().lower()

        if day not in DAY_DATA:
            print("\nInvalid input. Please try again in one of the accepted input formats.")

    print(f"\nYou have chosen: city: {city.upper()}, month/s: {month.upper()} and day/s: {day.upper()}.")
    print('-'*65)

    #Returning the city, month and day selections
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
    # load data file into a dataframe
    print("\nLoading data...")
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower())


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month,:]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day,:]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #Uses mode method to find the most popular month
    popular_month = df['month'].mode()[0]

    print(f"Most Popular Month: {popular_month}")

    #Uses mode method to find the most popular day
    popular_day = df['day_of_week'].mode()[0]

    print(f"\nMost Popular Day  : {popular_day}")

    #Extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    #Uses mode method to find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print(f"\nMost Popular Start Hour: {popular_hour}")

    #Prints the time taken to perform the calculation
    #You will find this in all the functions involving any calculation
    #throughout this program
    print("\nThis took %s seconds." % round((time.time() - start_time), ndigits=6))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station: " + common_start_station)

    # Display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station  : " + common_end_station)

    # Display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station: " + str(frequent_combination.split("||")))

    print("\nThis took %s seconds." % round((time.time() - start_time), ndigits=6))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    sum_seconds = total_travel_time%60
    sum_minutes = total_travel_time//60%60
    sum_hours = total_travel_time//3600%60
    sum_days = total_travel_time//24//3600
    print('Passengers travelled a total of {} days, {} hours, {} minutes and {} seconds'.format(sum_days, sum_hours, sum_minutes, round(sum_seconds, ndigits=(0))))

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    sum_seconds = mean_travel_time%60
    sum_minutes = mean_travel_time//60%60
    sum_hours = mean_travel_time//3600%60
    sum_days = mean_travel_time//24//3600
    print('The mean travel times for passengers are {} days, {} hours, {} minutes and {} seconds'.format(sum_days, sum_hours, sum_minutes, round(sum_seconds, ndigits=(0))))

    print("\nThis took %s seconds." % round((time.time() - start_time), ndigits=6))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types from the given data is: \n" + str(user_types))

    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("\nThe count of Gender from the given data is: \n" + str(gender))
    except:
        print("\nThere is no 'Gender' column in this file.")

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
        print('\nEarliest birth from the given data is   : {}'.format(int(earliest_birth)))
        print('Most recent birth from the given data is: {}'.format(int(most_recent_birth)))
        print('Most common birth from the given data is: {}\n'.format(int(most_common_birth)))
    except:
        print("There is no birth year details in this file.")

    print("\nThis took %s seconds." % round((time.time() - start_time), ndigits=6))
    print('-'*40)


def display_five_rows_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nWould you like to view next five rows? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next += 5
        print(df.iloc[next:next+5])


def main():
     while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        while True:
            view_raw_data = input('\nWould you like to view first five row of raw data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
            display_five_rows_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
