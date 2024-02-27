from flask import Flask, render_template, jsonify
from threading import Thread
import time
import sys
from pathlib import Path

# Agrega la carpeta Oxigen al sys.path
oxigen_path = Path(__file__).resolve().parent / 'Oxigen'
sys.path.append(str(oxigen_path))

# Ahora puedes importar desde Oxigen sin problemas
from hrmonitor import HeartRateMonitor

app = Flask(__name__)

# Variable global para almacenar los últimos datos
latest_data = {"heart_rate": 0, "oxygen_level": 0}

def update_sensor_data():
    hrm = HeartRateMonitor(print_raw=False, print_result=False)
    hrm.start_sensor()
    try:
        while True:
            if hrm.bpm > 0 and hrm.spo2 > 0:
                global latest_data
                latest_data = {"heart_rate": hrm.bpm, "oxygen_level": int(hrm.spo2)}
            time.sleep(1)
    finally:
        hrm.stop_sensor()

# Inicia el hilo para actualizar los datos del sensor
sensor_thread = Thread(target=update_sensor_data, daemon=True)
sensor_thread.start()

@app.route('/')
def index():
    return render_template('index3.html')


@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(latest_data)

if __name__ == '__main__':
    app.run(debug=True)