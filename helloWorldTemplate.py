'''
Code Created by Taurean Branch
'''

from flask import Flask, render_template, request, jsonify, url_for, redirect
from datetime import datetime
import csv

app = Flask(__name__)
@app.route('/')

def index():
    now = datetime.datetime.now()
    timeString = now.strftime("%m-%d-%Y %H:%M")

    with open('gardendata.csv', 'r') as csvfile:
	    reader = csv.reader(csvfile)
        last_row = list(reader)[-1]
        time = last_row[0]
        newtime = datetime.strptime(time,"%Y-%m-%dT%H:%M:%SZ")
        newtime = newtime.strft(time, "%m-%d-%y %H:%M")
        temperature = last_row[1]
        humidity = last_row[2]
        light = last_row[3]
            
    templateData =  {
        'title': 'Hello',
        'time' : newtime,
        'temperature': temperature,
        'humidity': humidity,
        'light': light
        }

    return render_template('index.html', **templateData)


@app.route('/gardendata', methods=['POST'])
def handle_gardendata():
    data = request.json
    time = data['timestamp']
    readings = data['readings']
    temperature = (readings['temperature'] * 9/5)+32
    humidity = readings['humidity']
    light = readings['luminance']

    with open('gardendata.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([time,temperature, humidity, light])

    return jsonify(success=True)

if __name__ == '__main__':
        app.run(debug=True, port=80, host='0.0.0.0')






