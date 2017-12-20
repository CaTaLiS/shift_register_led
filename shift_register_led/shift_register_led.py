import RPi.GPIO as GPIO
import time
import argparse
import sys

DATA_PIN = 4 #DS
CLOCK_PIN = 17 #SH_CP
LATCH_PIN = 27 #ST_CP

def setup():
    GPIO.setwarnings(False)
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
    
def count_on_leds_binary(endless):
    print('Counting from 0 to 255 on LEDs. Endless: {}'.format(endless))
    while (True):
        for number in range(0, 256):
            print(number)
            shiftOut(number)
            time.sleep(0.1)
        if not endless:
            break
    
def show_binary_number():
    while (True):
        print('Enter DEC 0-255: ')
        input_number = int(sys.stdin.readline())
        shiftOut(input_number)
        print('{} send to led through shift register'.format(input_number))
    
if __name__ == '__main__':
    setup()
    try:
        parser = argparse.ArgumentParser(description='Plays with shift register (74HC595).')
        parser.add_argument('-c', '--count', action='store_true', default=False, dest="count", help="counting from 0 to 255 with shift register")
        parser.add_argument('-e', '--endless', action='store_true', default=False, dest="endless", help="endless counting")
        parser.add_argument('-i', '--interactive', action='store_true', default=True, dest="input", help="interactive input mode")
        args = parser.parse_args()
        if args.count:
            count_on_leds_binary(args.endless)
        if args.input:
            show_binary_number()
    except KeyboardInterrupt:
        destroy()
