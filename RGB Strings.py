import RPi.GPIO as GPIO,drivers,threading
from time import sleep as wait

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings
display=drivers.Lcd() # enable the LCD display

display.lcd_clear() # clear the LCD screen

latch=33
data_bit=35
clock=31

sensor=38

RGB_led1=[13,11,7]
RGB_led2=[21,19,15]

RGB_mix1=[[13,11],[13,7],[11,7]]
RGB_mix2=[[21,19],[21,15],[19,15]]

blue_green='''
GPIO.output(RGB_led1[2],1)
GPIO.output(RGB_led2[1],1)'''

green_blue='''
GPIO.output(RGB_led1[1],1)
GPIO.output(RGB_led2[2],1)'''

red_yellow='''
GPIO.output(RGB_led1[0],1)
GPIO.output(RGB_mix2[0],1)'''

yellow_red='''
GPIO.output(RGB_led2[0],1)
GPIO.output(RGB_mix1[0],1)'''

pink_cyan='''
GPIO.output(RGB_mix1[1],1)
GPIO.output(RGB_mix2[2],1)'''

cyan_pink='''
GPIO.output(RGB_mix1[2],1)
GPIO.output(RGB_mix2[1],1)'''

blue='''
GPIO.output(RGB_led1[2],1)
GPIO.output(RGB_led2[2],1)'''

pink='''
GPIO.output(RGB_mix1[1],1)
GPIO.output(RGB_mix2[1],1)'''

cyan='''
GPIO.output(RGB_mix1[2],1)
GPIO.output(RGB_mix2[2],1)'''

RGB_off='''
for i in RGB_led1,RGB_led2:
    GPIO.output(i,0)'''

stop_program_message='''
print('Stop program Execution/run:')
print('cleanup/release all GPIO pinouts \
to LOW state.')'''

led_loop1=blue_green,green_blue
led_loop2=red_yellow,yellow_red
led_loop3=cyan,pink

led_speed=.05

GPIO.setup(sensor,GPIO.IN)

for i in RGB_led1,RGB_led2:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,0)

control_shift=latch,data_bit,clock

for i in control_shift:GPIO.setup(i,GPIO.OUT)
    
for i in range(16):            
    GPIO.output(latch,0)
    GPIO.output(data_bit,0)
    GPIO.output(clock,1)
    GPIO.output(latch,1)
    GPIO.output(clock,0)
    
byte1='0000000000000000'

byte2=['1000000000000001',
       '0100000000000010',
       '0010000000000100',
       '0001000000001000',
       '0000100000010000',
       '0000010000100000',
       '0000001001000000',
       '0000000110000000']
       
byte3=['0000001001000000',
       '0000010000100000',
       '0000100000010000',
       '0001000000001000',
       '0010000000000100',
       '0100000000000010',
       '1000000000000001']

while True:
    if GPIO.input(sensor)==1:
    
        for x in led_loop2:
            for y in RGB_led1,RGB_led2:
                GPIO.output(y,0)
            exec(x)

            for i in byte2:
                for j in range(16):
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed)
                
            for i in byte3:
                for j in range(16):
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed)
        else:
            break
