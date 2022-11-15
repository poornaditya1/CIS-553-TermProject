import speech_recognition as sr
import webbrowser

url = 'https://docs.google.com/forms/d/e/1FAIpQLScGia1PMCFzaURH1UUX0DXtfzcQ-uyF8kStjZp0cDjccx5Cvw/formResponse?'

def listen(prompt):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # add function for speaking using the "prompt"
        audio = r.listen(source)
    text1 = r.recognize_google(audio)
    text = text1.replace(" ", "+")
    return text

def fillForm():
    name = listen("Speak your name")
    role = listen("Speak your role")
    uni = listen("Speak the name of your university")
    data = url + "entry.2109765752=" + name + "&entry.636569773=" + role + "&entry.958710338=" + uni
    webbrowser.open(data)

if __name__ == "__main__":
    fillForm()
    print("Done!")
