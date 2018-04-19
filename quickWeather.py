#! /usr/bin/python3
# quickWeather.py - prints the weather for a location from commandline

import sys, requests, json, pprint

# get location from commandline
if len(sys.argv) < 2:
    print('Give me some location for weather')
    sys.exit()
location = ' '.join(sys.argv[1:])

'''
OpenWeatherMap.org provides real-time weather information in JSON format.
http://api.openweathermap.org/data/2.5/forecast/daily?q=<Location>&cnt=3,
where <Location> is the name of the city whose weather you want.
'''

# download data from the api
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=71fd55e8aeeccbdbb9b1e55b4eb7eb67' % (location)
res = requests.get(url)
res.raise_for_status

# load json data into python variable
weatherData = json.loads(res.text)
pprint.pprint(weatherData)

# print weather description
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
