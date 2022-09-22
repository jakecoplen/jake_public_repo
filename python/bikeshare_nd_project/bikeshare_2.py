from re import T
import time
import pandas as pd
import numpy as np
from mimetypes import common_types
from statistics import mode

# list of city names
# if this list grows and analysis is expanded, add new city names and file names
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# if new data is present for months beyond June, then this list will need to be expanded to include all months
months = ['january','february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december' ]

days_of_week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    while True:
        try:
            # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
            city = str(input('Please enter a city to explore (Chicago, New York City, or Washington).\n')).lower()
            if city in CITY_DATA:
                print('\nYou are exploring bikeshare data from {}\n'.format(city.title()))
                break
            else:
                print('\n', city.title(), 'is NOT an acceptable city\n')
                continue
        except:
            print('\nError: Please enter either either "Chicago", "New York City", or "Washington"\n')

    while True:
        # get user input for month (all, january, february, ... , june)
        try:
            month = str(input('\nPlease enter a month name from January to June to analyze, or enter "all" to include all months.\nData only available for first 6 months of the year (i.e. January - June) \n')).lower()
            if month in months:
                print('\nYou are exploring bikeshare data from {} during {}\n'.format(city.title(), month.title()))
                break
            elif month == 'all':
                print('\nYou are exploring bikeshare data from {} for all months.\n'.format(city.title()))
                break
            else:
                print(month.title(), ' is NOT a valid month. Please check your spelling. \n')
                continue
        except:
            print('\nPlease enter a full month name from January to June, or enter "all" to explore all months.\n')

    while True:
        try:
            # get user input for day of week (all, monday, tuesday, ... sunday)
            day = str(input('\nPlease enter a day of the week to analyze, or enter "all" to include all days \n')).lower()
            if day in days_of_week:
                if month == 'all':
                    print('\nYou are exploring bikeshare data from {} during all months and on {}\'s\n'.format(city.title(), day.title()))
                    break
                elif month != 'all':
                    print('\nYou are exploring bikeshare data from {} during {} on {}\'s\n'.format(city.title(), month.title(), day.title()))
                    break
            elif day == 'all':
                if month == 'all':
                    print('\nYou are exploring bikeshare data from {} during all months and all days of the week\n'.format(city.title()))
                    break
                elif month != 'all':
                    print('\nYou are exploring bikeshare data from {} during {} on all days of the week\n'.format(city.title(), month.title()))
                    break
            else:
                print(day.title(), ' is NOT a valid day of the week. Please check your spelling. \n')
                continue
        except:
            print('\nPlease enter a valid day of the week.\n')
            
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
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time and End time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week (day name) from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['month_name'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    df['start & end station'] = 'Start - ' + df['Start Station'] + ' || End - ' + df['End Station']
    # filter by month if applicable
    if month != 'all':
        # created list of months and use index position to get corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_int = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month_int]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    df.rename(columns={ df.columns[0]: 'id'}, inplace = True)
    return df


def time_stats(df, month, day):
    """
    Displays statistics on the most frequent times of travel
    ."""

    pause = input('Press any key to see statistics on total travel time and the most frequent times of travel.')
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month_num = mode(df['month'])
    month_counts = df['month'].value_counts()
    common_month = months[common_month_num - 1].title()

    if month == 'all':
        print('\nThe most common month, based on number of trips, was: {} with {} total trips\n'.format(common_month, month_counts[common_month_num]))
    elif month != 'all':
        print('\nYour current dataset is only filtered for {}, therefore the most common month will be {}\n'.format(month.title(), common_month.title()))


    # display the most common day of week
    common_day_of_week = mode(df['day_of_week'])
    day_counts = df['day_of_week'].value_counts()

    if day == 'all':
        print('\nThe most common day of the week during {} was, based on number of trips: {} with {} total trips\n'.format(common_month, common_day_of_week, day_counts[common_day_of_week]))
    elif day != 'all':
        print('\nYour current dataset is only filtered for {}\'s, therefore the most common day will be {}\n'.format(day.title(), common_day_of_week.title()))


    # display the most common start hour
    common_hour = mode(df['hour'])
    hour_counts = df['hour'].value_counts()

    if common_hour < 12:
        print('\nThe most common hour for travel was {}A.M.\n'.format(common_hour, hour_counts[common_hour]))
    elif common_hour == 12:
        print('\nThe most common hour for travel was {} noon\n'.format(common_hour, hour_counts[common_hour]))
    else:
        common_hour_pm = common_hour - 12
        print('\nThe most common hour for travel was {}P.M.\n'.format(common_hour_pm, hour_counts[common_hour]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    """

    # to create a better user experience, I created this input command
    # this way a user can see small sets of data at a time, rather than all at once
    pause = input('Press any key to see statistics on the most popular stations and trip.')
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    busiest_start_station = mode(df['Start Station'])
    station_start_counts = df['Start Station'].value_counts()
    print('\nThe most commonly used Start Station was {}, with {} uses.\n'.format(busiest_start_station, station_start_counts[0]))

    # display most commonly used end station
    busiest_end_station = mode(df['End Station'])
    station_end_counts = df['End Station'].value_counts()
    print('\nThe most commonly used End Station was {}, with {} uses.\n'.format(busiest_end_station, station_end_counts[0]))

    # display most frequent combination of start station and end station trip
    most_common_start_end = mode(df['start & end station'])
    start_end_station_counts = df['start & end station'].value_counts()

    print('\nThe most common combination of start & end stations was: {} with {} rides starting and ending at the respective stations\n'.format(most_common_start_end, start_end_station_counts[most_common_start_end]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    pause = input('Press any key to see statistics on the total and average trip durations.')
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time_sec = np.sum(df['Trip Duration'])
    total_travel_time_min = total_travel_time_sec/60
    total_travel_time_hour = total_travel_time_min/60
    total_travel_time_day = total_travel_time_hour/24
    print('Total travel time for all trips is {} days, which represents {} total hours of travel\n'.format(round(total_travel_time_day, 1), round(total_travel_time_hour, 1)))

    # display mean travel time
    avg_travel_time_sec = np.average(df['Trip Duration'])
    avg_travel_time_min = avg_travel_time_sec/60
    avg_travel_time_hour = avg_travel_time_min/60
    print('The average duration of a trip is {} minutes (or {} hours)\n'.format(round(avg_travel_time_min, 1), round(avg_travel_time_hour, 2)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    pause = input('Press any key to see statistics on bikeshare users.')
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    percent = '%'
    print('User Type breakout by number of rides:')
    print(user_type_counts)
    print('\nMeaning {}{} of trips came from subscribers\n'.format(round((user_type_counts[0]/(user_type_counts[0]+user_type_counts[1])*100), 2), percent))

    if city.lower() != 'washington':
        # Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print('\nGender breakout by number of rides:')
        print(gender_counts)
        print('\nMeaning {}{} of trips came from male riders\n'.format(round((gender_counts[0]/(gender_counts[0]+gender_counts[1])*100), 2), percent))

        # Display earliest, most recent, and most common year of birth
        most_recent_birth_year = int(df['Birth Year'].max())
        earliest_birth_year = int(df['Birth Year'].min())
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        birth_year_counts = df['Birth Year'].value_counts()

        print('The most common birth year for riders in {} is {}, with {} trips from riders born in {}\n'.format(city.title(), most_common_birth_year, birth_year_counts[most_common_birth_year], most_common_birth_year ))
        print('The earliest birth year of a rider in {} is {}, with {} trips from riders born in {}\n'.format(city.title(), earliest_birth_year, birth_year_counts[earliest_birth_year], earliest_birth_year))
        print('The most recent birth year of a rider in {} is {}, with {} trips from riders born in {}\n'.format(city.title(), most_recent_birth_year, birth_year_counts[most_recent_birth_year], most_recent_birth_year))

    else:
        print('Gender and birth year data is not available for the city of Washington.\n')
        print('If you would like to explore this data, please select "New York City" or "Chicago" as the city to explore at the beginning of this program.\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """
    This function takes user input to allow the user to see rows of raw data until they are satisified or they reach the end of the file
    """
    while True:
        try:
            see_data = input('Would you like to see raw data? (yes or no)\n')
            if see_data.lower() == 'yes':
                i = 0
                while i <= len(df):
                    print(df.iloc[i:i+5,:]) 
                    i += 5
                    if (i+1) >= len(df):
                        print('You\'ve reached the end of the file. There is no more raw data to view.')
                        break
                    else:
                        while True:
                            try:
                                more_data = input('Would you like to see 5 more rows of data? (yes or no)\n')
                                if more_data.lower() == 'no':
                                    i = len(df) + 1
                                    break
                                elif more_data.lower() == 'yes':
                                    break
                                else:
                                    print('Error: that is not a valid input')
                            except:
                                print('Please enter "Yes" or "No"')     
                break
            elif see_data.lower() == 'no':
                break
            else:
                print('Error: Input arguement must be "yes" or "no"\n')
                continue
        except:
            print('Please enter "yes" or "no" to continue\n')
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        while True:
            try:        
                restart = input('\nWould you like to restart? Enter yes or no.\n')
                if restart.lower() == 'no':
                    response = 'no'
                    break
                elif restart.lower() == 'yes':
                    response = 'yes'
                    break
                else:
                    print('Invalid input: please enter "yes" or "no"')
            except:
                print('Please enter "yes" or "no"')

        if response == 'yes':
            continue
        elif response == 'no':
            break


if __name__ == "__main__":
	main()
