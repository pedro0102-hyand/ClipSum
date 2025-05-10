from flask import Flask, request, jsonify, render_template
from threading import Thread
from transformers import T5ForConditionalGeneration, T5Tokenizer
import pyperclip
import time
import re

app = Flask(__name__)

# Carrega o modelo leve e funcional
model = T5ForConditionalGeneration.from_pretrained("t5-small")
tokenizer = T5Tokenizer.from_pretrained("t5-small")

shared_data = {"original": "", "summary": ""}


def limpar_texto(texto):
    texto = re.sub(r'\[\d+\]', '', texto)
    texto = re.sub(r'[^\w\s,.!?;çáéíóúãõêôâÁÉÍÓÚÃÕÊÔÂ]', '', texto)
    return texto.strip()


def summarize_text(text):
    input_text = "summarize: " + text
    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
    output_ids = model.generate(input_ids, max_length=100, min_length=20, length_penalty=2.0, num_beams=4)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)


def clipboard_monitor():
    last_text = ""
    while True:
        try:
            current = pyperclip.paste()
            current = limpar_texto(current)
            if current != last_text and len(current.split()) > 8:
                last_text = current
                summary = summarize_text(current)
                shared_data["original"] = current
                shared_data["summary"] = summary
        except Exception as e:
            print("Erro:", e)
        time.sleep(2)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/get_data')
def get_data():
    return jsonify(shared_data)


if __name__ == "__main__":
    Thread(target=clipboard_monitor, daemon=True).start()
    app.run(debug=True)




