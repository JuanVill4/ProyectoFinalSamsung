
from flask import Flask, render_template, jsonify
import threading
import random

app = Flask(__name__)

# Simulando datos del sensor para el ejemplo
latest_data = {'heart_rate': 75, 'oxygen_level': 98}

def simulate_sensor_data():
    global latest_data
    while True:
        latest_data = {
            'heart_rate': random.randint(60, 100),
            'oxygen_level': random.randint(95, 100)
        }

# Inicia el thread para simular la lectura de datos del sensor
sensor_thread = threading.Thread(target=simulate_sensor_data, daemon=True)
sensor_thread.start()

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/data')
def data():
    return jsonify(latest_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
