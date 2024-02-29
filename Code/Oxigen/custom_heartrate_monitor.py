
from hrmonitor import HeartRateMonitor
import time

def monitor_heart_rate_and_spo2():
    hrm = HeartRateMonitor(print_raw=False, print_result=False)
    hrm.start_sensor()

    try:
        print("Monitoreo de la frecuencia cardíaca y oxigenación iniciado. Presiona CTRL+C para detener.")
        while True:
            if hrm.bpm > 0 and hrm.spo2 > 0:  # Asegura que hay valores válidos
                print(f"BPM actual: {hrm.bpm}, SpO2 actual: {int(hrm.spo2)}%")
            if hrm.bpm == 0:
                print("No se detectó el dedo")    
            time.sleep(1)  # Espera un segundo antes de leer el siguiente valor
    except KeyboardInterrupt:
        print("Deteniendo el monitoreo...")
    finally:
        hrm.stop_sensor()

if __name__ == "__main__":
    monitor_heart_rate_and_spo2()

