import RPi.GPIO as GPIO
import time
import argparse
import sys
import threading

from argparse import RawTextHelpFormatter
from led import LedOps, LedOpsThread
from display_7 import Display7Ops, Display7OpsThread

class Dispatcher:
    
    def __init__(self):
        self.led = LedOps()
        self.display = Display7Ops()
    
    def parse_args(self):
        parser = argparse.ArgumentParser(description='Plays with shift register (74HC595).', formatter_class=RawTextHelpFormatter)
        parser.add_argument('-c', '--count', action='store', choices=['led', 'display', 'all'], dest="count",
                            help="{led} - counting from 0 to 255 on LEDs\n{display} - counting from 0 to E on 7-segments display\n{all} - counting on all")
        parser.add_argument('-e', '--endless', action='store', choices=['led', 'display', 'all'], dest="endless",
                            help="{led} - endless counting from 0 to 255 on LEDs\n{display} - endless counting from 0 to E on 7-segments display\n{all} - endless counting on all")
        parser.add_argument('-i', '--interactive', action='store', choices=['led', 'display'], dest="input",
                            help="{led} - send values on LEDs\n{display} - send values on 7-segments display")
        return parser.parse_args()
    
    def dispatch(self):
        args = self.parse_args()
        if args.count == 'led':
            print('Handling counting on LEDs')
            self.led.count(False)
        elif args.count == 'display':
            print('Handling counting on 7-segments display')
            self.display.count(False)
        elif args.count == 'all':
            print('Handling counting on LEDs and 7-segments display')
            led_thread = LedOpsThread(self.led, False)
            led_thread.setDaemon(True)
            display_thread = Display7OpsThread(self.display, False)
            display_thread.setDaemon(True)
            led_thread.start()
            display_thread.start()
        elif args.endless == 'led':
            print('Handling endless counting on LEDs')
            self.led.count(True)
        elif args.endless == 'display':
            print('Handling endless counting on 7-segments display')
            self.display.count(True)
        elif args.endless == 'all':
            print('Handling endless counting on LEDs and 7-segments display')
            led_thread = LedOpsThread(self.led, True)
            led_thread.setDaemon(True)
            display_thread = Display7OpsThread(self.display, True)
            display_thread.setDaemon(True)
            led_thread.start()
            display_thread.start()
        elif args.input == 'led':
            print('Handling input mode on LEDs')
            self.led.show()
        elif args.input == 'display':
            print('Handling input mode on 7-segments display')
            self.display.show()
            
    def cleanup(self):
        print('Cleaning up all stuff...')
        self.led.cleanup()
        self.display.cleanup()

if __name__ == '__main__':
    dispatcher = Dispatcher()
    try:
        dispatcher.dispatch()
        while threading.active_count() > 0:
            time.sleep(0.1)
    except KeyboardInterrupt:
        dispatcher.cleanup()
