import webiopi

GPIO = webiopi.GPIO


SERVO_PIN = 2 // use GPIO 2

DEFAULT_PAN = 0

GPIO.setFunction(SERVO_PIN, GPIO.PWM)
GPIO.pulseAngle(SERVO_PIN, DEFAULT_PAN)

angle = DEFAULT_PAN
increase = 30

while 1:
	GPIO.pulseAngle(SERVO_PIN, angle)
	
	angle += increase
	if angle > 90:
		angle = 60
		increase = -30
	elif angle < -90:
		angle = -60
		increase = 30

	webiopi.sleep(2)
	
