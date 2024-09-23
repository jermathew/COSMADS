from data_services.diecutter import GetCurrentDataFromChip
from data_services.database import GetDiecutterChipIdFromDiecutterId
import time

def pipeline_function():
    diecutter_id = 25
    chip_id = GetDiecutterChipIdFromDiecutterId.call(diecutter_id=diecutter_id)
    
    results = []
    for window in range(3):
        temperatures = []
        rotations = 0
        start_time = time.time()
        while time.time() - start_time < 30:
            current_data = GetCurrentDataFromChip.call(chip_id=chip_id)
            temperatures.append(current_data['temperature'])
            rotations = current_data['rotations']
            time.sleep(1)
        end_time = time.time()
        
        average_temperature = sum(temperatures)/len(temperatures)
        results.append({
            'window': window + 1,
            'rotations': rotations,
            'average_temperature': average_temperature,
            'start_timestamp': time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(start_time)),
            'end_timestamp': time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(end_time))
        })
    
    return results