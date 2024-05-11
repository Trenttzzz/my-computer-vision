import cv2 as cv

# FOR IMAGE
# img = cv.imread('image/turbo-lag.jpg')

# show image
# cv.imshow('turbo lag', img)

# wait 
# cv.waitKey(0)


# FOR VIDEO
vid = cv.VideoCapture('video/bird.mp4')

# using while loop to show all the image frame by frame
while True:
    isTrue, frame = vid.read()

    cv.imshow('video',frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

vid.release()
cv.destroyAllWindows()
