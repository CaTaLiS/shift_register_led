import RPi.GPIO as GPIO
import time

DATA_PIN = 4 #DS
CLOCK_PIN = 17 #SH_CP
LATCH_PIN = 27 #ST_CP

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DATA_PIN, GPIO.OUT)
    GPIO.setup(CLOCK_PIN, GPIO.OUT)
    GPIO.setup(LATCH_PIN, GPIO.OUT)

def destroy():
    GPIO.output(DATA_PIN, GPIO.LOW)
    GPIO.output(CLOCK_PIN, GPIO.LOW)
    GPIO.output(LATCH_PIN, GPIO.LOW)
    GPIO.cleanup()
    
def shiftOut(byte):
    GPIO.output(LATCH_PIN, GPIO.LOW)
    for x in range(0, 8):
        GPIO.output(DATA_PIN, (byte >> x) & 1)
        GPIO.output(CLOCK_PIN, GPIO.HIGH)
        GPIO.output(CLOCK_PIN, GPIO.LOW)
    GPIO.output(LATCH_PIN, GPIO.HIGH)
    
def count_on_leds_binary():
    print('Counting from 0 to 255 on LEDs.')
    for number in range(0, 255):
        print(number)
        shiftOut(number)
        time.sleep(1)
    
if __name__ == '__main__':
    setup()
    try:
        count_on_leds_binary()
    except KeyboardInterrupt:
        destroy()
