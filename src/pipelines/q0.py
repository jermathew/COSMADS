from data_services.database import GetSerialCamera1IdFromDiecutterId
from data_services.database import GetSerialCamera2IdFromDiecutterId
from data_services.database import GetDiecuttersIdOfFactory

def pipeline_function():
    serial_number = 88888404

    results = []

    diecutters_ids = GetDiecuttersIdOfFactory.call()
    for diecutter_id in diecutters_ids:
        serial_camera1 = GetSerialCamera1IdFromDiecutterId.call(diecutter_id=diecutter_id)
        serial_camera2 = GetSerialCamera2IdFromDiecutterId.call(diecutter_id=diecutter_id)
        if serial_camera1 == serial_number:
            camera_type = "camera1"
            results.append({
                'serial number': serial_number,
                'diecutter_id': diecutter_id,
                'type': camera_type
            })
            break
        elif serial_camera2 == serial_number:
            camera_type = "camera2"
            results.append({
                'serial number': serial_number,
                'diecutter_id': diecutter_id,
                'type': camera_type
            })
            break
    
    return results