import pyttsx3
import speech_recognition as sr
from config import ASSISTANT_NAME, VOICE_RATE, VOICE_INDEX

engine = pyttsx3.init()

voices = engine.getProperty("voices")

if len(voices) > VOICE_INDEX:
    engine.setProperty("voice", voices[VOICE_INDEX].id)

engine.setProperty("rate", VOICE_RATE)

import asyncio
import edge_tts
from playsound import playsound
import tempfile
import os

VOICE = "en-US-AriaNeural"   # Female Microsoft AI voice

RATE = "+15%"   # Speed of speech

def speak(text):
    print("DARVIS:", text)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
        filename = temp_file.name

    async def generate_voice():
        communicate = edge_tts.Communicate(
            text=text,
            voice=VOICE,
            rate=RATE
        )
        await communicate.save(filename)

    asyncio.run(generate_voice())

    playsound(filename)
    os.remove(filename)



def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )
        except sr.WaitTimeoutError:
            return ""

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        speak("Speech recognition is unavailable.")
        return ""