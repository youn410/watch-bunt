import webiopi
import time
import wiringpi2 as wiringpi

SERVO_PAN = 18

SERVO_PAN_LEFT_LIMIT = 60
SERVO_PAN_RIGHT_LIMIT = -60

##### SERVO SPECIFICATION #####
SERVO_ANGLE_MIN = -90
SERVO_ANGLE_MAX = 90
SERVO_PULSE_MIN = 0.5
SERVO_PULSE_MAX = 2.4
SERVO_CYCLE = 20
##############################

##### WIRINGPI SPECIFICATION #####
PWM_WRITE_MIN = 0
PWM_WRITE_MAX = 1024
##################################

SERVO_DUTY_MIN = SERVO_PULSE_MIN/SERVO_CYCLE
SERVO_DUTY_MAX = SERVO_PULSE_MAX/SERVO_CYCLE

DUTY_PER_ANGLE = (SERVO_DUTY_MAX - SERVO_DUTY_MIN)/(SERVO_ANGLE_MAX - SERVO_ANGLE_MIN)

SERVO_PAN_DUTY_MIN = DUTY_PER_ANGLE * (SERVO_PAN_RIGHT_LIMIT - SERVO_ANGLE_MIN) + SERVO_DUTY_MIN
SERVO_PAN_DUTY_MAX = DUTY_PER_ANGLE * (SERVO_PAN_LEFT_LIMIT - SERVO_ANGLE_MIN) + SERVO_DUTY_MIN

SERVO_PAN_PWM_WRITE_MIN = PWM_WRITE_MAX * SERVO_PAN_DUTY_MIN
SERVO_PAN_PWM_WRITE_MAX = PWM_WRITE_MAX * SERVO_PAN_DUTY_MAX

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(SERVO_PAN, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetClock(375)


# This function return 0 ... 1024
def getServoPanPWMValue(val):
	pwm_value = int((SERVO_PAN_PWM_WRITE_MAX - SERVO_PAN_PWM_WRITE_MIN) * val + SERVO_PAN_PWM_WRITE_MIN)
	return pwm_value

webiopi.setDebug()

def setup():
	webiopi.debug("Script with macros - Setup")

def loop():
	webiopi.sleep(5)

def destroy():
	webiopi.debug("Script with macros - Destroy")

@webiopi.macro
def setHwPWMforPan(duty, commandID):
	print(getServoPanPWMValue(float(duty)))
	wiringpi.pwmWrite(SERVO_PAN, getServoPanPWMValue(float(duty)))
