from voice import speak, listen
from commands import execute
from config import ASSISTANT_NAME, USER_NAME


def start():

    speak(f"Hello {USER_NAME}. I am {ASSISTANT_NAME}.")
    speak("I am ready. What can I do for you?")

    while True:

        command = listen()

        if command == "":
            continue

        response = execute(command)

        if response == "EXIT":
            speak("Goodbye. Have a nice day.")
            break

        speak(response)


if __name__ == "__main__":
    start()