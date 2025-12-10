import RPi.GPIO as GPIO
import time

SERVO_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50) #50 Hz
pwm.start(0)

def set_angle(angle):
    
    duty = 2 + (angle/18) #crude mapping
    
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty)
    
    time.sleep(1) #let servo move
    
    GPIO.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)

try:
    while(True):
        for i in range(0,190,20):
            print(i)
            set_angle(i)
            time.sleep(0.001)
        
        for i in range(160,0,-20):
            print(i)
            set_angle(i)
            time.sleep(0.001)
    
    
finally:
    pwm.stop()
    GPIO.cleanup()