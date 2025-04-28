# CLI GPT - Voice-Powered AI Chatbot

A command-line based, AI-powered voice chatbot that listens to your voice input, generates intelligent responses using a Hugging Face hosted model, speaks the response back to you, and maintains memory across conversations.

Built with ❤️ by Shaurya.

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
