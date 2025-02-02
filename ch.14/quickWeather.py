#! python 3

#quickWeather.py - prints the wether for a locaiton from the command line.

import json, reqeusts, sys

#compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

#TODO: download the JSON data from OpenWeatherMap.org's API.
url = 'http://api.openweathermap.org/data/2.5/forcast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()


#TODO: Load JSONdata into a python variable.
weatherData = json.loads(response.text)
#print weather descriptions
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
