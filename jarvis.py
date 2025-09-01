import openai
import pyttsx3
import speech_recognition as sr
from config import apikey

openai.api_key = apikey

class JarvisAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with self.mic as source:
            print("Listening...")
            audio = self.r.listen(source)
        try:
            return self.r.recognize_google(audio)
        except:
            return ""

    def ask_ai(self, query):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=query,
            max_tokens=150
        )
        return response.choices[0].text.strip()
