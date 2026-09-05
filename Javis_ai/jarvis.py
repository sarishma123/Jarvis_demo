from voice import speak, listen
from commands import execute
from config import USER_NAME, ASSISTANT_NAME


def start():

    speak(f"Hello {USER_NAME}. I am {ASSISTANT_NAME}.")
    speak("How can I help you today?")

    while True:

        command = listen()

        if command == "":
            continue

        response = execute(command)

        if response == "EXIT":
            speak("Goodbye. Have a wonderful day.")
            break

        speak(response)


if __name__ == "__main__":
    start()