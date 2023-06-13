import time
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder

picam = Picamera2()

picam.resolution = (640, 480)
picam.framerate = 15

encoder = H264Encoder(10000000)

picam.start_recording(encoder, "/mnt/dsm/temp/test-python-%s.mkv" % time.time())

while True:
    # 60초마다 영상을 끊고 파일을 저장하는 반복문
    time.sleep(60)

    picam.stop_recording()

    picam.start_recording("/mnt/dsm/temp/test-python-%s.mkv" % time.time(), format="h264")

picam.stop_recording()

picam.close()