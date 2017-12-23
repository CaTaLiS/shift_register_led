import time
import sys

from threading import Thread
from lib.shift_register import ShiftRegister


class LedOps:
    
    __data_pin = 4
    __clock_pin = 17
    __latch_pin = 27
    
    def __init__(self):
        self.shift_register = ShiftRegister(self.__data_pin, self.__clock_pin, self.__latch_pin)
    
    def count(self, endless):
        print('Counting from 0 to 255 on LEDs. Endless: {}'.format(endless))
        while (True):
            for number in range(0, 256):
                print(number)
                self.shift_register.shift_out(number)
                time.sleep(0.5)
            if not endless:
                break
    
    def show(self):
        while (True):
            print('Enter DEC 0-255: ')
            input_number = int(sys.stdin.readline())
            self.shift_register.shift_out(input_number)
            print('{} send to LEDs through Shift Register'.format(input_number))
            
    def cleanup(self):
        self.shift_register.cleanup()

class LedOpsThread(Thread):
    
    def __init__(self, led_ops):
      Thread.__init__(self)
      self.__led_ops = led_ops
      
    def run(self):
      print('Starting led thread.')
      self.__led_ops.count(False)

