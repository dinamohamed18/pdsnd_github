import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = {"chicago", "new york city", "washington"}
months = ("all", "january", "february", "march", "april", "may", "june")
days = ("all", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")

def get_filters():
    """
    Asks user to specify a City, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        chosen_city = input("\nChoose a city [chicago, new york city, washington] : \n")
        if chosen_city in cities :
            break;
    # TO DO: get user input for month (all, january, february, ... , june)
    while True :
        chosen_month = input("\nChoose a month [all, january, february, march, april, may, june] : \n")
        if chosen_month in months :
            break;
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        chosen_day = input("\nChoose a month [all, sunday, monday, tuesday, wednesday, thursday, friday, saturday] : \n")
        if chosen_day in days :
            break;

    print('-'*40)
    return chosen_city, chosen_month, chosen_day


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day Of Week'] = df['Start Time'].dt.weekday_name
    df['Start Hour'] = df['Start Time'].dt.hour

    if month != 'all':
        df = df[df['Month'] == (months.index(month))]

    if day != 'all' :
        df = df[df['Day Of Week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['Month'].mode()[0]
    print(f"\nMost Common Month : {most_common_month}")
    # TO DO: display the most common day of week
    most_common_day = df['Day Of Week'].mode()[0]
    print(f"\nMost Common Day Of Week : {most_common_day}")
    # TO DO: display the most common start hour
    most_common_start_hour = df['Start Hour'].mode()[0]
    print(f"\nMost Common Start Hour : {most_common_start_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_used_start_station = df['Start Station'].mode()[0]
    print(f'\nMost Common Start Station : {most_common_used_start_station}')

    # TO DO: display most commonly used end station
    most_common_used_end_station = df['End Station'].mode()[0]
    print(f'\nMost Common End Station : {most_common_used_end_station}')

    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    most_common_combination = df['Start To End'].mode()[0]
    print(f'\nMost Frequent Combination of Start and End Station : {most_common_combination}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    minute, second = divmod(total_travel_time, 60)
    hour, minute = divmod(minute, 60)
    print(f'\nTotal Travel Time : {total_travel_time}')
    print(f'{hour} hours, {minute} minutes and {second} seconds')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time = round(mean_travel_time)
    minute, second = divmod(mean_travel_time, 60)
    hour, minute = divmod(minute, 60)
    print(f'\nMean Travel Time : {mean_travel_time}')
    if hour != 0 :
        print(f'{hour} hours, {minute} minutes and {second} seconds')
    else:
        print(f'{minute} minutes and {second} seconds')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print(f'\nUser Type Counts : {user_type_counts}')

    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print(f'\nGender Counts : {gender_counts}')
    except:
        print('\nThis file does not contain gender and birthdate columns [maybe washington.csv] ')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year_of_birth = df['Birth Year'].min()
        most_recent_year_of_birth = df['Birth Year'].max()
        most_common_year_of_birth = df['Birth Year'].mode()[0]
        print(f'\nEarliest Year of Birth : {int(earliest_year_of_birth)}, Most Recent Year of Birth : {int(most_recent_year_of_birth)}, Most Common Year of Birth : {int(most_common_year_of_birth)}')
    except:
        print('\nThis file does not contain gender and birthdate columns [maybe washington.csv] ')
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
