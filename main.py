from flask import Flask
from flask import render_template
from flask import request
from utils import *

app = Flask(__name__)
 
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST': 
        string = request.form['input']
        diachi = Diachi(string)
        quan= Quan(string)
        tinhthanh = Tinhthanh(string)
        return render_template('index.html',quan=quan,diachi=diachi,tinhthanh=tinhthanh)
    return render_template('index.html')
 
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
 
 