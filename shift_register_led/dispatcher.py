import RPi.GPIO as GPIO
import time
import argparse
import sys

from argparse import RawTextHelpFormatter


class Dispatcher:
    
    def parse_args(self):
        parser = argparse.ArgumentParser(description='Plays with shift register (74HC595).', formatter_class=RawTextHelpFormatter)
        parser.add_argument('-c', '--count', action='store', choices=['led', 'display'], dest="count",
                            help="{led} - counting from 0 to 255 on LEDs\n{display} - counting from 0 to E on 7-segments display")
        parser.add_argument('-e', '--endless', action='store', choices=['led', 'display'], dest="endless",
                            help="{led} - endless counting from 0 to 255 on LEDs\n{display} - endless counting from 0 to E on 7-segments display")
        parser.add_argument('-i', '--interactive', action='store', choices=['led', 'display'], dest="input",
                            help="{led} - send values on LEDs\n{display} - send values on 7-segments display")
        return parser.parse_args()
    
    def dispatch(self):
        args = self.parse_args()
        if args.count == 'led':
            print('Handling counting on LEDs')
        if args.count == 'display':
            print('Handling counting on 7-segments display')
        if args.endless == 'led':
            print('Handling endless counting on LEDs')
        if args.endless == 'display':
            print('Handling endless counting on 7-segments display')
        if args.input == 'led':
            print('Handling input mode on LEDs')
        if args.input == 'display':
            print('Handling input mode on 7-segments display')

if __name__ == '__main__':
    dispatcher = Dispatcher()
    dispatcher.dispatch()

    