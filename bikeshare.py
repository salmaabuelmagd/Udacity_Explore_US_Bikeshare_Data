import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ["all","january","february","march","april","may","june"]
days = ["all","monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

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
        city = input("Would you like to see data for one of these cities (chicago , new york city or washington)?").lower()
        if city in CITY_DATA:
            break
        else:
            print("Error")
     # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("which month would you like to see data for (january,febraury,march,april,may,june or all?").lower()
        if month in months:
            break
        else:
            print("Error")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("which day would you like to see data for (monday,tuesday,wednesday,thursday,friday,saturday,sunday or all?").lower()
        if day in days:
            break
        else:
            print("Error")
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
    df = pd.read_csv(CITY_DATA[city]) #to read data for the city the user chose into a data frame in panda
    df["Start Time"] = pd.to_datetime(df["Start Time"]) #to convert Start Time to Date time type
    df["month"] = df["Start Time"].dt.month #extract month from Start Time
    df["day_of_week"] = df["Start Time"].dt.weekday_name #extraxt day from Start Time
    df["hour"] = df["Start Time"].dt.hour # extract hour from Start Time
    if month != "all":
        months = ["january" , "february" , "march" , "april" , "may" , "june"] # months list after removing all from it 
        month = months.index(month) + 1  #using indexing to get number of the month 
        df = df[df["month"] == month] # create new dataframe to filter by month
    if day != "all":
        df = df[df["day_of_week"] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    most_common_month = df["month"].mode()[0]
    print("the most common month is: {}".format(most_common_month))
    # TO DO: display the most common day of week
    most_common_day_of_week = df["day_of_week"].mode()[0]
    print("the most common day of week is: {}".format(most_common_day_of_week))
    # TO DO: display the most common start hour
    most_common_start_hour = df["hour"].mode()[0]
    print("the most common start hour is: {}".format(most_common_start_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_used_start_station = df["Start Station"].mode()[0]
    print("most commonly used start station is: {}".format(commonly_used_start_station))
    # TO DO: display most commonly used end station
    commonly_used_end_station = df["End Station"].mode()[0]
    print("most commonly used end station is: {}".format(commonly_used_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df["cmob_start_end"] = df["Start Station"] + " - " + df["End Station"]
    route = df["cmob_start_end"].mode()[0]
    print("the most frequent combination of start station and end station trip is: {}".format(route))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("the total travel time is: {}".format(total_travel_time))
    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("the mean travel time is: {}".format(mean_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    print("the counts of user types is: {}".format(user_types))
    # TO DO: Display counts of gender
    try:
        gender = df["Gender"].value_counts()
        print("the counts of gender is: {}".format(gender))
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year_of_birth = df["Birth Year"].min()
        print("the earliest year of birth is: {}".format(earliest_year_of_birth))
        most_recent_year_of_birth = df["Birth Year"].max()
        print("the most recent year of birth is: {}".format(most_recent_year_of_birth)) 
        most_common_year_of_birth = df["Birth Year"].mode()[0]
        print("the most common year of birth is: {}".format(most_common_year_of_birth))
    except:
            print("there aren't any gender nor birth year data for this city")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):
    """Displays 5 rows of data from the csv file for the selected city."""
    answer = input("would you like to see 5 rows of raw data please answer yes or no?")
    start = 0
    while True:
        if answer == "no":
            break
        else:
            print(df.iloc[start:start + 5])
            start += 5
            answer = input("would you like to see more 5 rows of raw data?")
        
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
