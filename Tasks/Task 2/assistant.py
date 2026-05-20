import pyttsx3
import datetime
import webbrowser
import os
import random

# =========================
# INITIALIZE JARVIS
# =========================

engine = pyttsx3.init()

# Jarvis Voice Settings
engine.setProperty('rate', 120)
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)   # Male voice

# =========================
# SPEAK FUNCTION
# =========================

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# =========================
# STARTUP
# =========================

startup_lines = [
    "System online sir.",
    "Jarvis activated.",
    "Welcome back sir.",
    "All systems are operational sir."
]

speak(random.choice(startup_lines))

# =========================
# MAIN LOOP
# =========================

while True:

    command = input("\nEnter command: ").lower()

    # =========================
    # PLAY MUSIC
    # =========================

    if "play music" in command:

        music_path = r"C:\Users\yashwanth\Music\song.mp3"

        if os.path.exists(music_path):
            os.startfile(music_path)
            speak("Certainly sir. Playing your music now.")
        else:
            speak("Music file not found sir.")

    # =========================
    # OPEN GOOGLE
    # =========================

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google sir.")

    # =========================
    # OPEN YOUTUBE
    # =========================

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube sir.")

    # =========================
    # OPEN CHATGPT
    # =========================

    elif "open chatgpt" in command:
        webbrowser.open("https://chat.openai.com")
        speak("Opening ChatGPT sir.")

    # =========================
    # OPEN WHATSAPP
    # =========================

    elif "open whatsapp" in command:
        webbrowser.open("https://web.whatsapp.com")
        speak("Opening WhatsApp sir.")

    # =========================
    # OPEN INSTAGRAM
    # =========================

    elif "open instagram" in command:
        webbrowser.open("https://www.instagram.com")
        speak("Opening Instagram sir.")

    # =========================
    # OPEN FACEBOOK
    # =========================

    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook sir.")

    # =========================
    # OPEN CALCULATOR
    # =========================

    elif "open calculator" in command:
        os.system("calc")
        speak("Opening Calculator sir.")

    # =========================
    # OPEN NOTEPAD
    # =========================

    elif "open notepad" in command:
        os.system("notepad")
        speak("Opening Notepad sir.")

    # =========================
    # OPEN PAINT
    # =========================

    elif "open paint" in command:
        os.system("mspaint")
        speak("Opening Paint sir.")

    # =========================
    # OPEN COMMAND PROMPT
    # =========================

    elif "open cmd" in command:
        os.system("start cmd")
        speak("Opening Command Prompt sir.")

    # =========================
    # TIME
    # =========================

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"Sir, the current time is {current_time}")

    # =========================
    # DATE
    # =========================

    elif "date" in command:
        today = datetime.date.today()
        speak(f"Sir, today's date is {today}")

    # =========================
    # GREETINGS
    # =========================

    elif "hello" in command:
        speak("Hello sir. How may I assist you today?")

    elif "how are you" in command:
        speak("I am functioning perfectly sir.")

    elif "good morning" in command:
        speak("Good morning sir. Wishing you a productive day.")

    elif "good night" in command:
        speak("Good night sir. Take care.")

    # =========================
    # JARVIS INFORMATION
    # =========================

    elif "who are you" in command:
        speak("I am Jarvis, your intelligent virtual assistant.")

    elif "your name" in command:
        speak("My name is Jarvis sir.")

    elif "thank you" in command:
        speak("Always happy to help sir.")

    # =========================
    # GOOGLE SEARCH
    # =========================

    elif "search google" in command:

        search = input("What should I search on Google: ")

        webbrowser.open(
            f"https://www.google.com/search?q={search}"
        )

        speak(f"Searching Google for {search}")

    # =========================
    # YOUTUBE SEARCH
    # =========================

    elif "search youtube" in command:

        search = input("What should I search on YouTube: ")

        webbrowser.open(
            f"https://www.youtube.com/results?search_query={search}"
        )

        speak(f"Searching YouTube for {search}")

    # =========================
    # SYSTEM COMMANDS
    # =========================

    elif "shutdown" in command:
        speak("Shutting down the computer sir.")
        os.system("shutdown /s /t 5")

    elif "restart" in command:
        speak("Restarting the computer sir.")
        os.system("shutdown /r /t 5")

    # =========================
    # EXIT
    # =========================

    elif "exit" in command or "bye" in command:
        speak("Shutting down systems. Goodbye sir.")
        break

    # =========================
    # UNKNOWN COMMAND
    # =========================

    else:
        speak("I apologize sir. I did not understand that command.")