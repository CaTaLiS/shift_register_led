import RPi.GPIO as GPIO

class ShiftRegister:
    
    __all_instances_number = 0
    
    def __register_instance(self):
        ShiftRegister.__all_instances_number = ShiftRegister.__all_instances_number + 1
        print('[ShiftRegister] Registered {} instance.'.format(ShiftRegister.__all_instances_number))

    def __unregister_instance(self):
        print('[ShiftRegister] Unregistered {} instance.'.format(ShiftRegister.__all_instances_number))
        ShiftRegister.__all_instances_number = ShiftRegister.__all_instances_number - 1

    def __init__(self, data_pin, clock_pin, latch_pin):
        self.__data_pin = data_pin
        self.__clock_pin = clock_pin
        self.__latch_pin = latch_pin
        self.setup()

    def setup(self):
        if ShiftRegister.__all_instances_number == 0:
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
        self.__register_instance()
        GPIO.setup(self.__data_pin, GPIO.OUT)
        GPIO.setup(self.__clock_pin, GPIO.OUT)
        GPIO.setup(self.__latch_pin, GPIO.OUT)
        
    def cleanup(self, state=0):
        self.__unregister_instance()
        self.shift_out(state)
        #GPIO.output(self.__data_pin, GPIO.LOW)
        #GPIO.output(self.__clock_pin, GPIO.LOW)
        #GPIO.output(self.__latch_pin, GPIO.LOW)
        if ShiftRegister.__all_instances_number == 0:
            print('[ShiftRegister] Cleaning GPIO...')
            GPIO.cleanup()
    
    def shift_out(self, byte):
        GPIO.output(self.__latch_pin, GPIO.LOW)
        for x in range(0, 8):
            GPIO.output(self.__data_pin, (byte >> x) & 1)
            GPIO.output(self.__clock_pin, GPIO.HIGH)
            GPIO.output(self.__clock_pin, GPIO.LOW)
        GPIO.output(self.__latch_pin, GPIO.HIGH)
