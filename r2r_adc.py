import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.01, verbose=False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
        
        if self.verbose:
            print(f"R2R_ADC initialized with dynamic range: {self.dynamic_range}V")
    
    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()
        
        if self.verbose:
            print("R2R_ADC deinitialized")
    
    def number_to_dac(self, number):
        for i, pin in enumerate(self.bits_gpio):
            bit = (number >> (7 - i)) & 1
            GPIO.output(pin, bit)
        
        if self.verbose:
            print(f"DAC set to: {number} (0x{number:02X})")
    
    def sequential_counting_adc(self):
        for number in range(256):
            self.number_to_dac(number)
            
            time.sleep(self.compare_time)
            
            if GPIO.input(self.comp_gpio):
                if self.verbose:
                    print(f"Conversion complete: {number} (DAC voltage exceeded input)")
                return number
        
        if self.verbose:
            print("Input voltage exceeds maximum DAC range")
        return 255
    
    def get_sc_voltage(self):
        digital_value = self.sequential_counting_adc()
        voltage = (digital_value / 255.0) * self.dynamic_range
        
        if self.verbose:
            print(f"Measured voltage: {voltage:.3f}V (digital: {digital_value})")
        
        return voltage

if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.3, 0.01, True)
        
        print("Measuring potentiometer voltage. Press Ctrl+C to stop")
        print("-" * 40)
        
        while True:
            voltage = adc.get_sc_voltage()
            print(f"Voltage: {voltage:.3f} V")
            print("-" * 40)
            
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        print("\nMeasurement stopped by user")
        
    finally:
        adc.deinit()