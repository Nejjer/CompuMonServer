from flask import Flask, jsonify
from flask_cors import CORS  # Импортируем CORS
from getCpuTemp import get_cpu_temperature_inxi
from getMemory import get_memory_info
from getCpuUsage import get_cpu_usage
from getFanSpeed import get_fan_speed_inxi
import threading
import time

# Глобальные переменные для хранения результатов
cpu_usage_per_core = None
avg_temperature = None

# Функция для обновления загрузки процессора
def update_cpu_usage():
    global cpu_usage_per_core
    while True:
        cpu_usage_per_core = get_cpu_usage()
        print(f"Обновление загрузки процессора: {cpu_usage_per_core}")
        time.sleep(0.1)

# Функция для обновления температуры процессора
def update_cpu_temperature():
    global avg_temperature
    while True:
        avg_temperature = get_cpu_temperature_inxi()
        print(f"Обновление температуры процессора: {avg_temperature}")
        time.sleep(0.5)


# Запускаем потоки для обновления данных
thread_cpu_usage = threading.Thread(target=update_cpu_usage, daemon=True)
thread_cpu_temperature = threading.Thread(target=update_cpu_temperature, daemon=True)

thread_cpu_usage.start()
thread_cpu_temperature.start()

app = Flask(__name__)
CORS(app)  # Разрешаем все CORS-запросы

@app.route('/api/getPcStatus', methods=['GET'])
def get_cpu_status():

    memory_info = get_memory_info()
    fan_info = get_fan_speed_inxi()
    # Формируем ответ в заданном формате

    pc_status = {
        "cpu": {
            "load": cpu_usage_per_core,
            "temperature": avg_temperature,
            'fanSpeed': fan_info
        },
        "ram": {
            "total": memory_info['total_memory'],
            "used": memory_info['used_memory']
        }
    }

    print('Запрос на получение инфы о сервере')
    print(pc_status)

    return jsonify(pc_status)

if __name__ == '__main__':
    app.run(host='192.168.1.119', port=5000)
