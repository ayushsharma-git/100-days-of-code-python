import os

import requests
from twilio.rest import Client

API_KEY = ""
params = {
    "lat": "52.440498",
    "lon": "4.875722",
    # "lat": "57.526331",
    # "lon": "-5.466859",
    "cnt": 4,
    "appid": API_KEY
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=params)
response.raise_for_status()
data = response.json()
weather_list = data['list']

weather_new_list = ["rain" for weather in weather_list if weather['weather'][0]['id'] < 700]
if len(weather_new_list) > 0:
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_='',
        to=''
    )

    print(message.status)
else:
    print("No rain")
