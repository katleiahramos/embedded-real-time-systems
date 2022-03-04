import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)	

led_pin = 12
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
 
# set up the GPIO channels - one output
GPIO.setup(led_pin, GPIO.OUT)

# PWM

pi_pwm = GPIO.PWM(led_pin,50)		#create PWM instance with frequency
pi_pwm.start(0)	

# Start high
pi_pwm.ChangeDutyCycle(2)
print('2')
time.sleep(.5)
pi_pwm.ChangeDutyCycle(0)


time.sleep(3)

pi_pwm.ChangeDutyCycle(7)
print('7')
time.sleep(1)
pi_pwm.ChangeDutyCycle(0)

time.sleep(3)
# Get half dim
pi_pwm.ChangeDutyCycle(12)
print('10')
time.sleep(1)
pi_pwm.ChangeDutyCycle(0)
# # Get very dim
# pi_pwm.ChangeDutyCycle(12)
# time.sleep(1)

time.sleep(3)

pi_pwm.stop()
GPIO.cleanup()