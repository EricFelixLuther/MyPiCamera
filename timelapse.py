import time
import picamera
import datetime

setting = True
while setting:
    print "Odstep czasow:"
    print "Sugerowany 30 sekund"
    delay = int(raw_input("delay = "))
    print "Calkowita ilosc zdjec:"
    print "Sugeorowana 2880"
    total_photos=int(raw_input("total_photos = "))
    print "Czas zdjec wynosi: " + str(datetime.timedelta(seconds=(delay * total_photos)))
    print "Przy " + str(total_photos) + " zdjeciach i 10 fps, film wyjsciowy bedzie trwal: " + str(datetime.timedelta(seconds=total_photos/10))
    print "Przy " + str(total_photos) + " zdjeciach i 20 fps, film wyjsciowy bedzie trwal: " + str(datetime.timedelta(seconds=total_photos/20))
    print "Przy " + str(total_photos) + " zdjeciach i 24 fps, film wyjsciowy bedzie trwal: " + str(datetime.timedelta(seconds=total_photos/24))
    while True:
        print "Kontynuowac z tymi danymi?"
        if str(raw_input()) == 'y':
            setting = False
            break
        elif str(raw_input()) == 'n':
            break
        else:
            print "Co?"


def timelapse():
    while True:
        if datetime.datetime.now() >= datetime.datetime(2015, 12, 10, 0, 0, 0):
            break
        print "Not yet. Waiting 5 seconds."
        time.sleep(5)
    x = 0
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.framerate = 30
        time.sleep(2)

        camera.start_preview()
        time.sleep(2)
        while True:
            camera.capture('/home/pi/tlps/img%04d.jpg' % x)
            print('Captures img%04d.jpg' % x)
            time.sleep(delay)
            x += 1
            if x >= total_photos:#2880:
                break
        camera.stop_preview()

timelapse()
