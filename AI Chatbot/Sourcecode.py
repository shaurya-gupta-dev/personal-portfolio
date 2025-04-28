import requests
import time
import os
from colorama import init, Fore, Back, Style
import pyfiglet
import pyttsx3
import speech_recognition as sr
import re

init(autoreset=True)

API_URL = "https://router.huggingface.co/novita/v3/openai/chat/completions"
headers = {"Authorization": "Bearer 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"}
MEMORY_FILE = "memory.txt"
MAX_TOKENS = 150  # Adjust depending on model's token limit

def estimate_tokens(messages):
    return sum(len(msg["content"].split()) for msg in messages)

def compress_memory(messages):
    old_messages = messages[:-10]  # Keep latest 10
    summary_prompt = [
        {"role": "system", "content": "Summarize the following conversation briefly."},
        {"role": "user", "content": "\n".join([f"{m['role']}: {m['content']}" for m in old_messages])}
    ]
    payload = {
        "model": "deepseek/deepseek-v3-0324",
        "messages": summary_prompt
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    summary = response.json()["choices"][0]["message"]["content"]
    return [{"role": "system", "content": "Conversation so far: " + summary}] + messages[-10:]

def load_memory():
    messages = []
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if ":" in line:
                    role, content = line.strip().split(":", 1)
                    messages.append({"role": role, "content": content})
    return messages

def save_memory(messages):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        for msg in messages[-10:]:  # Save only last 10 messages
            f.write(f"{msg['role']}:{msg['content']}\n")

def clean_text(text):
    # Remove emojis and non-speech characters
    return re.sub(r'[^\x00-\x7F]+', '', text)

def chat():
    messages = load_memory()

    if estimate_tokens(messages) > MAX_TOKENS:
        messages = compress_memory(messages)

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(Fore.CYAN + "Listening...")
        audio = recognizer.listen(source)
        try:
            prompt = recognizer.recognize_google(audio)
            print(Fore.YELLOW + f"You: {prompt}")
        except Exception as e:
            print(Fore.RED + f"Speech Recognition Error: {e}")
            return chat()

    if prompt.lower() == "exit":
        print(Fore.LIGHTMAGENTA_EX + "Exiting, have a great day....")
        return

    messages.append({"role": "user", "content": prompt})
    
    # Insert system prompt at the beginning
    messages.insert(0, {
        "role": "system",
        "content": "You are an elite AI assistant trained by Dhruv. Respond like a big brother who keeps it raw, real, and helpful."
    })

    print(Fore.BLUE + "Thinking...")
    time.sleep(1)

    payload = {
        "model": "deepseek/deepseek-v3-0324",
        "messages": messages
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    reply = response.json()["choices"][0]["message"]["content"]
    print(Fore.GREEN + f"AI: {reply}")

    speaker = pyttsx3.init()
    speaker.setProperty('rate', 180)  # Speed
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[2].id)
    text = clean_text(reply)
    speaker.say(text)
    speaker.runAndWait()

    messages.append({"role": "assistant", "content": reply})
    save_memory(messages)

    with open("logs.txt", "a", encoding="utf-8") as logs:
        logs.write(f"You: {prompt}\n")
        logs.write(f"AI: {reply}\n\n")

    chat()

# Banner
banner = pyfiglet.figlet_format("CLI GPT")
print(Fore.LIGHTYELLOW_EX + banner)
time.sleep(1)
print(Fore.RED + Back.BLUE + "Hello, how can I help you?")
time.sleep(1)

a = input("press enter to start or exit to exit the programm: ")

if a == "":
    chat()
elif a == "exit":
    print("programm exited\nhave a nice day :)")
    exit()
else:
    print("invalid input")
