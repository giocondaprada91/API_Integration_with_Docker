from requests import get
import sys
import os
import argparse

if __name__ == '__main__':
    # Create the parser
    parser = argparse.ArgumentParser(description='Retrieve holiday information using the AbstractAPI Holidays API.')
    
    # Add arguments
    parser.add_argument('--country', type=str, help='The country code (e.g., US)', required=True)
    parser.add_argument('--year', type=str, help='The year (e.g., 2020)', required=True)
    parser.add_argument('--month', type=str, help='The month (e.g., 12)', required=True)
    parser.add_argument('--day', type=str, help='The day (e.g., 25)', required=True)
    
    # Parse the arguments
    args = parser.parse_args(sys.argv[1:])
    
    # Access the parsed arguments
    country = args.country
    year = args.year
    month = args.month
    day = args.day
    
    # Get the API key from the environment variable
    api_key = os.getenv('API_KEY')

    # Define the base URL
    base_url = "https://holidays.abstractapi.com/v1/"
    
    # Create a dictionary for the query parameters
    params = {
        'api_key': api_key,
        'country': country,
        'year': year,
        'month': month,
        'day': day
    }
    
    # Make the API request using the parameters
    response = get(base_url, params=params)
    holidays = response.json()

    if holidays:
        for holiday in holidays:
            print("\nHoliday Details:")
            print(f"Name: {holiday['name']}")
            print(f"Local Name: {holiday.get('name_local', 'N/A')}")
            print(f"Country: {holiday['country']}")
            print(f"Type: {holiday['type']}")
            print(f"Date: {holiday['date']}")
            print(f"Year: {holiday['date_year']}")
            print(f"Month: {holiday['date_month']}")
            print(f"Day: {holiday['date_day']}")
            print(f"Weekday: {holiday['week_day']}")
            
    else:
        print("No holidays found for the specified date.")




    