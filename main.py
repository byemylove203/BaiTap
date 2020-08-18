from flask import Flask
from flask import render_template
from flask import request
from utils import *

app = Flask(__name__)
 
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST': 
        data=standartdized(request.form['input'])
        strLen=getLen(data)
        wordCount = count(data)
        return render_template('index.html',data=data,strLen=strLen,wordCount=wordCount)
    return render_template('index.html')
 
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
 
 