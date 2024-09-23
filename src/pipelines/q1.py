from data_services.diecutter import GetCurrentDataFromChip
from data_services.database import GetDiecutterChipIdFromDiecutterId
import time

def pipeline_function():
    diecutter_id = 6
    
    chip_id = GetDiecutterChipIdFromDiecutterId.call(diecutter_id=diecutter_id)
        
    temperatures = []
    start_time = time.time()
    end_time = start_time + 60
    while time.time() <= end_time:
        current_data = GetCurrentDataFromChip.call(chip_id=chip_id)
        temperatures.append(current_data["temperature"])
        time.sleep(1)
    average_temperature = sum(temperatures)/len(temperatures)
    results = {
        'start_timestamp': time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(start_time)),
        'end_timestamp': time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(end_time)),
        'average_temperature': average_temperature
    }
    return [results]