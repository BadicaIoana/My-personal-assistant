import speech_recognition as sr
import requests
from datetime import datetime
import pyttsx3

# Recognizer instance
r = sr.Recognizer()

# Infinite loop for processing user input
while True:
    # Initialize text-to-speech engine
    engine = pyttsx3.init()
    
    # Use microphone as audio source
    with sr.Microphone() as source:
        audio = r.listen(source)

    # Try to recognize user input
    try:
        # If user provided input via terminal
        try:
            request = input("You: ")  
        except:
            # If user provided input via speech
            request = r.recognize_google(audio, language="en-US")
        print("You: " + request)
        
        # Respond based on the user input
        if "hello" in request.lower():
            response = "Hello! How can I help you?"
        elif "how are you" in request.lower():
            response = "I am doing well, thank you for asking!"
        elif "what are you" in request.lower():
            response = "I'm Ghost, your personal assistant."
        elif "what is the date" in request.lower():
            response = f"Today is {datetime.now().strftime('%m/%d/%Y')}"
        elif "what is the time" in request.lower():
            response = f"The current time is {datetime.now().strftime('%H:%M:%S')}"
        elif "what's the weather" in request.lower():
            # Get weather information from OpenWeatherMap API
            api_key = 'your api'
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            city_name = "your city"
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            weather_data = response.json()
            if weather_data["cod"] != "404":
                main_data = weather_data["main"]
                current_temperature = main_data["temp"]
                current_pressure = main_data["pressure"]
                current_humidity = main_data["humidity"]
                weather_desc = weather_data["weather"][0]["description"]
                response = f"Temperature: {current_temperature}°C\nPressure: {current_pressure} hPa\nHumidity: {current_humidity}%\nWeather description: {weather_desc}"
            else:
                response = "City not found"
        else:
            response = "I don't understand what you want to say. Can I help you with anything else?"
    except sr.UnknownValueError:
        response = "I didn't understand what you said."
    
    # Print and speak the response
    print("Assistant:", response)
    engine.say(response)
    engine.runAndWait()
