from requests import get
from bs4 import BeautifulSoup
from forcast import Forecast
from datetime import datetime
import os


def convert_to_tsql_datetime(date_string):
    # Define the format of the input date string
    input_format = "%H:%M (%Z) on %a %d %b %Y"
    
    # Parse the input string to a datetime object
    datetime_obj = datetime.strptime(date_string, input_format)
    
    # Convert the datetime object to a string in T-SQL DATETIME format
    tsql_datetime = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
    
    return tsql_datetime

def main():

    pw = os.getenv('PW')

    # URL of the shipping forecast page
    url = "https://www.metoffice.gov.uk/weather/specialist-forecasts/coast-and-sea/shipping-forecast"

    # Send a GET request to the URL
    response = get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the forecast sections
    forecast_sections = soup.find_all('section', class_='marine-card warning')

    # Extract each forecast area section and details, 
    for section in forecast_sections:
        
        region_name = section.find('h2').text.strip()
        warning_summary = section.find('dl', class_='warning-info').find('p').text.strip()
        issue_date = convert_to_tsql_datetime(section.find('time').text.strip())
        forecast_area = section.find('dl', class_='forecast-info')
        forecast_info = forecast_area.find_all('dd')
        
        #Add the elements about the forecast to an array, required as there are no class names to use on the <dd> elements
        forecast_info_array = [dd.text for dd in forecast_info]
        
        #assign the array elements to the correct variables
        wind = forecast_info_array[0]
        sea_state = forecast_info_array[1]
        weather = forecast_info_array[2]
        visibility = forecast_info_array[3]

        #create a new forecast object and print the details
        forcast = Forecast(region_name, warning_summary, issue_date, wind, sea_state, weather, visibility)
        forcast.saveToDatabse()

if __name__ == "__main__":
    main()



