import asyncio
import os
import tempfile
import speech_recognition as sr
import edge_tts
import pygame

VOICE = "en-US-AriaNeural"   # Female AI voice

pygame.mixer.init()


async def _speak_async(text):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        filename = f.name

    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(filename)

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    pygame.mixer.music.unload()
    os.remove(filename)


def speak(text):
    print("DARVIS:", text)
    asyncio.run(_speak_async(text))


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
        return ""

    except sr.RequestError:
        speak("Speech recognition is unavailable.")
        return ""