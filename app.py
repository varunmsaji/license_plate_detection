
import ultralytics
from ultralytics import YOLO
import cv2
from sort.sort import *
from utils import get_car
mot_tracker = Sort()
model = YOLO('yolov8n.pt')
license_model = YOLO('runs/detect/train2/weights/best.pt')

cap = cv2.VideoCapture('demo.mp4')
#only need the car bike etc
vehicle =[2,3,5,7] 
detection_ = []
ret = True
frame_no =-1
while ret:
    frame_no+=1
    ret,frame = cap.read()
    if  ret and frame_no < 10:
        pass 
        
        detections = model(frame)[0]
        #will print x,y,x2,y2 ,confedence and classid 
        for detection in detections.boxes.data.tolist():
            x1,y1,x2,y2,score,class_id = detection 
            if int(class_id) in vehicle:
                detection_.append([x1,y1,x2,y2,score])
       
       
        #track vehicles
        #will have all the bounding box data and tracking id
        track_ids = mot_tracker.update(np.asarray(detection_))

        #now we need to detect licence plates
        licence_plates =  license_model(frame)[0]
        for licence_plate in licence_plates.boxes.data.tolist():
            x1,y1,x2,y2,score,class_id = licence_plate 

            #connect car to licence plate using cutom funtion
            xcar1,ycar1,xcar2,ycar2,car_id = get_car(licence_plate,track_ids)
            #crop the licence plate
            licence_plate_crop = frame[int(y1):int(y2),int(x1):int(x2)]
            #process the coped licence plates
            licence_plate_crop_gray = cv2.cvtColor(licence_plate_crop,cv2.COLOR_BGR2GRAY)
            _,licence_plate_crop_thresh = cv2.threshold(licence_plate_crop_gray,64,255,cv2.THRESH_BINARY_INV)
            cv2.imshow('original',licence_plate_crop)
            cv2.imshow('threshold',licence_plate_crop_thresh)
            cv2.waitKey(0)