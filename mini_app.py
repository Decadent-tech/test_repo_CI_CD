from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/panda")
def hello_panda():
    return "<p>Hello, PANDA!</p>"

@app.route("/ping")
def hello_ping():
    return {'message':'Hi, I am a JSON REPLY'}

if __name__ == "__main__":
    app.run()

# To run the app, use the command: python mini_app.py