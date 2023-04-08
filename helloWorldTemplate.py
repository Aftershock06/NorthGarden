'''
Code Created by Taurean Branch
'''

from flask import Flask, render_template, request, jsonify
import datetime
import csv

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


@app.route('/gardendata', methods=['POST'])
def handle_gardendata():
    now = datetime.datetime.now()
    timeString = now.strftime("%m-%d-%Y %H:%M")
    data = request.json
    temperature = data['temperature']
    humidity = data['humidity']
    light = data['light']

    with open('gardendata.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([timeString,temperature, humidity, light])

    response_data = {
        'lastUpdate': timeString,
        'lastTemp': temperature,
        'lastHumidity' : humidity,
        'light' : light
    }

    return jsonify(response_data)

if __name__ == '__main__':
        app.run(debug=True, port=80, host='0.0.0.0')






