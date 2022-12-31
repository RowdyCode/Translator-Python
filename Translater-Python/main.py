from translator import TranslationHinToEng
from listen import Listen
from speak import speak

def MicExe():
    query = Listen()
    data = TranslationHinToEng(query)
    speak(data)

while True:
	MicExe()