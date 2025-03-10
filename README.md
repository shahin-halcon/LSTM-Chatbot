# LSTM Chatbot 🤖

This project is a simple **AI-powered chatbot** built with an **LSTM (Long Short-Term Memory)** neural network. It demonstrates how deep learning can be used to create conversational AI capable of understanding and responding to user input.

The chatbot has both a **backend** (Python + Flask + TensorFlow) and a **frontend** (HTML, CSS, JavaScript), making it a complete, interactive application you can run locally or host on a server.

---

## 📂 Project Structure
```
chatbot-project/
├── backend/
│   ├── app.py           # Flask server code that loads the model and handles chat requests
│   ├── TrainChatbot.ipynb         # Script to build, train, and save the chatbot model
│   └── requirements.txt # Python dependencies
├── frontend/
│   ├── index.html       # HTML for the user interface
│   ├── style.css        # CSS styling for the UI
│   └── script.js        # JavaScript for sending/receiving messages
└── README.md            # Instructions and project overview
```

---

## ✨ Features
- **Deep Learning Model**: Uses an LSTM network for intent recognition and response generation.
- **Custom Training**: The model is trained on a dataset of intents (questions and answers).
- **Frontend UI**: A clean, minimal chat interface for user interaction.
- **API Integration**: Frontend and backend connected via RESTful API (Flask).

---

## 🚀 How It Works
1. **Training**: The `TrainChatbot.ipynb` script processes intents data, tokenizes text, and trains the LSTM model.
2. **Serving**: `app.py` loads the trained model and serves it using Flask. It accepts chat messages and returns responses.
3. **User Interface**: `index.html`, `style.css`, and `script.js` create a responsive chat interface that interacts with the Flask API.

---

## 🛠️ Tech Stack
- **Backend**: Python, Flask, TensorFlow/Keras
- **Frontend**: HTML, CSS, JavaScript
- **Model**: LSTM neural network

---

## 📌 How to Run
1. **Clone the repo**
   ```bash
   git clone https://github.com/shahin-halcon/LSTM-Chatbot.git
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Train the model**
   TrainChatbot.ipynb
4. **Run the Flask server**
   ```bash
   python app.py
   ```
