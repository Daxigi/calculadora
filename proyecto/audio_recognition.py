import pyaudio
import wave
import speech_recognition as sr


def recognize_audio_from_file(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        print("Por favor, diga algo...")
        audio = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio, language='es-ES')
            print("Texto reconocido: ", text)
            return text
        except sr.UnknownValueError:
            print("No se ha podido reconocer el audio")
        except sr.RequestError as e:
            print("Error en la petición: ", e)
    return None