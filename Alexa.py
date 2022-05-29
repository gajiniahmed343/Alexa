import speech_recognition as sr
import pyttsx3
import pywhatkit
import flask
import datetime
import wikipedia
import pyjokes
import requests,json,sys

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("rate",140)
engine.setProperty("voice",voices[1].id)
def talk(text):
	engine.say(text)
	engine.runAndWait()

def take_command():
	try:
		with sr.Microphone() as source:
			print("Listening...")
			voice=listener.listen(source)
			command=listener.recognize_google(voice)
			command=command.lower()
	except:
		pass
	return command

def run_alexa():
	command=take_command()
	if "play" in command:
		song=command.replace("play","")
		talk("playing"+song)
		pywhatkit.playonyt(song)
	elif "time" in command:
		time=datetime.datetime.now().strftime("%I:%M %p")
		print(time)
		talk("Current time is "+time)
	elif "tell me" in command:
		person=command.replace("tell me","")
		info=wikipedia.summary(person,1)
		print(info)
		talk(info)
	elif "who is" in command:
		person=command.replace("who is","")
		info=wikipedia.summary(person,1)
		print(info)
		talk(info)
	elif "joke" in command:
		talk(pyjokes.get_joke())
	elif "date" in command:
		date=datetime.datetime.today().strftime("%B:%d %Y")
		print(date)
		talk("Today's date is "+date)
	
	elif "temperature" in command:
		apiKey="bf51fa4ce7e8af35d988827d3e6c91d4"
		baseurl="https://api.openweathermap.org/data/2.5/weather?q="
		res=requests.get("https://ipinfo.io/")
		data=res.json()
		cityname=data.get("city")
		completeurl=baseurl+cityname+"&appid="+apiKey
		response=requests.get(completeurl)
		da=response.json()
		temp=str(round(((da["main"]["feels_like"])-273.15),2))
		talk("Current Temperature at your Location is"+temp+"degree Celsius")
	elif "where am i" in command:
		res=requests.get("https://ipinfo.io/")
		data=res.json()
		city=data.get("city")
		sta=data.get("region")
		country=data.get("country")
		talk("You are in"+city+"City")
		talk(sta+"State")
	elif "current location" in command:
		res=requests.get("https://ipinfo.io/")
		data=res.json()
		city=data.get("city")
		sta=data.get("region")
		country=data.get("country")
		talk("You are in"+city+"City")
		talk(sta+"State")
	elif "stop" in command:
		sys.exit()


	else:
		talk("I can't understand what are you saying,Please tell me again")

	

while True:
	run_alexa()