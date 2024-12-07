import psutil

def get_cpu_usage():
    # Получаем использование CPU в процентах
    cpu_usage = psutil.cpu_percent(interval=1, percpu=False)
    return cpu_usage

# Пример использования
cpu_usage = get_cpu_usage()
