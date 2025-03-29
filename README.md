# TabTamer
“AI-powered Chrome tab usage tracker with Gemini integration"

# 🚀 TabTamer — AI-Backed Tab Overload Crusher

Are you drowning in a sea of browser tabs?  
**TabTamer** is your quirky AI-powered productivity sidekick — built for students, multitaskers, and tab hoarders alike.

---

## ✨ Features

- 📊 Tracks your open tabs in real-time
- 🤖 Uses **Gemini AI** to give:
  - Tabs to close
  - Tabs to keep
  - Fun motivational tip
- 📈 Calculates time spent per tab (tracked every minute)
- 🧠 Estimates memory usage per tab
- 📋 Provides a visual dashboard:
  - Top 10 tabs → 📊 histogram
  - Others → 🧾 table view
- 🔁 Automatic analysis every minute
- 🌱 Encourages focus, sustainability & less e-waste

---

## 💻 Tech Stack

| Area              | Tools/Frameworks               |
|-------------------|-------------------------------|
| Backend           | Python, Flask                 |
| AI Integration    | Google Gemini API (Free Tier) |
| Extension         | Chrome (JS, HTML, JSON)       |
| Data Viz          | Matplotlib                    |
| Styling           | CSS + dark mode aesthetics    |

---
## 🧪 How to Run This

### 🔌 1. Clone the Repo
```bash
git clone https://github.com/YOUR_USERNAME/tabtamer.git
cd tabtamer
```

---

### ⚙️ 2. Install Backend Dependencies
```bash
pip install -r requirements.txt
```

---

### ▶️ 3. Start Flask Server
```bash
python app.py
```

---

🧩 Chrome Extension Setup

1. Go to `chrome://extensions`
2. Enable Developer Mode
3. Click "Load Unpacked"
4. Select the `/extension` folder inside this repo


## 🔍 Output Preview

- 🎯 **Web Dashboard** → Visit `/realtime-summary`
- 📊 **Top 10 Tabs** → Displayed as a colorful histogram
- 📋 **All Tabs** → Listed in a readable table format
- 🤖 **Gemini AI Advice** → Personalized, witty tips (if AI key is added)

---

## 🛑 IMPORTANT: Enable Gemini AI (😎)

> Want TabTamer to give you real-time AI-generated advice on what tabs to close and how productive you really are?

### 🔐 How to Get Your Gemini API Key

1. Go to 👉 [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click on **“Create API key”**
4. Copy the generated key

---

### 🛠️ For Replit Users

1. Open the 🔒 **Secrets (Environment Variables)** tab  
2. Add a new secret:
   - **Key**: `GEMINI_API_KEY`
   - **Value**: *your Gemini API key here*

That’s it! 🎉 AI advice will now show up on your dashboard every minute.

