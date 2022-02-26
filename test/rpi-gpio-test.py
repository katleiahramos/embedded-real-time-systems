import RPi.GPIO as GPIO
import time

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
 
# set up the GPIO channels - one output
GPIO.setup(12, GPIO.OUT)
 
#blink
GPIO.output(12, GPIO.HIGH)

time.sleep(3)

GPIO.output(12, GPIO.LOW)
