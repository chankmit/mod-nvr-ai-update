import cv2
import numpy as np
from elements.yolo import OBJ_DETECTION
import time 
import configparser
from datetime import datetime, timedelta
import os
from PIL import Image
from csv import DictWriter
import requests

config = configparser.ConfigParser()
config.sections()
config.read('mod_config.ini')

is_opend_detection =int(config['DEFAULT']['is_opend_detection'])
detection_status = int(config['DEFAULT']['detection_status'])
process_num = int(config['DEFAULT']['process_num'])
show_result = int(config['DEFAULT']['show_result']) 
store_detected_image = int(config['DEFAULT']['store_detected_image']) 
store_detected_time_range = int(config['DEFAULT']['store_detected_time_range']) 
store_detected_location = str(config['DEFAULT']['store_detected_location'])  


is_notify = int(config['NOTIFY']['is_notify']) 
notify_time_range = int(config['NOTIFY']['notify_time_range']) 
notify_classes = config['NOTIFY']['notify_classes']
notify_token = str(config['NOTIFY']['notify_token'])


cam_01 = 'rtsp://admin:Things22@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif'
cam_02 = 'rtsp://admin:Things22@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif'
cam_03 = 'rtsp://admin:Things22@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif'
cam_04 = 'rtsp://admin:Things22@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif'

Object_classes = config['DEFAULT']['object_classes']
Object_detector = OBJ_DETECTION('weights/yolov5n.pt', Object_classes)
DISPLAY_LOCATION = str(config['DEFAULT']['org_name']) 
COLS_DETECT_INFO = ['name', 'confidence', 'image', 'location', 'year', 'month', 'date', 'time', 'timestamp']

if(process_num>0):
    cap01 = cv2.VideoCapture(cam_01)
    cam_size = (854, 480)
    full_size = (854, 480)
if(process_num>1):
    cap02 = cv2.VideoCapture(cam_02)
    cam_size = (640, 360)
    full_size = (1280, 360)
if(process_num>2):
    cap03 = cv2.VideoCapture(cam_03)
    cam_size = (640, 360)
    full_size = (1280, 720)
if(process_num>3):
    cap04 = cv2.VideoCapture(cam_04)
    cam_size =(640, 360)
    full_size = (1280, 720) 

if detection_status == 1:
    #window_handle = cv2.namedWindow("CSI Camera", cv2.WINDOW_AUTOSIZE)
    # Window
    box_color = (255, 0, 255)
    sendtime = datetime.now() 
    sendlinetime = datetime.now() 
    while True:
        start_time = time.time() 
        framerd = cv2.imread('bg.jpg')
        #print(framerd.shape)
        frame = cv2.resize(framerd, full_size)
        ret01 = ''
        ret02 = ''
        if(process_num==1):
            if cap01.isOpened():
                ret01, img01 = cap01.read()
                if ret01:
                    frame01 = cv2.resize(img01, cam_size) 
                    frame = frame01
                else : 
                    cap01 = cv2.VideoCapture(cam_01)
                
        if(process_num==2):
            if cap01.isOpened():
                ret01, img01 = cap01.read()
                if ret01:
                    frame01 = cv2.resize(img01, cam_size) 
                    frame[0:640, 0:640]=frame01 
                else : 
                    cap01 = cv2.VideoCapture(cam_01)
            if cap02.isOpened():
                ret02, img02 = cap02.read()
                if ret02:
                    frame02 = cv2.resize(img02, cam_size) 
                    frame[0:640, 640:1280]=frame02
                else : 
                    cap02 = cv2.VideoCapture(cam_02)

        if(process_num==3):
            if cap01.isOpened():
                ret01, img01 = cap01.read()
                if ret01:
                    frame01 = cv2.resize(img01, cam_size) 
                    frame[0:360, 0:640]=frame01
                else : 
                    cap01 = cv2.VideoCapture(cam_01)
            if cap02.isOpened():
                ret02, img02 = cap02.read()
                if ret02:
                    frame02 = cv2.resize(img02, cam_size) 
                    frame[0:360, 640:1280]=frame02 
                else : 
                    cap02 = cv2.VideoCapture(cam_02)
            if cap03.isOpened():
                ret03, img03 = cap03.read()
                if ret03:
                    frame03 = cv2.resize(img03, cam_size) 
                    frame[360:720, 0:640]=frame03
                else : 
                    cap03 = cv2.VideoCapture(cam_03)
                
        if(process_num==4):
            if cap01.isOpened():
                ret01, img01 = cap01.read()
                if ret01:
                    frame01 = cv2.resize(img01, cam_size) 
                    frame[0:360, 0:640]=frame01
                else : 
                    cap01 = cv2.VideoCapture(cam_01)
            if cap02.isOpened():
                ret02, img02 = cap02.read()
                if ret02:
                    frame02 = cv2.resize(img02, cam_size) 
                    frame[0:360, 640:1280]=frame02 
                else : 
                    cap02 = cv2.VideoCapture(cam_02)
            if cap03.isOpened():
                ret03, img03 = cap03.read()
                if ret03:
                    frame03 = cv2.resize(img03, cam_size) 
                    frame[360:720, 0:640]=frame03
                else : 
                    cap03 = cv2.VideoCapture(cam_03)
            if cap04.isOpened():
                ret04, img04 = cap04.read()
                if ret04:
                    frame04 = cv2.resize(img04, cam_size) 
                    frame[360:720, 640:1280]=frame04
                else : 
                    cap04 = cv2.VideoCapture(cam_04)
        
        TODAY_CODE = datetime.now().strftime('%Y-%m-%d')
        TODAY_Day = datetime.now().strftime('%d')
        TODAY_Month = datetime.now().strftime('%m')
        TODAY_Year = datetime.now().strftime('%Y')

        if ret01 or ret02 or ret03 or ret04:
            print(frame.shape)
            # detection process
            objs = Object_detector.detect(frame)
            
            # plotting
            for obj in objs:
                # print(obj)
                if obj['label'] in Object_classes:
                    label = obj['label']
                    score = obj['score']
                    [(xmin,ymin),(xmax,ymax)] = obj['bbox'] 
                    
                    #frame = cv2.rectangle(frame, (xmin,ymin), (xmax,ymax), color, 2) 
                    cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), box_color, 1)
                    # Top Left  x,y
                    cv2.line(frame, (xmin, ymin), (xmin+30, ymin), box_color, 5)
                    cv2.line(frame, (xmin, ymin), (xmin, ymin+30), box_color, 5) 
                    # Top Right  x1,y
                    cv2.line(frame, (xmax, ymin), (xmax-30, ymin), box_color, 5)
                    cv2.line(frame, (xmax, ymin), (xmax, ymin+30), box_color, 5)
                    # Bottom Left  x,y1
                    cv2.line(frame, (xmin, ymax), (xmin+30, ymax), box_color, 5)
                    cv2.line(frame, (xmin, ymax), (xmin, ymax-30), box_color, 5)
                    # Bottom Right  x1,y1
                    cv2.line(frame, (xmax, ymax), (xmax-30, ymax), box_color, 5)
                    cv2.line(frame, (xmax, ymax), (xmax, ymax-10), box_color, 5)
                    #cv2.rectangle( small_frame, (xmin-2, ymax + 10), (xmax+2, ymax-3), box_color, cv2.FILLED)
                    frame = cv2.putText(frame, f'{label} ({str(score)})', (xmin+10,ymin+15), cv2.FONT_HERSHEY_SIMPLEX , 0.40, box_color, 1, cv2.LINE_AA)
                    if store_detected_image ==1 and abs(datetime.now() - sendtime) > timedelta(seconds=store_detected_time_range): 
                        try:
                            DISPLAY_IMAGE = cv2.cvtColor(frame[ymin:ymax, xmin:xmax], cv2.COLOR_BGR2RGB)
                            STORAGE_FOLDER = "detected_images/"+str(TODAY_CODE)
                            if not os.path.exists(STORAGE_FOLDER): 
                                os.mkdir(STORAGE_FOLDER)
                            
                            FILE_NAME = STORAGE_FOLDER+"/"+str(time.time())+"_"+str(label)+".jpg"
                            cv2.imwrite(FILE_NAME, DISPLAY_IMAGE[:, :, ::-1])
                            PATH_DETECT_DATA = "detected_images/"+str(TODAY_CODE)+'-detection.csv'
                            dict={'name':str(label), 'confidence': str(score), 'image':str(FILE_NAME), 'location':DISPLAY_LOCATION, 'year':str(TODAY_Year), 'month':str(TODAY_Month), 'date':str(TODAY_Day), 'time': str(datetime.now().strftime('%H:%M:%S')), 'timestamp':str(time.time())}
                            if not os.path.isfile(PATH_DETECT_DATA): 
                                with open(PATH_DETECT_DATA, 'a', encoding='UTF8', newline='') as f_object:
                                    dictwriter_object = DictWriter(f_object, fieldnames=COLS_DETECT_INFO)
                                    dictwriter_object.writeheader()
                                    dictwriter_object.writerow(dict)
                                    f_object.close()                        
                            else: 
                                with open(PATH_DETECT_DATA, 'a', encoding='UTF8', newline='') as f_object:
                                    dictwriter_object = DictWriter(f_object, fieldnames=COLS_DETECT_INFO)
                                    #dictwriter_object.writeheader()
                                    dictwriter_object.writerow(dict)
                                    f_object.close()
                            sendtime = datetime.now() 
                            if is_notify == 1 and obj['label'] in notify_classes:
                                if abs(datetime.now() - sendlinetime) > timedelta(seconds=notify_time_range):
                                    try:
                                        file = {'imageFile':open(FILE_NAME,'rb')}
                                        data = ({
                                                'message':'Object Detection Notify'
                                            })
                                        LINE_HEADERS = {"Authorization":"Bearer "+notify_token}
                                        session = requests.Session()
                                        r=session.post('https://notify-api.line.me/api/notify', headers=LINE_HEADERS, files=file, data=data)
                                        sendlinetime = datetime.now() 
                                    except:
                                        print('can not send notify')
                        except:
                            print('empty image')


                            
        if show_result ==1:
            cv2.imshow("MOD-AI: Video Analytics", frame) 
        print("FPS: ", 1.0 / (time.time() - start_time))
        keyCode = cv2.waitKey(30)
        if keyCode == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
else:
    print("Unable to open camera")
