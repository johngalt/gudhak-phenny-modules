import urllib
from xml.etree import ElementTree as ET

def weather(phenny, input):
	if not input:
		phenny.say('[Weather] Please enter a search term..')
	else:
		html = urllib.urlopen('http://api.wunderground.com/auto/wui/geo/WXCurrentObXML/index.xml?query=' + input)
		tree = ET.parse(html)
		html.close()
		
		location = tree.findtext("observation_location/full")
		country = tree.findtext("observation_location/country")
		forcast = tree.findtext("weather")
		temp = tree.findtext("temperature_string")
		humidity = tree.findtext("relative_humidity")
		wind = tree.findtext("wind_string")
		heatindex = tree.findtext("heat_index_string")
		windchill = tree.findtext("windchill_string")
		
		if forcast:
			phenny.say('[Weather] \002Location:\002 ' + location + ' (' + country + ') | \002Currently:\002 ' \
			+ temp + ' (' + forcast + ') | \002Humidity:\002 ' + humidity + ' | \002Wind:\002 ' + wind \
			+ ' | \002Heat Index:\002 '	+ heatindex + ' | \002Wind Chill:\002 ' + windchill)
		else:
			phenny.say('[Weather] None found.')

weather.commands = ['weather', 'we']
weather.example = ".weather <zip>"

