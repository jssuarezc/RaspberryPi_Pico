from machine import Pin, SoftI2C
from machine_i2c_lcd import I2cLcd
from time import sleep

# Use the address you are testing (0x27 or 0x3F)
I2C_ADDR = 0x3F 
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = SoftI2C(sda=Pin(6), scl=Pin(7), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

print("Starting LCD Test...")

lcd.backlight_on() # Ensure the backlight is on

while True:
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr("LCD Test OK!")
    
    lcd.move_to(0, 1)
    lcd.putstr("MicroPython RUNNING")
    
    sleep(1)
    
    lcd.clear()
    sleep(0.5)