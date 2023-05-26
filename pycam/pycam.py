import time
from picamera2 import Picamera2, Preview

picam = Picamera2()

config = picam.create_preview_configuration()
config.resolution = (640, 480)
config.framerate = 15

picam.configure(config)

picam.start()

while True:
    time.sleep(60)
    picam.capture_file("/mnt/dsm/temp/test-python-%s.jpg" % time.time())

picam.close()