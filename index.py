from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/searchLanguage', methods=['POST'])
def searchLanguage():
    username = str(request.form['username']).lower()    
    language = str(request.form['language']).lower()
    github = str('https://github.com/')
    complementation = str('?utf8=%E2%9C%93&tab=repositories&q=&type=&language=')
    os.startfile(github + username + complementation + language)
    return index()

if __name__ == "__main__":
    app.run(debug=True)    