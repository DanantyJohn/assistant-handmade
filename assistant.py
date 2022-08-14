import pyttsx3
import speech_recognition as sr
import webbrowser as wb
import os
import time
import sys
import datetime

def clear():
    os.system("clear")

robot = pyttsx3.init()

voice = robot.getProperty('voices')
robot.setProperty('voice',voice[1].id)

def nowtime ():
	Time = datetime.datetime.now().strftime("%I:%M:%p")
	speak(f"It's {Time} \n")

def speak(audio):
	for char in audio:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.02)
	robot.say(audio)
	robot.runAndWait()

def welcome():
	greeting = ["Good morning!\n", "Good afternoon!\n", "Good night!\n"]
	hour = datetime.datetime.now().hour
	if hour >= 6 and hour < 12:
		speak(greeting[0])
	elif hour >= 12 and hour <18:
		speak(greeting[1])
	elif hour >= 18 and hour <24:
		speak(greeting[2])

def user():
	u = sr.Recognizer()
	with sr.Microphone() as source:
		u.pause_threshold = 2
		audio = u.listen(source)
	try:
		query = c.recognize_google(audio,language='en')
		print("Wuoc: " + query)
	except sr.UnknownValueError:
		print("Please repeat or typing the command ")
		query = str(input('Your order is: '))
	return query


	
if __name__ =="__main__":
	welcome()
	speak('How can I help you, sir? \n')
	while True:
		command= input('User: ')
		#command = user().lower()
		google = r'C:\Program Files (x86)\CocCoc\Browser\Application\browser.exe'
		if "google" in command:
			speak('What do you want to search on google? \n')
			search= input('User: ')		
			#os.startfile(google)
			if search == 'youtube':
				speak('What do you like to watch on youtube, sir? \n')
				ohayo=input()
				wb.register('youtube', None,wb.BackgroundBrowser(google))
				url=f"www.youtube.com/results?search_query={ohayo}"
				wb.get('youtube').open(url)
				print(' ')
			elif search == 'quit':
				speak("How can I help you now, sir? \n")
				continue
			else:
				wb.register('google', None,wb.BackgroundBrowser(google))
				url=f"https://www.google.com/search?q={search}"
				wb.get('google').open_new_tab(url)
				print(' ')
		elif "nothing" in command:
			speak("So you you don't want to search anything, sir! \n")
			#o = input("User: ")
			#if "yes" in o:
			#	speak('Goodbye, sir \n')
			#else:
			#	speak('How can I help you now, sir? \n')
			continue

		elif 'time' in command:
			nowtime()

		elif "quit" in command:
			speak("Goodbye, sir \n")
			quit()
		else:
			speak('For now, we have no updated for this program. Please try again!!!\n')
			continue

		speak('What do you want to do next, sir? \n')