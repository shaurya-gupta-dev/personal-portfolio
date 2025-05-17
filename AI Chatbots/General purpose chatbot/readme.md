# CLI GPT - Voice-Powered AI Chatbot

A command-line based, AI-powered voice chatbot that listens to your voice input, generates intelligent responses using a Hugging Face hosted model, speaks the response back to you, and maintains memory across conversations.

Built with ❤️ by Shaurya

---

## 🚀 Features

- 🎤 **Voice Input:** Speak to the chatbot via your microphone.
- 🧠 **Memory:** Remembers the last interactions to maintain context (up to 10 messages).
- 🔥 **Personality:** Responds like a "big brother" — raw, real, and helpful.
- 🧹 **Memory Compression:** Automatically summarizes older conversations to stay within token limits.
- 🎙️ **Voice Output:** Speaks responses using realistic text-to-speech.
- 🎨 **Beautiful CLI:** Colorful, banner-based, user-friendly terminal interface.
- 📝 **Logging:** Saves full conversations to `logs.txt` for future reference.

---

## 📋 Requirements

- Python 3.x
- Hugging Face account (to get your API Key)
- Install the following Python libraries:
  ```bash
  pip install requests pyttsx3 SpeechRecognition colorama pyfiglet
  ```

## ⚙️ Installation
1- get code from sourcecode.py and make a python file consisting that code.

2- Install the dependencies:

```bash
pip install -r requirements.txt
```

(Create a requirements.txt with the following lines if not already created:

```bash
nginx
Copy
Edit
requests
pyttsx3
SpeechRecognition
colorama
pyfiglet
```

3- Set your Hugging Face API Key inside the script:

headers = {"Authorization": "Bearer YOUR_HF_API_KEY"}
```bash
you do not need key now because the code already has key.
```

## 🛠️ Usage
1- Run the script:

```bash
python filename.py
```

2- You will see a banner:

```bash
 ____ _     ___   ____ ____ _____ 
/ ___| |   / _ \ / ___|  _ \_   _|
| |   | |  | | | | |  _| |_) || |  
| |___| |__| |_| | |_| |  __/ | |  
\____|_____\___/ \____|_|    |_|  
Press Enter to start chatting, or type exit to close the program.
```

- Speak when the bot says "Listening..."

- Wait while it says "Thinking..."

- The bot will reply back by speaking and printing the response.

## 💡 How It Works
- Listens to your voice input using SpeechRecognition.

- Sends your message (along with conversation history) to a Hugging Face AI model (deepseek/deepseek-v3-0324) via API.

- Receives the AI’s response.

- Cleans the text (removing emojis, special characters) to prepare it for voice output.

- Speaks the reply using pyttsx3.

- Saves your conversation history locally for continuous context.

## 📂 Files
- chatbot.py — Main script file.

- memory.txt — Stores the last 10 messages for memory persistence.

- logs.txt — Saves every full conversation session.

## 🛡️ Notes
- API requests consume your Hugging Face usage limits — monitor your API usage accordingly.

- Microphone access is required.

- Internet connection is necessary for making API calls to Hugging Face.
