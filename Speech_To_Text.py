import speech_recognition as sr
import spacy
from spacy.language import Language
from spacy_langdetect import LanguageDetector
from transformers import pipeline
from googletrans import Translator

#LOAD PIPELINE
@Language.factory("language_detector")

def get_lang_detector(nlp, name):
   return LanguageDetector()

nlp = spacy.load("en_core_web_sm")
#print(nlp.pipeline)
nlp.add_pipe('language_detector', last=True)

#SPEECH TO TEXT
r = sr.Recognizer()

with sr.AudioFile("output1.wav") as source:
    audio_text = r.listen(source)
    try:
        text = r.recognize_google(audio_text)
        print("Speech to text results: ", text)
    except:
        print('Sorry... run again')

#DETECT LANGUAGE
doc = nlp(text)
detected_language = doc._.language
print("Detected_language: ", detected_language['language'])

#SET YOUR LANGUAGE
# en = english
# es = spanish
# it = italian
# fr = french

selected_language = 'en'

# USING PRETRAINED PIPELINES
"""if selected_language != detected_language['language']:
    print("It is not in your language! Translation in progress...")
    #translation_from_to = 'translation_' + detected_language['language'] + '_' + 'to' + '_' + selected_language
    #print(translation_from_to)
    translation_pipeline = pipeline('translation', 'facebook/m2m100_418M', src_lang=detected_language['language'], tgt_lang=selected_language)
    translated_text = translation_pipeline(text)
    print(translated_text[0]['translation_text'])

else:
    print("No translation required.")"""

# USING GOOGLE TRANSLATOR API
if selected_language != detected_language['language']:
    print("It is not in your language! Translation in progress...")
    translator = Translator()
    translator.translate(text, dest=selected_language)
    
else:
    print("No translation required.")
