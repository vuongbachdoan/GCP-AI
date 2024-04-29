import speech_recognition as sr
from google.cloud import speech_v1 as speech
from google.cloud.speech_v1 import types
from vertex import generate

def listen_and_convert():
  """Listens using microphone for 10 seconds and converts to text using Speech-to-Text"""
  can_continue = True

  while can_continue:
    # Initialize recognizer and microphone
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
      print("Listening...")
      audio = recognizer.listen(source, timeout=10)  # Listen for 10 seconds

    # Try converting audio to text
    try:
      text = recognizer.recognize_google(audio)
      print("You said: " + text)
      if text == 'exit' or text == 'quit' or text == 'end call':
        can_continue = False
        print('Exiting!')
      else:
        generate(text)
        can_continue = True
    except sr.UnknownValueError:
      print("Could not understand audio")
    except sr.RequestError as e:
      print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
  listen_and_convert()







