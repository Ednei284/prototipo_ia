from flask import Flask, request, jsonify
import text_to_speech as ts

app = Flask(__name__)

@app.route('/image')
def image():
    return '/image'

@app.route('/text', methods=['GET'])
def text():
    return '/text'

@app.route('/audio', methods=['POST'])
def audio():
    res_analise = ts.speech_text()
    return res_analise

@app.route('/video', methods=['POST'])
def video():
    return '/video'

if __name__ == "__main__":
    app.run(debug=True)
