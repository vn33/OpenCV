import cv2 as cv

img = cv.imread('Photos/group 2.jpg')
cv.imshow('Person', img)

gray =  cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# read xml file
har_cascade = cv.CascadeClassifier('haar_face.xml')

# detect faces
faces_rect = har_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)
print('Number of faces found', len(faces_rect))

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
    

cv.imshow('Detected Faces', img)

cv.waitKey(0)