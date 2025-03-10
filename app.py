# backend/app.py
from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
import pickle
from keras.utils import pad_sequences # type: ignore
import os
model_path = os.path.join(os.path.dirname(__file__), "chatbot.h5")



app = Flask(__name__, static_folder='../frontend', template_folder='../frontend')
# Load the trained model and tokenizer
model = tf.keras.models.load_model(model_path)
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# Use the same max length as used during training for padding.
max_len_q = model.input_shape[1]

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/chat", methods=["POST"])
# def chat():
    data = request.json
    user_input = data.get("message")
    # Tokenize and pad user input
    seq = tokenizer.texts_to_sequences([user_input])
    padded = pad_sequences(seq, maxlen=max_len_q, padding='post')
    
    # Predict next word (very simplified; a real chatbot would generate sequences)
    pred = model.predict(padded)
    pred_idx = np.argmax(pred, axis=1)[0]
    
    # Reverse lookup to find the word corresponding to the index
    response = None
    for word, idx in tokenizer.word_index.items():
        if idx == pred_idx:
            response = word
            break
    if response is None:
        response = "I don't know."
    
    return jsonify({"response": response})
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_input = data.get("message")
        print("Received user input:", user_input)
        
        # Tokenize input and pad the sequence
        seq = tokenizer.texts_to_sequences([user_input])
        print("Tokenized sequence:", seq)
        
        padded = pad_sequences(seq, maxlen=max_len_q, padding='post')
        print("Padded sequence shape:", padded.shape)
        
        # Convert padded sequences to one-hot encoded vectors
        one_hot_input = tf.keras.utils.to_categorical(padded, num_classes=model.input_shape[-1])

        print("One-hot input shape:", one_hot_input.shape)
        
        # Get model prediction using the one-hot encoded input
        pred = model.predict(one_hot_input)
        print("Model prediction (raw):", pred)
        
        pred_idx = np.argmax(pred, axis=1)[0]
        print("Predicted index:", pred_idx)
        
        # Use the tokenizer's reverse mapping for response
        response = tokenizer.index_word.get(pred_idx, "I don't know.")
        print("Returning response:", response)
        print("Tokenizer keys:", list(tokenizer.index_word.keys()))
        
        return jsonify({"response": response})
    except Exception as e:
        print("Error in /chat:", e)
        return jsonify({"response": "Error processing your request."}), 500


if __name__ == "__main__":
    app.run(debug=True)
