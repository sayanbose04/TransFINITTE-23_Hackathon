import cv2
from tracker import *
# Create tracker object
tracker = EuclideanDistTracker()
cap = cv2.VideoCapture("Highway.mp4")
# Define the grid properties
grid_spacing = 90
grid_color = (0,0,0) 


# Object detection from Stable camera
object_detector = cv2.createBackgroundSubtractorMOG2(history=90, varThreshold=35)

while True:
    ret, frame = cap.read()#ret is a boolean regarding whether or not there was a return at all, at the frame is each frame that is returned.
    height, width, _ = frame.shape

    for i in range(0, frame.shape[0], grid_spacing):
        cv2.line(frame, (0, i), (frame.shape[1], i), grid_color, 1)

    # Draw the vertical lines
    for j in range(0, frame.shape[1], grid_spacing):
        cv2.line(frame, (j, 0), (j, frame.shape[0]), grid_color, 1)



 #Display the frame with grid lines
    cv2.imshow('Video with Grid Lines', frame)
    # Extract Region of interest
    roi = frame[20:,350:]
    # 1. Object Detection
    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []
    for cnt in contours:
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)
        if area >1000 and area <1030:
            x, y, w, h = cv2.boundingRect(cnt)
            detections.append([x, y, w, h])
    # 2. Object Tracking
    boxes_ids = tracker.update(detections)
    for box_id in boxes_ids:
        x, y, w, h, id = box_id
        cv2.putText(roi, str(id), (x, y-15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        if y+h<300:
            colour = (0,255,0)
        else:
            colour = (0,0,255)
        cv2.rectangle(roi, (x, y), (x + w, y +h),colour, 3)
        print(id,":",(x,y))
    cv2.imshow("roi", roi)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()