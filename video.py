import cv2
vid=cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while(True):

    ret,frame=vid.read()
    gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,5)
print(faces)

for (x,y,w,h) in faces:
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) 
    cv2.imshow("webcam",frame)
if cv2.waitKey(25)==32:
        break
vid.release()
cv2.destroyAllWindows()
    