from machine import Pin, PWM, ADC
from time import sleep

adc = ADC(0) #knob potentiometer connection to A0
pwm = PWM(Pin(27)) #buzzer connected to A1
pwm.freq(10000)

while True:
    val = adc.read_u16()
    #drive the buzzer and turn it off when val is less than 300
    if val > 300:
        pwm.freq(int(val/10))
        pwm.duty_u16(10000)
    else:
        pwm.duty_u16(0)
    
    print(val)
    sleep(0.05)