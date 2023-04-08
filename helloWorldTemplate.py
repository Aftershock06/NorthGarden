'''
Code Created by Taurean Branch
'''

from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)
@app.route('/')

def index():
        now = datetime.datetime.now()
        timeString = now.strftime("%m-%d-%Y %H:%M")
        templateData =  {
                'title': 'Hello',
                'time' : timeString
                }
        return render_template('index.html', **templateData)


if __name__ == '__main__':
        app.run(debug=True, port=80, host='0.0.0.0')






