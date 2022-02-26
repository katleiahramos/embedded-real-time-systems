# Resouce: https://www.electronicwings.com/raspberry-pi/stepper-motor-interfacing-with-raspberry-pi for source code


import RPi.GPIO as GPIO
import time
import sys

motor_channel = (11,12,15,16)
sleep = 0.002 # Limit seems to be around 0.001

def setup():
    print('in setup')
    GPIO.setwarnings(False)

    # to use Raspberry Pi board pin numbers
    GPIO.setmode(GPIO.BOARD)

    # set up the GPIO channels - one output
    GPIO.setup(motor_channel, GPIO.OUT)

def run():
    print('in run')
    motor_direction = input('select motor direction a=anticlockwise, c=clockwise: ')
    while True:
        try:
            if(motor_direction == 'c'):
                print('motor running clockwise\n')
                GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
                time.sleep(sleep)
                GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
                time.sleep(sleep)
                GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
                time.sleep(sleep)
                GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
                time.sleep(sleep)

            elif(motor_direction == 'a'):
                print('motor running anti-clockwise\n')
                GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
                time.sleep(sleep)
                GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
                time.sleep(sleep)
                GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
                time.sleep(sleep)
                GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
                time.sleep(sleep)

                
        #press ctrl+c for keyboard interrupt
        except KeyboardInterrupt:
            #query for setting motor direction or exit
            motor_direction = input('select motor direction a=anticlockwise, c=clockwise or q=exit: ')
            #check for exit
            if(motor_direction == 'q'):
                print('motor stopped')
                sys.exit(0)

def main():
    setup()
    run()

main()
