import time
from picamera2 import Picamera2

picam = Picamera2()

picam.resolution = (640, 480)
picam.framerate = 15

picam.start_recording("/mnt/dsm/temp/test-python-%s.mkv" % time.time(), format="h264")

while True:
    # 60초마다 영상을 끊고 파일을 저장하는 반복문
    time.sleep(60)

    picam.stop_recording()

    picam.start_recording("/mnt/dsm/temp/test-python-%s.mkv" % time.time(), format="h264")

picam.stop_recording()

picam.close()