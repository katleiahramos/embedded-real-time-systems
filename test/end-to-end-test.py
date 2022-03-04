import RPi.GPIO as GPIO
import time
import board
import busio
import adafruit_vl53l0x

# Initialize Servo
GPIO.setwarnings(False)	

led_pin = 18
# to use Raspberry Pi board pin numbers
# GPIO.setmode(GPIO.BOARD)
 
# set up the GPIO channels - one output
GPIO.setup(led_pin, GPIO.OUT)


pi_pwm = GPIO.PWM(led_pin,50)		#create PWM instance with frequency
pi_pwm.start(2)	

# Go to starting position
print('set up servo')
pi_pwm.ChangeDutyCycle(2)
time.sleep(.5)
pi_pwm.ChangeDutyCycle(0)
time.sleep(3)




# Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)

# Run While Loop
while True:
    # print("Range: {0}mm".format(vl53.range))
    if vl53.range < 75:
        print('less than 75')
        pi_pwm.ChangeDutyCycle(7.5)
        print('7')
        time.sleep(.5)
        pi_pwm.ChangeDutyCycle(0)
        time.sleep(3)
        pi_pwm.ChangeDutyCycle(2)
        print('2')
        time.sleep(.5)
        pi_pwm.ChangeDutyCycle(0)
        time.sleep(1)


    time.sleep(1.0)


# PWM



# Start high
# pi_pwm.ChangeDutyCycle(2)
# print('2')
# time.sleep(.5)
# pi_pwm.ChangeDutyCycle(0)


time.sleep(3)


# # Get half dim
# pi_pwm.ChangeDutyCycle(12)
# print('10')
# time.sleep(1)
# pi_pwm.ChangeDutyCycle(0)
# # Get very dim
# pi_pwm.ChangeDutyCycle(12)
# time.sleep(1)

# time.sleep(3)

pi_pwm.stop()
GPIO.cleanup()