from googletrans import Translator
import googletrans
import speech_recognition as sr

# SELECT YOUR LANGUAGE
selected_language = 'en'

# SPEECH TO TEXT
r = sr.Recognizer()

with sr.AudioFile("output1.wav") as source:
    audio_text = r.listen(source)
    try:
        text = r.recognize_google(audio_text)
        print("Speech to text results: ", text)
    except:
        print('Sorry... run again')

# TRANSLATOR SETUP
translator = Translator()

detected = translator.detect(text)
print(detected)
detected_language = detected["lang"]

if selected_language != detected_language['language']:
    print("It is not in your language! Translation in progress...")
    translator = Translator()
    translator.translate(text, dest=selected_language)

else:
    print("No translation required.")

