
import json
import requests
from win32com.client import Dispatch
from types import SimpleNamespace

speak = Dispatch("SAPI.SpVoice")
# speak.Speak("Hello World")

r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=5621f945a9c746baa86da2f1b394d166")
data = r.json()

description = data['articles'][0]['description']
speak.Speak(description)