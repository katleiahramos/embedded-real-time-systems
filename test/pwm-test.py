import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)	

led_pin = 12
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
 
# set up the GPIO channels - one output
GPIO.setup(led_pin, GPIO.OUT)

# PWM

pi_pwm = GPIO.PWM(led_pin,1000)		#create PWM instance with frequency
pi_pwm.start(0)	

# Start high
pi_pwm.ChangeDutyCycle(100)
time.sleep(1)

# Get half dim
pi_pwm.ChangeDutyCycle(50)
time.sleep(1)

# Get very dim
pi_pwm.ChangeDutyCycle(25)
time.sleep(1)

