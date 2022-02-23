from flask import Flask

app = Flask(__name__)

#remember to put 2 empty lines between functions
@app.route('/')
def hello_world():
    return ('Hello World!')





if __name__ == '__main__':
    app.run()