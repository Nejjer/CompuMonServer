def get_cpu_load_and_temperature(computer, HardwareType, SensorType):
    cpu_load = 0
    cpu_temperature = 0
    fan_speed = 0
    for hardware in computer.Hardware:
        if hardware.HardwareType == HardwareType.Cpu:
            hardware.Update()
            for sensor in hardware.Sensors:
                if sensor.SensorType == SensorType.Load and "Total" in sensor.Name:
                    cpu_load = sensor.Value
                elif sensor.SensorType == SensorType.Temperature:
                    if cpu_temperature != 0:
                        continue
                    cpu_temperature = sensor.Value
        elif hardware.HardwareType == HardwareType.Motherboard:
            hardware.Update()
            for subHardware in hardware.SubHardware:
                subHardware.Update()
                for sensor in subHardware.Sensors:
                    if sensor.SensorType == SensorType.Fan:
                        if fan_speed != 0:
                            continue
                        fan_speed = sensor.Value


    return cpu_load, cpu_temperature, fan_speed


def get_gpu_load(computer, HardwareType, SensorType):
    gpu_load = 0
    gpu_temperature = 0
    gpu_memory_total = 0
    gpu_memory_used = 0
    gpu_fan_speeds = 0

    for hardware in computer.Hardware:
        if hardware.HardwareType in (HardwareType.GpuNvidia, HardwareType.GpuAmd):
            hardware.Update()
            for sensor in hardware.Sensors:
                if sensor.SensorType == SensorType.Load:
                    if gpu_load != 0:
                        continue
                    gpu_load = sensor.Value
                elif sensor.SensorType == SensorType.Temperature:
                    if gpu_temperature != 0:
                        continue
                    gpu_temperature = sensor.Value
                elif sensor.SensorType == SensorType.SmallData:
                    if "GPU Memory Total" in sensor.Name:
                        gpu_memory_total = sensor.Value
                    elif "GPU Memory Used" in sensor.Name:
                        gpu_memory_used = sensor.Value
                elif sensor.SensorType == SensorType.Fan:
                    gpu_fan_speeds = sensor.Value

    return gpu_load, gpu_temperature, gpu_memory_total, gpu_memory_used, gpu_fan_speeds


def get_ram_info(computer, HardwareType, SensorType):
    rav_available = 0
    ram_used = 0

    for hardware in computer.Hardware:
        if hardware.HardwareType == HardwareType.Memory:
            hardware.Update()
            for sensor in hardware.Sensors:
                if sensor.SensorType == SensorType.Data:
                    if "Memory Used" in sensor.Name:
                        if ram_used != 0:
                            continue
                        ram_used = sensor.Value
                    elif "Memory Available" in sensor.Name:
                        if rav_available != 0:
                            continue
                        rav_available = sensor.Value
    ram_total = rav_available + ram_used
    return ram_total, ram_used
