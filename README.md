# Ai-MCQ-Generator

# 📚 Automated Study Buddy Quiz Generator

An AI-powered web application that acts as your personal study assistant. Simply paste a link to an educational article or Wikipedia page, and the app will instantly read the text and generate an interactive multiple-choice quiz to test your knowledge!

This project was built as an MCA Major Project to demonstrate the integration of Web Scraping, Artificial Intelligence (LLMs), and modern UI/UX design using pure Python.

## ✨ Features
* **Automated Web Scraping:** Uses `BeautifulSoup` to safely extract readable text from web pages while bypassing basic bot-protections.
* **AI-Powered Generation:** Integrates Google's **Gemini 2.5 Flash** AI to comprehend complex text and formulate accurate quiz questions.
* **Beautiful User Interface:** Built entirely in Python using **Streamlit**, featuring interactive buttons, loading states, and clean markdown formatting.
* **No Database Required:** Processes everything in real-time, making the application lightweight and incredibly fast.

## 🛠️ Technology Stack
* **Language:** Python 3.13+
* **Frontend/UI:** Streamlit
* **AI API:** Google Generative AI (Gemini)
* **Web Scraping:** BeautifulSoup4, Requests

---

## 🚀 How to Install and Run This Project

Follow these simple steps to run the application on your own computer.

### Prerequisites
1. You must have **Python** installed on your computer. (Download it from [python.org](https://www.python.org/downloads/)). *Make sure to check "Add Python to PATH" during installation.*
2. You need a free **Google Gemini API Key**. (Get one from [Google AI Studio](https://aistudio.google.com/)).

### Step-by-Step Installation

**1. Download the Project**
Download or clone this repository to your computer and open the folder in your code editor (like VS Code).

**2. Open the Terminal**
Open your terminal or Command Prompt inside the project folder.

**3. Create a Virtual Environment (Recommended)**
This keeps the projectHere is the entire README file in a single block. You can just click the small "Copy" button in the top right corner of this box, and then paste it directly into tools separate from your main computer. Run this command:
```bash
python -m venv venv
