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
    data = request.json
    time = data['timestamp']
    readings = data['readings']
    temperature = readings['temperature']
    humidity = readings['humidity']
    light = readings['light']

    with open('gardendata.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([time,temperature, humidity, light])

    response_data = {
        'lastUpdate': time,
        'lastTemp': temperature,
        'lastHumidity' : humidity,
        'light' : light
    }

    return jsonify(response_data)

if __name__ == '__main__':
        app.run(debug=True, port=80, host='0.0.0.0')






