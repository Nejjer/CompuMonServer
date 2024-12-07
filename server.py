from flask import Flask, jsonify
from flask_cors import CORS  # Импортируем CORS
import clr


from winGetPCInfo import get_gpu_load, get_ram_info, get_cpu_load_and_temperature

clr.AddReference("F:\Downloads\LibreHardwareMonitor-net472\LibreHardwareMonitorLib.dll")
from LibreHardwareMonitor.Hardware import Computer, HardwareType, SensorType

# Инициализация объекта Computer
computer = Computer()
computer.IsCpuEnabled = True  # Включаем мониторинг процессора
computer.IsGpuEnabled = True  # Включаем мониторинг видеокарты
computer.IsMemoryEnabled = True  # Включаем мониторинг видеокарты
computer.IsMotherboardEnabled = True  # Включаем мониторинг видеокарты
computer.Open()

app = Flask(__name__)
CORS(app)  # Разрешаем все CORS-запросы

@app.route('/api/getPcStatus', methods=['GET'])
def get_cpu_status():
    gpu_load, gpu_temperature, gpu_memory_total, gpu_memory_used, gpu_fan_speeds = get_gpu_load(computer, HardwareType, SensorType)
    cpu_load, cpu_temperature, fan_speed = get_cpu_load_and_temperature(computer, HardwareType, SensorType)
    ram_total, ram_used = get_ram_info(computer, HardwareType, SensorType)
    # Формируем ответ в заданном формате
    pc_status = {
        "cpu": {
            "loads": round(cpu_load),
            "temperatures": round(cpu_temperature),
            'fanSpeed': round(fan_speed)
        },
        "gpu": {
            "loads": gpu_load,
            "temperatures": gpu_temperature,
            "memory": {
                "total": round(gpu_memory_total / 1024),
                "used": round(gpu_memory_used / 1024),
            },
            "fanSpeed": gpu_fan_speeds
        },
        "ram": {
            "total": round(ram_total),
            "used": round(ram_used)
        }
    }

    print('Запрос на получение инфы о сервере')
    print(pc_status)

    return jsonify(pc_status)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
