import RPi.GPIO as GPIO
import time
import datetime
import picamera

sensor = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False
led_light = False

cam=picamera.PiCamera()

while True:
	time.sleep(0.1)
	previous_state = current_state
	current_state = GPIO.input(sensor)
	if current_state != previous_state:
		new_state = 'HIGH' if current_state else 'LOW'
		print('GPIO pin %s is %s' % (sensor, new_state))
		if current_state:
			cam.start_preview()
			time.sleep(2)
			cam.capture(str(datetime.datetime.now().strftime('%y_%m_%d_%H_%M_%S')) + '.jpg')
			time.sleep(1)
			cam.stop_preview()
			time.sleep(6)
