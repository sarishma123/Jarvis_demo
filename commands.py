import datetime
import webbrowser
import os


def execute(command):

    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}"

    elif "date" in command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        return f"Today is {today}"

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google."

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    elif "open calculator" in command:
        os.system("calc")
        return "Opening Calculator."

    elif "open chrome" in command:
        os.system("start chrome")
        return "Opening Chrome."

    elif "open vscode" in command:
        os.system("code")
        return "Opening Visual Studio Code."

    elif "exit" in command:
        return "EXIT"

    else:
        return "Sorry, I don't know that command yet."