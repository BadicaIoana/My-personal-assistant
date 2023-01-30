import speech_recognition as sr
import requests
from datetime import datetime
import pyttsx3

r = sr.Recognizer ( )

while True :
	engine = pyttsx3.init ( )
	with sr.Microphone ( ) as source :
		audio = r.listen ( source )
	try :
		try :
			request = input ( "You: " )  # get input from the user via the terminal
		
		except :
			request = r.recognize_google ( audio , language = "en-US" )
		print ( "You: " + request )
		# Check if user greeted
		if "hello" in request.lower ( ) :
			response = "Hello! How can I help you?"
		# Check if user is asking how the assistant is doing
		elif "how are you" in request.lower ( ) :
			response = "I am doing well, thank you for asking!"
		# Check if user is asking who the assistant is
		elif "what are you" in request.lower ( ) :
			response = "I'm Ghost, your personal assistant."
		elif "what is the date" in request.lower ( ) :
			response = f"Today is {datetime.now ( ).strftime ( '%m/%d/%Y' )}"
		elif "what is the time" in request.lower ( ) :
			response = f"The current time is {datetime.now ( ).strftime ( '%H:%M:%S' )}"
		elif "what's the weather" in request.lower ( ) :
			# get weather information from OpenWeatherMap API
			api_key = 'your api'
			base_url = "http://api.openweathermap.org/data/2.5/weather?"
			city_name = "your city"  # replace this with the desired city
			complete_url = base_url + "appid=" + api_key + "&q=" + city_name
			response = requests.get ( complete_url )
			x = response.json ( )
			if x [ "cod" ] != "404" :
				y = x [ "main" ]
				current_temperature = y [ "temp" ]
				current_pressure = y [ "pressure" ]
				current_humidity = y [ "humidity" ]
				z = x [ "weather" ]
				weather_description = z [ 0 ] [ "description" ]
				response = f"Temperature: {current_temperature}°C\nPressure: {current_pressure} hPa\nHumidity: {current_humidity}%\nWeather description: {weather_description}"
			else :
				response = "City not found"
		else :
			response = "I don't understand what you want to say. Can I help you with anything else?"
	except sr.UnknownValueError :
		response = "I didn't understand what you said."
	print ( "Assistant:" , response )
	engine.say ( response )
	engine.runAndWait ( )
