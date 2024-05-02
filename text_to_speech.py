import pyttsx3
import os
voice = pyttsx3.init()
myText = "Hello my beautiful people.Now in this video you are learning how to convert text to speech using python"
voice.say(myText)
voice.save_to_file(myText,"hello.mp3")
voice.runAndWait()
os.system("start hello.mp3")

