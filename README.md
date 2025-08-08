# Jarvis – Python Voice Assistant

Jarvis is a simple voice assistant built in Python for practice and learning.  
It listens for the wake word **"Jarvis"** and can open websites, read news headlines, and play music links from your own `musicLibrary.py`.

---

## ✨ Features

- **Wake word detection** – say `"Jarvis"` to activate.
- **Open websites** – Google, YouTube, LinkedIn.
- **News headlines** – fetches and reads the latest US headlines from [NewsAPI](https://newsapi.org/).
- **Play music** – plays songs/links stored in `musicLibrary.py`.
- **Text-to-speech** responses.

---

## 📦 Requirements

- Python 3.8+
- Microphone and speakers
- A [NewsAPI](https://newsapi.org/) account (free) for your own API key

---

## 🚀 Setup & Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>

   ```

2. **Create and activate a virtual environment**
   python -m venv .venv

# Windows (PowerShell)

.venv\Scripts\activate

# macOS/Linux

source .venv/bin/activate

3. **Install dependencies**
   pip install -r requirements.txt

4. **Create your .env file**
   NEWS_API_KEY=your_api_key_here

5. **Run The Script**
   python main.py
