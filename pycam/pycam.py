import time
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput

picam2 = picamera2()

config = picam2.create_video_configuration(main={"size": (1280, 720)})
picam2.configure(config)

encoder = H264Encoder(10000000)
output = FfmpegOutput("/mnt/dsm/temp/test-python-%s.mp4" % time.time())

while True:
    # 60초마다 영상을 끊고 파일을 저장하는 반복문
    time.sleep(60)

    picam2.stop_recording()

    picam2.start_recording(encoder, output )

picam.stop_recording()

picam.close()