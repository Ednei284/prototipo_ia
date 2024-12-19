import time
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment 
from pydub.playback import play
import feeling_recognition 
from googletrans import Translator
translator = Translator()
from flask import  jsonify

# Função para converter voz em texto
def speech_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="pt-BR")
            text_converted_to_english =  translator.translate(text, src='pt', dest='en')
            time.sleep(2)
            text_converted_to_english = str(text_converted_to_english)
            feeling = feeling_recognition.feeling_analiser(text_converted_to_english)
            return jsonify({"recognized_text": text,'feeling':feeling}), 200

        except sr.UnknownValueError:
            return jsonify({"error": "Desculpe, não consegui entender o que você disse."}), 400
            
        except sr.RequestError as e:
            return jsonify({"error": f"Não foi possível solicitar os resultados: {e}"}), 500

# Função para converter texto em voz
def text_speech(texto):
    tts = gTTS(texto, lang="pt")
    tts.save("saida.mp3")
    song = AudioSegment.from_mp3('saida.mp3') 
    play(song)


