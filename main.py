from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello,I am Pragati and I am new to this project  and this is my project to deploying through CI/CD pileline V1.0!"

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port= 8080)
