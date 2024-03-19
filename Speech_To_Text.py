import speech_recognition as sr
from spacy_langdetect import LanguageDetector
import spacy
#import en_core_web_sm


r = sr.Recognizer()

with sr.AudioFile("output1.wav") as source:
    audio_text = r.listen(source)
    try:
        text = r.recognize_google(audio_text)
        print(text)
    except:
        print('Sorry...run again')
        
nlp = spacy.load("en_core_web_sm")
import en_core_web_sm
nlp = en_core_web_sm.load()
nlp.add_pipe(LanguageDetector(), name = 'language_detector', last=True)
doc = nlp(text)
detect_language = doc._.language
print(detect_language)
        
