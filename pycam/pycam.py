import time
import datetime
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
import os
import shutil

# Set the desired working directory 
# 작업 경로와 복사할 경로를 맞춰서 실행해줘야 함 
print(os.getcwd())
working_directory = "/home/kgu4624/Documents/nodegpio/webdav"
dst = "/mnt/dsm/rasberry/temp/_cctv/"
os.chdir(working_directory)

# picam 초기화 및 해상도 설정 
picam2 = Picamera2()
config = picam2.create_video_configuration(main={"size": (640, 480)})
picam2.configure(config)

#H264 1분단위 녹화 -> 전송 
# webdav 혹은 samba 혹은 로컬 스토리지 등등 이동 가능 
# 추천은 여기선 녹화만 하고, 별도 스크립트를 통해 이동하는 것을 권장 
# 파이썬은 파일 옮기는게 좋은 플랫폼은 아님 
# webdav 한 번 죽으면 라즈베리 리부팅 >> 리부팅에 3분 가까이 걸림 ㅡㅡ;;;
# 처음엔 잘 되다가 왜 반복하면 죽어버리지 
while True:
    time.sleep(2)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    filename = "test-python-{}.mp4".format(current_time)
    encoder = H264Encoder(10000000)
    output = FfmpegOutput(filename)

    # 60초 영상을 끊고 파일을 저장하는 반복문
    

    picam2.start_recording(encoder, output )
    time.sleep(60)

    picam2.stop_recording()
    print("recorded once" + filename )
    
picam.stop_recording()

picam.close()