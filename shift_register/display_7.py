import time
import sys

from threading import Thread
from lib.shift_register import ShiftRegister

class Display7Ops:
    
    __digits = [252, 96, 218, 242, 102, 182, 190, 224, 254, 246, 238, 62, 156, 122, 158, 142]
    
    __data_pin = 5
    __clock_pin = 13
    __latch_pin = 19
    
    def __init__(self):
        self.shift_register = ShiftRegister(self.__data_pin, self.__clock_pin, self.__latch_pin)
    
    def count(self, endless):
        print('Counting from 0 to F on 7-segments display. Endless: {}'.format(endless))
        while (True):
            for i in range(0, 16):
                print(i)
                self.shift_register.shift_out(255 - self.__digits[i])
                time.sleep(0.5)
            if not endless:
                break
    
    def show(self):
        while (True):
            print('Enter HEX 0-15: ')
            input_number = int(sys.stdin.readline())
            self.shift_register.shift_out(255 - self.__digits[input_number])
            print('{} send to 7-segments display through Shift Register'.format(input_number))
            
    def cleanup(self):
        self.shift_register.cleanup(255)
        
class Display7OpsThread(Thread):
    
    def __init__(self, display_ops, endless_count):
      Thread.__init__(self)
      self.__display_ops = display_ops
      self.__endless_count = endless_count
      
    def run(self):
      print('Starting display thread.')
      self.__display_ops.count(self.__endless_count)

