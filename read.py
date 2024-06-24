import cv2 as cv
# Reading images
img = cv.imread('Photos/cat_large.jpg')
cv.imshow('Cat', img)

# Reading videos
capture = cv.VideoCapture('Videos/dog.mp4') # 0 -> webcam
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
