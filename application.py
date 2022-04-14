from random import randrange
from flask import Flask

# function to generate a random temperature given a location
def get_temp(location):
    temperature = randrange(-20, 35)
    return '<p>Temperature in %s is %s degrees C:</p>' % (location.capitalize(), str(temperature))

# function to generate a random wind speed and direction given a location
def get_wind(location):
    wind_speed = randrange(0, 50)
    wind_direction = str(randrange(0, 360)).rjust(3, "0")
    return '<p>Wind in %s is %skts at %sdeg</p>\n' % (location.capitalize(), str(wind_speed), wind_direction)

# HTML elements
header_title = '''
    <html>\n<head> <title>Weather Checker API</title> </head>\n<body>'''
instructions = '''
    <p>Instructions: Append a location 
    to the URL then either /temp or /wind (for example: /london/temp or /london/wind) 
    to get the temperature or wind at the entered location.</p>\n'''
instructions_location = '''
    <p>Instructions: Append  either /temp or /wind to the URL to get the temperature 
    or the wind.</p>\n'''
home_link = '<p><a href="/">Home</a></p>\n'
footer = '</body>\n</html>'

# Flask initiation
application = Flask(__name__)

# URL rules to access requested endpoint
application.add_url_rule('/', 'index', (lambda: header_title +
     instructions + footer))

application.add_url_rule('/<location>', 'location', (lambda location: 
    header_title + instructions_location + home_link + footer))

application.add_url_rule('/<location>/temp', 'temperature', (lambda location:
    header_title + get_temp(location) + home_link + footer))

application.add_url_rule('/<location>/wind', 'wind', (lambda location:
    header_title + get_wind(location) + home_link + footer))

if __name__ == "__main__":
    application.run()