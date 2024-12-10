from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic_settings import BaseSettings
import clr
import os

from winGetPCInfo import get_gpu_load, get_ram_info, get_cpu_load_and_temperature

# Импортируем библиотеку LibreHardwareMonitor
current_dir = os.path.dirname(os.path.abspath(__file__))
library_path = os.path.join(current_dir, '..\lib', 'LibreHardwareMonitorLib.dll')
clr.AddReference(library_path)
from LibreHardwareMonitor.Hardware import Computer, HardwareType, SensorType

# Инициализация объекта Computer
computer = Computer()
computer.IsCpuEnabled = True  # Включаем мониторинг процессора
computer.IsGpuEnabled = True  # Включаем мониторинг видеокарты
computer.IsMemoryEnabled = True  # Включаем мониторинг памяти
computer.IsMotherboardEnabled = True  # Включаем мониторинг материнской платы
computer.Open()

# Конфигурация приложения через Pydantic Settings
class Settings(BaseSettings):
    host: str = "0.0.0.0"  # Адрес, на котором запускается приложение
    port: int = 5000       # Порт, на котором запускается приложение

    class Config:
        env_file = ".env"  # Поддержка загрузки конфигурации из файла .env

settings = Settings()

# Создание FastAPI приложения
app = FastAPI()

# Разрешаем CORS-запросы
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешаем запросы с любых доменов
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/getPcStatus")
def get_pc_status():
    gpu_load, gpu_temperature, gpu_memory_total, gpu_memory_used, gpu_fan_speeds = get_gpu_load(computer, HardwareType, SensorType)
    cpu_load, cpu_temperature, fan_speed = get_cpu_load_and_temperature(computer, HardwareType, SensorType)
    ram_total, ram_used = get_ram_info(computer, HardwareType, SensorType)

    pc_status = {
        "cpu": {
            "load": round(cpu_load),
            "temperature": round(cpu_temperature),
            "fanSpeed": round(fan_speed),
        },
        "gpu": {
            "load": gpu_load,
            "temperature": gpu_temperature,
            "memory": {
                "total": round(gpu_memory_total / 1024),
                "used": round(gpu_memory_used / 1024),
            },
            "fanSpeed": gpu_fan_speeds,
        },
        "ram": {
            "total": round(ram_total),
            "used": round(ram_used),
        },
    }

    print("Запрос на получение информации о сервере")
    print(pc_status)

    return pc_status

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.host, port=settings.port)
