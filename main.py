import RPi.GPIO as GPIO
import time
import board
import busio
import adafruit_vl53l0x

led_pin = 18

# Initialize Servo
GPIO.setwarnings(False)	

# Set up the GPIO channels - one output
GPIO.setup(led_pin, GPIO.OUT)

# Set up PWM for Servo
pi_pwm = GPIO.PWM(led_pin,50) # Create PWM instance with frequency
pi_pwm.start(2)	# Initialize in starting position

# Go to starting position
pi_pwm.ChangeDutyCycle(2)
time.sleep(.5)
pi_pwm.ChangeDutyCycle(0)
time.sleep(3)

# Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)

command = input('select r=run or q=exit: ')
# Run While Loop
while True:
    try:
        if(command == 'r'):
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
        elif(command == 'q'):
            stop()

    #press ctrl+c for keyboard interrupt
    except KeyboardInterrupt:
        command = input('select r=run or q=exit: ')
        if(command = 'q'):
            stop()

def stop():
    pi_pwm.stop()
    GPIO.cleanup()
    sys.exit(0)

