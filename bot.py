from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_data(as_text=True)
    with open("signal.txt", "w") as f:
        f.write(data)
    return "Signal reçu", 200

@app.route('/show-signal', methods=['GET'])
def show_signal():
    if os.path.exists("signal.txt"):
        with open("signal.txt", "r") as f:
            return f.read(), 200
    return "Aucun signal reçu", 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
