from dht11 import *
from machine import Pin, SoftI2C
from machine_i2c_lcd import I2cLcd
from time import sleep

# Define the LCD I2C address and dimensions
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16


#i2c = SoftI2C(0, scl=Pin(1), sda=Pin(0), freq=400000) #LED connected to I2C1
i2c = SoftI2C(sda=Pin(6), scl=Pin(7), freq=200000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
dht2 = DHT(18, Type=DHT11) #temp and humidity sensor, D18

lcd.putstr("It's working :)")
sleep(4)

while True:
    temp, humid = dht2.readTempHumid()
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr("Temp : "+ str(temp)+ "C")
    lcd.move_to(0, 1)
    lcd.putstr("Humid : "+ str(humid)+ "%")
    sleep(2)