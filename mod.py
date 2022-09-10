import cv2
import numpy as np
from elements.yolo import OBJ_DETECTION
import time 

is_opend_detection =1
detection_status = 1
process_num = 1
show_result = 1

cam_01 = 'rtsp://192.168.1.137:554/h264'
cam_02 = 'rtsp://admin:Things22@192.168.1.143:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif'
cam_03 = 'rtsp://admin:Things22@192.168.1.146:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif'
cam_04 = 'rtsp://admin:Things22@192.168.1.148:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif'
cam_05 = 'rtsp://admin:Things22@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif'
cam_06 = 'rtsp://admin:Things22@192.168.1.143:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif'

Object_classes = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
                'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
                'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
                'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard',
                'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
                'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
                'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
                'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear',
                'hair drier', 'toothbrush' ]

Object_colors = list(np.random.rand(80,3)*255)
Object_detector = OBJ_DETECTION('weights/yolov5s.pt', Object_classes)

if(process_num>0):
    cap01 = cv2.VideoCapture(cam_01)
    cam_size = (800, 400)
    full_size = (800, 400)
if(process_num>1):
    cap02 = cv2.VideoCapture(cam_02)
    cam_size = (400, 200)
    full_size = (800, 200)
if(process_num>2):
    cap03 = cv2.VideoCapture(cam_03)
    cam_size = (400, 200)
    full_size = (800, 400)
if(process_num>3):
    cap04 = cv2.VideoCapture(cam_04)
    cam_size =(400, 200)
    full_size = (800, 400)
if(process_num>4):
    cap05 = cv2.VideoCapture(cam_05)
    cam_size = (400, 200)
    full_size = (800, 600)
if(process_num>5):
    cap06 = cv2.VideoCapture(cam_06)
    cam_size = (400, 200)
    full_size = (800, 600)

if detection_status == 1:
    #window_handle = cv2.namedWindow("CSI Camera", cv2.WINDOW_AUTOSIZE)
    # Window
    box_color = (255, 0, 255)
    while True:
        start_time = time.time() 
        framerd = cv2.imread('bg.jpg')
        print(framerd.shape)
        frame = cv2.resize(framerd, full_size)
        ret01 = ''
        ret02 = ''
        if(process_num==1):
            ret01, img01 = cap01.read()
            if ret01:
                frame01 = cv2.resize(img01, cam_size) 
                frame = frame01
            else : 
                cap01 = cv2.VideoCapture(cam_01)
                
        if(process_num==2):
            ret01, img01 = cap01.read()
            ret02, img02 = cap02.read()
            if ret01:
                frame01 = cv2.resize(img01, cam_size) 
                frame[0:400, 0:400]=frame01
            if ret02:
                frame02 = cv2.resize(img02, cam_size) 
                frame[0:400, 400:800]=frame02
        if(process_num==3):
            ret01, img01 = cap01.read()
            ret02, img02 = cap02.read()
            ret03, img03 = cap03.read()
            if ret01:
                frame01 = cv2.resize(img01, cam_size) 
                frame[0:200, 0:400]=frame01
            if ret02:
                frame02 = cv2.resize(img02, cam_size) 
                frame[0:200, 400:800]=frame02 
            if ret03:
                frame03 = cv2.resize(img03, cam_size) 
                frame[200:400, 0:400]=frame03
                
        if(process_num==4):
            ret01, img01 = cap01.read()
            ret02, img02 = cap02.read()
            ret03, img03 = cap03.read()
            ret04, img04 = cap04.read()
            if ret01:
                frame01 = cv2.resize(img01, cam_size) 
                frame[0:200, 0:400]=frame01
            if ret02:
                frame02 = cv2.resize(img02, cam_size) 
                frame[0:200, 400:800]=frame02 
            if ret03:
                frame03 = cv2.resize(img03, cam_size) 
                frame[200:400, 0:400]=frame03
            if ret04:
                frame04 = cv2.resize(img04, cam_size) 
                frame[200:400, 400:800]=frame04
        if(process_num==5):
            ret01, img01 = cap01.read()
            ret02, img02 = cap02.read()
            ret03, img03 = cap03.read()
            ret04, img04 = cap04.read()
            ret05, img05 = cap05.read()
            if ret01:
                frame01 = cv2.resize(img01, cam_size) 
                frame[0:200, 0:400]=frame01
            if ret02:
                frame02 = cv2.resize(img02, cam_size) 
                frame[0:200, 400:800]=frame02 
            if ret03:
                frame03 = cv2.resize(img03, cam_size) 
                frame[200:400, 0:400]=frame03
            if ret04:
                frame04 = cv2.resize(img04, cam_size) 
                frame[200:400, 400:800]=frame04       
            if ret05:
                frame05 = cv2.resize(img05, cam_size) 
                frame[400:600, 0:400]=frame05

        if(process_num==6):
            ret01, img01 = cap01.read()
            ret02, img02 = cap02.read()
            ret03, img03 = cap03.read()
            ret04, img04 = cap04.read()
            ret05, img05 = cap05.read()
            ret06, img06 = cap06.read()
            if ret01:
                frame01 = cv2.resize(img01, cam_size) 
                frame[0:200, 0:400]=frame01
            if ret02:
                frame02 = cv2.resize(img02, cam_size) 
                frame[0:200, 400:800]=frame02 
            if ret03:
                frame03 = cv2.resize(img03, cam_size) 
                frame[200:400, 0:400]=frame03
            if ret04:
                frame04 = cv2.resize(img04, cam_size) 
                frame[200:400, 400:800]=frame04       
            if ret05:
                frame05 = cv2.resize(img05, cam_size) 
                frame[400:600, 0:400]=frame05  
            if ret06:
                frame06 = cv2.resize(img06, cam_size) 
                frame[400:600, 400:800]=frame06
        '''
        if ret01:
            frame01 = cv2.resize(img01, (800, 400))  
            frame[0:400, 0:800]=frame01
        if ret02:   
            frame02 = cv2.resize(img02, (800, 400))
            frame[400:800, 800:1600]=frame02
        '''
        if ret01 or ret02:
            print(frame.shape)
            # detection process
            objs = Object_detector.detect(frame)
            
            # plotting
            for obj in objs:
                # print(obj)
                label = obj['label']
                score = obj['score']
                [(xmin,ymin),(xmax,ymax)] = obj['bbox'] 
                
                color = Object_colors[Object_classes.index(label)]
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
                
                #frame = cv2.putText(frame, f'{label} ({str(score)})', (xmin,ymin), cv2.FONT_HERSHEY_SIMPLEX , 0.75, color, 1, cv2.LINE_AA)
        cv2.imshow("CSI Camera", frame) 
        print("FPS: ", 1.0 / (time.time() - start_time))
        keyCode = cv2.waitKey(30)
        if keyCode == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
else:
    print("Unable to open camera")
