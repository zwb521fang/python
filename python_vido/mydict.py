# -*- coding: utf-8 -*-
# import cv2
# cap = cv2.VideoCapture(0)
# ret,frame = cap.read()
# cv2.imwrite("12342.png",frame)
import cv2
import time

interval = 0.0001  # seconds
num_frames = 500
out_fps = 24

capture = cv2.VideoCapture(0)
size =(int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
    int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
video = cv2.VideoWriter("time_lapse.avi", cv2.VideoWriter_fourcc('I','4','2','0'), out_fps, size)

# for low quality webcams, discard the starting unstable frames
for i in xrange(42):
  capture.read()

# capture frames to video
for i in xrange(num_frames):
  _, frame = capture.read()
  video.write(frame)

  ## Optional, in case you need the frames for GIF or so
  filename = '{:4}.png'.format(i).replace(' ', '0')
  cv2.imwrite(filename, frame)

  print('Frame {} is captured.'.format(i))
  time.sleep(interval)

video.release()
capture.release()