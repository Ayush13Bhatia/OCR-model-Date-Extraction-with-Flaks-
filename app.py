import numpy as np
from flask import Flask,render_template
import pickle
import random
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/extract',methods=['POST'])
def extract():
    '''
    For rendering results on HTML GUI
    '''
    i, j = random.choice(list(model.items()))
    if j == []:
        return render_template('index.html', Extract_date = f'Extract file name:- {i} Extract date:- {"Null"}')
    return render_template('index.html', Extract_date = f'Extract file name:- {i}  Extract date:- {j.pop()}')


if __name__ == "__main__":
    app.run(debug=True)

