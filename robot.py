from flask import Flask, request, jsonify
from flask_cors import CORS
from chatterbot import ChatBot
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Family Guy Session 4 Ep 21'
app.config['CORS_HEADERS'] = 'Content-Type'

origin = os.environ.get('ORIGIN')
cors = CORS(app, resources={r"/": {"origins": origin}})

chatbot = ChatBot("BulBul")


@app.route("/", methods=['POST'])
def index():
    content = request.json
    question = content['question'].strip()
    # print(content['question'].strip(), flush=True)
    answer = chatbot.get_response(question).text
    response = jsonify({"answer": answer})
    return response