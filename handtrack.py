import cv2     
import mediapipe as mp
import time

cap= cv2.VideoCapture(0) 

mphands = mp.solutions.hands
hands = mphands.Hands(False)
mpDraw = mp.solutions.drawing_utils

pTime= 0
cTime= 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

 for id, lm in enumerate(handLms.landmark): 
    h,w,c = img.shape
    cx,cy = int(lm.x*w), int(lm.y*h)
    print( id, cx, cy)
            
if id==0:
     cv2.circle(img, (cx,cy), 10, (255,0,255), cv2.FILLED)
     mpDraw.draw_landmarks(img, handLms, mphands.HAND_CONNECTIONS)
            
           cTime = time.time()
           fps = 1/(cTime-pTime)
           pTime = cTime
            
           cv2.putText( img, str(int(fps)),(10,70), cv2.FONT_HERSEY_PLAIN, 3, (255,0,255),3)
           cv2.imshow("image", img)
if cv2.waitKey(1) & 0xFF == ord('q'):
                
            cap.release()
           cv2.destroyAllWindows()

    #install cv2 and mediapipe moduls before debugging; you can change variables name for your self comprehension. 
