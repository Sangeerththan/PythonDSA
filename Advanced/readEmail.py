# Importing necessary libraries
import win32com.client
import speech_recognition as sr
import pyttsx3
from datetime import date

r = sr.Recognizer()

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def read_emails():

    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder \
        (6) # "6" refers to the index of a folder - in this case,the inbox. You can change that number to reference any other folder
    messages = inbox.Items
    today_messages = messages.Restrict("[ReceivedTime] >= '" + str(date.today()) + "'")
    for message in today_messages:
        body_content = message.body
        print(body_content)
        SpeakText(body_content)

if __name__ == '__main__':
    read_emails()
