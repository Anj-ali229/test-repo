import requests

key = '7e2a864edd287ed4e6bec267ef1ad9cf'

city = input("Enter city: ")

data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={key}")

if data.json()['cod'] == '404':
    print("City not found")
else:
    weather = data.json()['weather'][0]['main']
    temp = round(data.json()['main']['temp'])

    print(f"The weather in {city} is: {weather}")
    print(f"The temperature in {city} is: {temp}^C")
