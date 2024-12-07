import subprocess

def get_cpu_temperature_inxi():
    try:
        # Выполняем команду inxi для получения информации о температуре
        result = subprocess.run(['inxi', '-s'], capture_output=True, text=True, check=True)
        
        # Извлекаем из вывода строку с температурой процессора
        output = result.stdout
        
        # Ищем строку, содержащую информацию о температуре процессора
        for line in output.splitlines():
            if "System Temperatures: cpu:" in line:
                # Возвращаем строку с температурой процессора
                print(line)
                return float(line.split(':')[2][:5].strip())
        
        return "Температура процессора не найдена."
    
    except subprocess.CalledProcessError as e:
        return f"Ошибка выполнения команды inxi: {e}"
    except FileNotFoundError:
        return "Утилита inxi не установлена."

