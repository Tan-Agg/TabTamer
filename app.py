from flask import Flask, request, jsonify
from flask_cors import CORS
from collections import defaultdict
import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
import psutil
import os
import requests

app = Flask(__name__)
CORS(app)

# Track time spent on each tab
tab_tracking_data = defaultdict(int)

# Gemini API key from Replit Secrets
gemini_key = os.getenv("GEMINI_API_KEY")

def call_gemini_api(prompt):
    try:
        url = "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-pro:generateContent"
        headers = {
            "Content-Type": "application/json",
            "x-goog-api-key": gemini_key
        }
        data = {
            "contents": [
                {
                    "parts": [{"text": prompt}]
                }
            ]
        }

        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        candidates = result.get("candidates")
        if candidates and "content" in candidates[0]:
            return candidates[0]["content"]["parts"][0]["text"]
        else:
            return "⚠️ Gemini Error: Unexpected response format"
    except Exception as e:
        return f"⚠️ Gemini Error: {str(e)}"

def generate_mood_advice(focus_score, total_time):
    if focus_score >= 80 and total_time < 45:
        return "💪 Super focused! Ride the wave."
    elif focus_score < 40 and total_time > 60:
        return "😵‍💫 Distracted and fatigued. Netflix break time?"
    elif 50 <= focus_score <= 70:
        return "🧘‍♀️ Solid focus. Don’t forget to blink."
    elif focus_score == 0:
        return "😴 Wake up, tab zombie. Close YouTube maybe?"
    else:
        return "😐 Keep it steady. You’re doing okay."

@app.route('/')
def home():
    return "🎉 TabTamer Backend with Gemini REST AI is running!"

@app.route('/analyze', methods=['POST'])
def analyze_tabs():
    tabs = request.json.get('tabs', [])
    for tab in tabs:
        title = tab.get('title', '')
        tab_tracking_data[title] += 1
    return jsonify({"status": "ok"})

@app.route('/realtime-summary', methods=['GET'])
def realtime_summary():
    sorted_tabs = sorted(tab_tracking_data.items(), key=lambda x: x[1], reverse=True)
    top_10 = sorted_tabs[:10]
    others = sorted_tabs[10:]

    titles = [title for title, _ in top_10]
    minutes = [minutes for _, minutes in top_10]
    plt.figure(figsize=(10, 5))
    plt.barh(titles[::-1], minutes[::-1], color='#5cb85c')
    plt.xlabel('Minutes Spent')
    plt.title('Top 10 Tabs Usage')
    img = io.BytesIO()
    plt.tight_layout()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_data = base64.b64encode(img.getvalue()).decode()

    mem = psutil.virtual_memory()
    used = f"{mem.used / (1024 ** 3):.2f} GB"
    total = f"{mem.total / (1024 ** 3):.2f} GB"

    work_keywords = ["Drive", "Docs", "Colab", "Resume", "Leetcode"]
    fun_keywords = ["YouTube", "Netflix", "Reddit", "Instagram"]
    work_time = 0
    fun_time = 0
    for title, mins in sorted_tabs:
        if any(word in title for word in work_keywords):
            work_time += mins
        elif any(word in title for word in fun_keywords):
            fun_time += mins

    total_time = work_time + fun_time
    focus_score = int((work_time / total_time) * 100) if total_time > 0 else 0
    mood_advice = generate_mood_advice(focus_score, total_time)

    top_info = "\n".join([f"{title}: {mins} min" for title, mins in top_10])
    prompt = f"""
Act like a sarcastic productivity coach.
Here’s today’s session:
{top_info}

🧮 Focus Score: {focus_score}/100
🧠 Work Time: {work_time} min | 💤 Fun Time: {fun_time} min

Now:
🧹 List tabs to close
🧠 List tabs to keep
💡 Give a short motivational tip
🎯 Suggest 1 task they should do next
Keep it cheeky, concise, and formatted with emojis.
    """
    ai_advice = call_gemini_api(prompt)

    def make_row(idx, tab, minutes, highlight=False):
        bg = "background-color: #2e7d32; color: #fff;" if highlight else ""
        return f"<tr style='{bg}'><td>{idx}</td><td>{tab}</td><td>{minutes} min</td></tr>"

    top_rows = [make_row(i+1, t, m, True) for i, (t, m) in enumerate(top_10)]
    other_rows = [make_row(i+11, t, m) for i, (t, m) in enumerate(others)]
    all_rows = "".join(top_rows + other_rows)

    html = f"""
    <html>
    <head>
      <title>TabTamer Dashboard</title>
      <style>
        body {{ font-family: 'Segoe UI', sans-serif; padding: 30px; background: #121212; color: #f1f1f1; }}
        h2, h3 {{ color: #ffcc80; margin-bottom: 10px; }}
        .header-title {{ font-size: 1.6em; font-weight: bold; color: #ff7043; margin-bottom: 12px; }}
        .ai-box, .mood-box {{ background: #1e1e1e; padding: 20px; margin-bottom: 25px; white-space: pre-wrap; font-size: 1.1em; line-height: 1.8; box-shadow: 0 4px 12px rgba(0,0,0,0.3); }}
        .ai-box {{ border-left: 5px solid #ff9800; }}
        .mood-box {{ border-left: 5px solid #64ffda; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 20px; background: #1f1f1f; box-shadow: 0 2px 8px rgba(0,0,0,0.2); margin-bottom: 40px; }}
        th, td {{ border: 1px solid #333; padding: 12px 16px; text-align: left; }}
        th {{ background-color: #424242; color: #fff; font-size: 1em; }}
        img {{ border-radius: 8px; margin-top: 15px; box-shadow: 0 2px 6px rgba(0,0,0,0.4); }}
        .meta-info p {{ margin: 5px 0; }}
      </style>
    </head>
    <body>
      <h2>📊 Real-Time Tab Usage Summary</h2>

      <div class='meta-info'>
        <p><strong>🖥️ System Memory:</strong> {used} used out of {total}</p>
        <p><strong>🧮 Focus Score:</strong> {focus_score}/100</p>
        <p><em>Focus Score = time spent on productive vs distracting tabs. Higher = better.</em></p>
      </div>

      <div class='mood-box'><strong>🧘 Mood Check:</strong> {mood_advice}</div>

      <div class='ai-box'>
        <div class='header-title'>🤖 AI Scaling (a.k.a Judging You)</div>
        {ai_advice}
      </div>

      <h3>📈 Top 10 Tabs (Histogram)</h3>
      <img src="data:image/png;base64,{plot_data}" alt="Top Tabs Histogram" width="100%"/>

      <h3>📋 All Tabs (Top 10 highlighted)</h3>
      <table>
        <tr><th>#</th><th>Tab Title</th><th>Time Spent</th></tr>
        {all_rows}
      </table>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
