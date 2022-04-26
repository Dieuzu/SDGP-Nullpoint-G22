def Jsonfinder():
    import os
    import Json
    import time

    start_time = time.time()
    for root,dirs,files in os.walk('output\\RAW\\'):
        for file in files:
                if file.endswith('.txt'):
                    if(os.path.join(root,file) == 'output\\RAW\\Task_1.txt'):
                       Json.Json(os.path.join(root,file)) 
                    if(os.path.join(root,file) == 'output\\RAW\\Task_2.txt'):
                       Json.Json(os.path.join(root,file)) 
                    if(os.path.join(root,file) == 'output\\RAW\\Task_3.txt'):
                       Json.Json(os.path.join(root,file)) 
    
    sttime = time.time() - start_time
    format_float = "{:.2f}".format(sttime)
    print("[SYSTEM] "+format_float+" Seconds took to finished to do separate txt part\n")