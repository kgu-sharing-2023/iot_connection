import time
import datetime
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
import os
import shutil

# Set the desired working directory
print(os.getcwd())
working_directory = "/home/kgu4624/Documents/nodegpio/webdav"
dst = "/mnt/dsm/temp/_cctv/"
os.chdir(working_directory)

picam2 = Picamera2()

config = picam2.create_video_configuration(main={"size": (640, 480)})
picam2.configure(config)


while True:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    filename = "test-python-{}.mp4".format(current_time)
    encoder = H264Encoder(10000000)
    output = FfmpegOutput(filename)

    # 5초 영상을 끊고 파일을 저장하는 반복문
    

    picam2.start_recording(encoder, output )
    time.sleep(5)

    picam2.stop_recording()
    print("recorded once" + filename )
    
    shutil.move(working_directory + "/" + filename, dst)

picam.stop_recording()

picam.close()