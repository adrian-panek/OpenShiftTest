from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Deployed with OpenShift, tutorial"

@app.route('/<phrase>')
def hello_name(phrase):
   return '%s' % phrase

if __name__ == "__main__":
    app.run()