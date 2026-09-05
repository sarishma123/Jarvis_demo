import customtkinter as ctk
from datetime import datetime
import threading

from voice import speak, listen
from commands import execute


# Theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Window
app = ctk.CTk()
app.title("DARVIS AI Assistant")
app.geometry("500x700")
app.configure(fg_color="#10002B")

# Title
title = ctk.CTkLabel(
    app,
    text="💜 DARVIS",
    font=("Segoe UI", 30, "bold"),
    text_color="#C77DFF"
)
title.pack(pady=40)

# Greeting
greeting = ctk.CTkLabel(
    app,
    text="Hello Sarishma 👋",
    font=("Segoe UI", 18),
    text_color="white"
)
greeting.pack()

# ✅ Clock widget FIRST
clock = ctk.CTkLabel(
    app,
    text="",
    font=("Segoe UI", 16),
    text_color="#9D4EDD"
)
clock.pack(pady=15)

# Clock function AFTER clock exists
def update_clock():
    current = datetime.now().strftime("%I:%M:%S %p")
    clock.configure(text=current)
    app.after(1000, update_clock)

# ---------------- CHAT BOX ----------------
chatbox = ctk.CTkTextbox(
    app,
    width=430,
    height=320,
    corner_radius=20,
    fg_color="#240046",
    text_color="white",
    font=("Consolas", 14)
)
chatbox.pack(pady=20)

# First message from DARVIS
chatbox.insert("end", "💜 DARVIS: Hello Sarishma! I'm ready to help you.\n\n")
# Start the clock
update_clock()


def add_message(sender, message):
    chatbox.insert("end", f"{sender}: {message}\n\n")
    # ---------------- MICROPHONE BUTTON ----------------
mic_button = ctk.CTkButton(
    app,
    text="🎤 Speak",
    width=180,
    height=55,
    corner_radius=30,
    fg_color="#7B2CBF",
    hover_color="#9D4EDD",
    font=("Segoe UI", 16, "bold"),
    command=lambda: threading.Thread(target=start_listening, daemon=True).start()
)

mic_button.pack(pady=25)
chatbox.see("end")      # Auto-scroll to latest message

add_message("You", "Hi DARVIS!")
add_message("DARVIS", "Hello! Nice to see you again.")

def start_listening():

    app.after(0, lambda: add_message("💜 DARVIS", "🎤 Listening..."))

    command = listen()

    if command == "":
        app.after(0, lambda: add_message("💜 DARVIS", "I didn't hear anything."))
        return

    app.after(0, lambda: add_message("🧑 You", command))

    response = execute(command)

    if response == "EXIT":
        speak("Goodbye Sarishma.")
        app.after(0, app.destroy)
        return

    app.after(0, lambda: add_message("💜 DARVIS", response))
    speak(response)

# Keep window open
app.mainloop()