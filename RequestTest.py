import speech_recognition as sr
import requests
import subprocess

url = 'https://docs.google.com/forms/d/e/1FAIpQLScGia1PMCFzaURH1UUX0DXtfzcQ-uyF8kStjZp0cDjccx5Cvw/formResponse?'

def speak(text):
    subprocess.call(["say",text])

def listen(prompt):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak(text)
        audio = r.listen(source)
    text1 = r.recognize_google(audio)
    text = text1.replace(" ", "+")
    return text

def fillForm():
    name = listen("Speak your name")
    role = listen("Speak your role")
    uni = listen("Speak the name of your university")
    data = url + "entry.2109765752=" + name + "&entry.636569773=" + role + "&entry.958710338=" + uni
    requests.post(data)

if __name__ == "__main__":
    fillForm()
    print("Done!")
