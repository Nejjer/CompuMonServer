import psutil

def get_memory_info():
    # Получаем информацию о памяти
    memory_info = psutil.virtual_memory()
    
    # Преобразуем значения в гигабайты
    total_memory = round(memory_info.total / (1024 ** 3), 2)  # Общее количество памяти
    used_memory = round(memory_info.used / (1024 ** 3), 2)    # Используемая память
    
    return {
        'total_memory': total_memory,
        'used_memory': used_memory
    }

# Пример использования
memory_info = get_memory_info()

