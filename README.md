# 🩺 Doctor Agent

Doctor Agent is a smart symptom checker built with **Python** and **Streamlit** that performs preliminary health triage, estimates urgency, suggests possible conditions, and recommends the right medical specialist.

## 🚀 Features

- 🧠 Smart symptom analysis
- ⚡ Urgency triage (routine / early consultation / urgent)
- 👨‍⚕️ Specialist recommendation
- 💬 Interactive symptom input
- 🎨 Clean healthcare-themed UI

## 📸 Preview

![Doctor Agent Home](assets/screenshot-home.png)

---

## 📂 Project Structure

```bash
doctor-agent/
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── LICENSE
│
├── data/
│   └── symptoms_data.json
│
├── utils/
│   ├── __init__.py
│   ├── symptom_checker.py
│   ├── triage.py
│   ├── specialist.py
│   └── prompts.py
│
├── assets/
│   ├── screenshot-home.png
│   └── logo.png
│
└── .github/
    └── workflows/
        └── python-app.yml
