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

### 2. Install Backend Dependencies
bash
Copy
Edit
pip install -r requirements.txt


3. Start Flask Server
bash
Copy
Edit
python app.py


🔍 Output Preview
🎯 Web Dashboard (/realtime-summary)
Top 10 Tabs → Displayed as a colorful histogram

All Tabs → Listed in a readable table format

🤖 AI Gemini Advice → Personalized, witty tips

### IMPORTANT
---

## 🔐 Using Gemini AI (Optional, but Fun 😄)

Want TabTamer to give you real-time AI-generated advice on what tabs to close and how productive you really are?

Follow these steps to enable AI integration:

1. Go to 👉 [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click on **“Create API key”**
4. Copy the generated key

---

### 🛠️ Replit Users

1. On Replit, open the 🔒 **Secrets (Environment Variables)** tab  
2. Add a new entry:
   - **Key**: `GEMINI_API_KEY`
   - **Value**: *paste your Gemini API key here*

That’s it! 🎉 AI advice will now show up on your dashboard every minute.

> ✅ If you don’t provide a key, the rest of TabTamer still works perfectly — you’ll just see a placeholder message in the AI advice box.

---
