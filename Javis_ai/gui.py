import customtkinter as ctk
from datetime import datetime

from .commands import execute
from .voice import listen, speak

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class DarvisUI:

    def __init__(self):

        self.app = ctk.CTk()

        self.app.title("DARVIS AI Assistant")

        self.app.geometry("500x700")

        self.app.configure(fg_color="#10002B")

        # -------- TITLE --------
        self.title = ctk.CTkLabel(
            self.app,
            text="💜 DARVIS",
            font=("Segoe UI", 28, "bold"),
            text_color="#C77DFF"
        )
        self.title.pack(pady=20)

        # -------- GREETING --------
        self.greeting = ctk.CTkLabel(
            self.app,
            text="Hello Sarishma 👋",
            font=("Segoe UI", 18),
            text_color="white"
        )
        self.greeting.pack()

        # -------- LIVE CLOCK --------
        self.clock = ctk.CTkLabel(
            self.app,
            text="",
            font=("Segoe UI", 16),
            text_color="#9D4EDD"
        )
        self.clock.pack(pady=10)

        # -------- CHAT BOX --------
        self.chatbox = ctk.CTkTextbox(
            self.app,
            width=430,
            height=350,
            corner_radius=20,
            fg_color="#240046",
            text_color="white",
            font=("Consolas", 14)
        )
        self.chatbox.pack(pady=15)

        self.chatbox.insert("end", "DARVIS: Ready to help you.\n\n")

        # -------- MIC BUTTON --------
        self.button = ctk.CTkButton(
            self.app,
            text="🎤 Speak",
            width=180,
            height=50,
            corner_radius=30,
            fg_color="#7B2CBF",
            hover_color="#9D4EDD",
            font=("Segoe UI", 16, "bold"),
            command=self.start_listening
        )
        self.button.pack(pady=20)

        self.update_clock()

    def update_clock(self):
        now = datetime.now().strftime("%I:%M:%S %p")
        self.clock.configure(text=now)
        self.app.after(1000, self.update_clock)

    def add_message(self, sender, message):
        self.chatbox.insert("end", f"{sender}: {message}\n\n")
        self.chatbox.see("end")

    def start_listening(self):
        self.add_message("DARVIS", "Listening...")

        try:
            command = listen()
        except (AttributeError, OSError) as error:
            self.add_message("DARVIS", f"Microphone unavailable: {error}")
            return

        if command == "":
            return

        self.add_message("You", command)

        response = execute(command)

        if response == "EXIT":
            speak("Goodbye Sarishma.")
            self.app.destroy()
            return

        speak(response)
        self.add_message("DARVIS", response)

    def run(self):
        self.app.mainloop()


if __name__ == "__main__":
    ui = DarvisUI()
    ui.run()