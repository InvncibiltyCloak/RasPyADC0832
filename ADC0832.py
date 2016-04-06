import time
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  Try again with superuser privileges.")

GPIO.setmode(GPIO.BOARD)

class ADC0832:
    ''' Extremely simple class for reading from an ADC0832 on a Raspberry Pi'''
    def __init__(self, clk_pin = 16, data_pin = 22, csel_pin = 18):
        '''Initializes the ADC0832 pins and state'''
        self.clk_pin = clk_pin
        self.data_pin = data_pin
        self.csel_pin = csel_pin
        self.clk_state = False
        GPIO.setup(clk_pin, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(data_pin, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(csel_pin, GPIO.OUT, initial=GPIO.HIGH) 

        
    def read_channel(self, i):
        '''Reads the value of a channel of the ADC'''
        GPIO.output(self.csel_pin, GPIO.LOW)
        GPIO.output(self.data_pin, GPIO.HIGH) # Start bit
        self._clk(); self._clk()
        # GPIO.output(self.data_pin, GPIO.HIGH) # Single ended reading
        self._clk(); self._clk()
        if(i == 0):
            GPIO.output(sefl.data_pin, GPIO.LOW) # Channel 0 select
        # else:
            # GPIO.output(self.data_pin, GPIO.HIGH) # Channel 1 select
        self._clk(); self._clk()
        
        # End of data input, now read output
        GPIO.setup(self.data_pin, GPIO.IN)
        self._clk();
        result = 0
        for _ in range(8):
            self._clk();self._clk()
            result <<= 1
            result |= GPIO.input(self.data_pin)
            
        GPIO.output(self.csel_pin, GPIO.HIGH)
        GPIO.setup(self.data_pin, GPIO.OUT, initial=GPIO.LOW)
        self._clk()

        return result
            
    def cleanup():
        '''Cleans up the RPi.GPIO library'''
        GPIO.cleanup()
        
    def _clk(self):
        '''Toggles clock between high and low while waiting an appropriate amount
        of time'''
        time.sleep(3e-6) # Yes, this is way smaller than the accuracy of a sleep.
                         # It makes the lib slower than necessary, but who cares?
        if(self.clk_state):
            GPIO.output(self.clk_pin, GPIO.LOW)
        else:
            GPIO.output(self.clk_pin, GPIO.HIGH)
        self.clk_state = not self.clk_state
        