from data_services.camera1 import GetFrameFromCamera1
from data_services.camera1 import DetectErrorsInCardboardUsingCamera1
from data_services.database import GetCamera1IdFromDiecutterId

def pipeline_function():
    diecutter_id = 1
    num_cardboards = 5
    no_defects_count = 0
    with_errors_count = 0
    hole_errors_count = 0
    fold_errors_count = 0
    
    camera1_id = GetCamera1IdFromDiecutterId.call(diecutter_id=diecutter_id)
    
    for _ in range(num_cardboards):
        frame = GetFrameFromCamera1.call(camera1_id=camera1_id)
        has_error, type_error = DetectErrorsInCardboardUsingCamera1.call(camera1_id=camera1_id, frame=frame)
        if has_error:
            if type_error == 1:
                hole_errors_count += 1
            elif type_error == 2:
                fold_errors_count += 1
            with_errors_count += 1
        else:
            no_defects_count += 1
    
    results = [{
        'no_defects_count': no_defects_count,
        'with_errors_count': with_errors_count,
        'hole_errors_count': hole_errors_count,
        'fold_errors_count': fold_errors_count
    }]
    return results