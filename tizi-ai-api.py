from flask import Flask, request, jsonify
import tiziai
import threading

app = Flask(__name__)

def chat_completion(model, messages):
    response = tiziai.ChatCompletion.create(model=model, provider=tiziai.Provider.DeepAi, messages=messages, stream=False, temperature=0.5, max_tokens=8192, frequency_penalty=0, top_p=0)
    return response

def chat_completion1(model, messages):
    response = tiziai.ChatCompletion.create(model=model, provider=tiziai.Provider.GetGpt, messages=messages, stream=False, temperature=0.5, max_tokens=8192, frequency_penalty=0, top_p=0)
    return response

def chat_completion2(model, messages):
    response = tiziai.ChatCompletion.create(model=model, provider=tiziai.Provider.H2o, messages=messages, stream=False, temperature=0.5, max_tokens=8192, frequency_penalty=0, top_p=0)
    return response

@app.route('/api/v1/gpt-3.5-tubo', methods=['POST'])
def chat():
    data = request.get_json()
    
    model = data.get('model', 'gpt-3.5-turbo')

    messages = data.get('messages', [])

    response = chat_completion(model, messages)
    
    return jsonify(response)

@app.route('/api/v2/gpt-3.5-tubo', methods=['POST'])
def chat():
    data = request.get_json()
    
    model = data.get('model', 'gpt-3.5-turbo')

    messages = data.get('messages', [])

    response = chat_completion1(model, messages)
    
    return jsonify(response)

@app.route('/api/v3/gpt-3.5-tubo', methods=['POST'])
def chat():
    data = request.get_json()
    
    model = data.get('model', 'gpt-3.5-turbo')

    messages = data.get('messages', [])

    response = chat_completion2(model, messages)
    
    return jsonify(response)

if __name__ == '__main__':
    app.run()
