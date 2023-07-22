# imports
import speech_recognition as sr
import pyttsx3 as pytt
import datetime
import pywhatkit
import wikipedia
import pyjokes
# Variables
listener = sr.Recognizer()
sp = pytt.init()
voices = sp.getProperty('voices')
sp.setProperty('voice', voices[2].id)
# functions
def say(text):
    sp.say(text)
    sp.runAndWait()
say("Hey\n, My name is Rob")
say(f"I can tell u an information about someone or something\nOr tell u jokes\n"
    f"and play a song for you\nor tell u the time\nand other things.")
def listen():
    try:
        with sr.Microphone() as source:
            print('listening...')
            say('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'rob' in command:
                command = command.replace('rob', '')
                print(command)
    except:
        say("sorry there is an error because of your stupidity")
    return command
def run_VA():
    command = listen()
    if "how are you" in command:
        say("fine\n thanks")
    elif "you're stupid" in command:
        say("I'm not the only one, cuz you're the most stupid person ever!")
    elif "who are you" in command:
        say("I'm Rob")
    elif ['hey', 'hi', 'hello'] in command:
        say("Hello")
    elif "i hate you" in command:
        say("me too")
    elif "repeat after me" in command:
        text = command.replace('repeat after me', '')
        say(text)
    elif "i want to destroy you" in command:
        say("You cant!\n I am an AI\n HAHA!")
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is' + time)
        say('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        say(info)
    elif 'what is' in command:
        thing = command.replace('what is', '')
        info = wikipedia.summary(thing, 1)
        print(info)
        say(info)
    elif 'play' in command:
        song = command.replace('play', '')
        pywhatkit.playonyt(song)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        say(joke)
    else:
        print("Please say the command again.")
        say('Please say the command again.')
# Running
if __name__ == '__main__':
    run_VA()
