import cv2 as cv

def resizeFrame(frame, scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

# READING VIDEO
vid = cv.VideoCapture('video/bird.mp4')

# while loop
while True:
    isTrue, frame = vid.read()

    frame_resize = resizeFrame(frame)

    cv.imshow('video', frame_resize)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

vid.release()
cv.destroyAllWindows()

