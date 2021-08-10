import requests, json
from json_tools import dict_to_json, json_to_dict
from secrets import lat, lon, api_key

url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}&units=metric'


def get_48_hour_weather_data():

    response = requests.get(url)
    weather_data = json.loads(response.text)

    # Save the data to a JSON file
    dict_to_json(weather_data, 'test-JSON.json')

    return weather_data


def check_for_rain(forecast_hours, weather_data):

    hourly_list = weather_data['hourly']

    # Only view the next x hours in the forecast
    for i in range(len(hourly_list) - forecast_hours):
        hourly_list.pop()

    for entry in hourly_list:
        weather = (entry['weather'][0]['main']).lower()
        description = (entry['weather'][0]['description']).lower()

        if 'rain' in weather or 'rain' in description or 'storm' in weather or 'storm' in description:
            return True

    return False


# This function is in-dev
def get_datetime_from_weather_data(forecast_hours, weather_data):

    hourly_list = weather_data['hourly']
    dt_hours = list()

    print(hourly_list)

    # Only view the next x hours in the forecast
    for i in range(len(hourly_list) - forecast_hours):
        hourly_list.pop()

    for entry in hourly_list:
        dt = entry
        print(dt)
        input()


if __name__ == '__main__':

    get_new_data = False

    if get_new_data:
        weather_info = get_48_hour_weather_data()
    else:
        weather_info = json_to_dict('test-JSON.json')

    rain = check_for_rain(6, weather_info)

    if rain:
        print('Rain is in the forecast.')
    else:
        print('Rain is not in the forecast.')
