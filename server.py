from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({'message': 'Hello from your laptop!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

response = requests.get('http://192.168.245.164:5000')
print(response.json())