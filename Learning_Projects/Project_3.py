# This is to develop a basic weather application that can provide the current weather conditions for a given city.

import requests
api_key = 'fdf228f3014d303f8655c45b05cd8773'

# Add location of city you want the weather for. You need information from the user - input
city = input("Enter the city name: ")
state = input("Enter the state code (Example, CA for California or NJ for New Jersey: ")
url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{state},US&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    temp_f = (temp - 273.15) * 9 / 5 + 32
    desc = data['weather'][0]['description']
    print(f'Temperature: {temp_f:.2f} °F')
    print(f'Description: {desc}')
else:
    print('Error fetching weather data')