# 🤖 OpenAI Streamlit Chatbot

A simple yet powerful conversational AI chatbot built with OpenAI's GPT models and Streamlit. Includes real-time conversation, memory (chat history), and auto-saving of conversations.

---

## ✨ Features

- 💬 Chat with GPT-3.5 or GPT-4 in real time
- 🧠 Maintains full chat history in memory
- 💾 Automatically saves each chat session to a timestamped `.json` file
- 🌐 Beautiful, minimal web UI using Streamlit

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/omovigho/openai-streamlit-chatbot.git
cd openai-streamlit-chatbot
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install openai streamlit
```

### 3. Set Your OpenAI API Key

```bash
export OPENAI_API_KEY=your-api-key-here
```

### 4. Run the Chatbot

```bash
streamlit run ai_chatbot_openai.py
```

---

## 🗂 Project Structure

```
├── ai_chatbot_openai.py   # Main chatbot code
├── requirements.txt       # Python dependencies
├── chat_*.json            # Auto-saved chat logs
└── README.md              # Documentation
```

---

## 📦 Future Improvements

* Toggle between GPT-3.5 and GPT-4
* Export to `.txt` or `.csv`
* Deploy with Streamlit Cloud or Hugging Face Spaces

---

## 📄 License

MIT License — use freely and modify for your own AI products.

---

## 🤝 Contributing

PRs and feature requests are welcome! Fork and submit a pull request to contribute.

```