Created 02.10.2020

Python Script to Explore US Bikeshare Data

Description
This project Uses Python to understand U.S. bikeshare data.
The script calculates statistics and build an interactive environment where
the user can choose and filter for a dataset to analyze.

You can run the script using a Python integrated development environment (IDE) such as Spyder. To install Spyder, you will need to download the Anaconda installer.
This script is written in Python 3, so you will need the Python 3.x version of the installer. After downloading and installing Anaconda, you will find the Spyder IDE by opening Anaconda Navigator.

Datasets
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:
* Start Time (e.g., 2017-01-01 00:07:57)
* End Time (e.g., 2017-01-01 00:20:53)
* Trip Duration (in seconds - e.g., 776)
* Start Station (e.g., Broadway & Barry Ave)
* End Station (e.g., Sedgwick St & North Ave)
* User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
* Gender
* Birth Year

Statistics Computed
The code is written to provide the following information:

1. Popular times of travel (i.e., occurs most often in the start time)
* most common month
* most common day of week
* most common hour of day

2. Popular stations and trip
* most common start station
* most common end station
* most common trip from start to end (i.e., most frequent combination of start station and end station)

3. Trip duration
* total travel time
* average travel time

4. User info
* counts of each user type
* counts of each gender (only available for Chicago and NYC)
* earliest, most recent, most common year of birth (only available for Chicago and NYC)

5. Display raw data in five rows step
*  In the end you can choose to display raw data in steps of five rows
