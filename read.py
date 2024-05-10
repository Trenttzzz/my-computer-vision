import cv2 as cv

# img = cv.imread('image/turbo-lag.jpg')

# show image
# cv.imshow('turbo lag', img)

# wait 
# cv.waitKey(0)

# read video
# using while loop to show all the frame

vid = cv.VideoCapture('video/bird.mp4')

# while loop
while True:
    isTrue, frame = vid.read()

    cv.imshow('video',frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

vid.release()
cv.destroyAllWindows()
