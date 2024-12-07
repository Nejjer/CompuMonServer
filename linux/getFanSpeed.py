import subprocess

def get_fan_speed_inxi():
    try:
        # Выполняем команду inxi для получения информации о температуре
        result = subprocess.run(['inxi', '-s'], capture_output=True, text=True, check=True)
        
        # Извлекаем из вывода строку с температурой процессора
        output = result.stdout
        
        # Ищем строку, содержащую информацию о температуре процессора
        for line in output.splitlines():
            if "Fan Speeds (RPM): cpu:" in line:
                # Возвращаем строку с температурой процессора
                return int(line.split(':')[2][:5])
        
        return "Температура процессора не найдена."
    
    except subprocess.CalledProcessError as e:
        return f"Ошибка выполнения команды inxi: {e}"
    except FileNotFoundError:
        return "Утилита inxi не установлена."

