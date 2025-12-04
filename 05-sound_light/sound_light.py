from machine import Pin, SoftI2C,ADC
from machine_i2c_lcd import I2cLcd
from time import sleep

# Define the LCD I2C address and dimensions
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c=SoftI2C(scl=Pin(7),sda=Pin(6),freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

sleep(1)
light=ADC(0)
sound=ADC(1)

while True:
    
    lightVal = light.read_u16()
    soundVal = sound.read_u16()
    
    lcd.clear()
    
    lcd.move_to(0, 0)
    
    lcd.putstr('LightVal=')
    lcd.putstr(str(lightVal))
    
    lcd.move_to(0, 1)
    
    lcd.putstr('SoundVal=')
    lcd.putstr(str(soundVal))
    
    sleep(1)