import RPi.GPIO as GPIO
import time
LedPin = 7   
def setup():
  GPIO.setmode(GPIO.BOARD)      
  GPIO.setup(LedPin, GPIO.OUT)   
  GPIO.output(LedPin, GPIO.HIGH) 

def blink():
  while True:
    GPIO.output(LedPin, GPIO.HIGH)  
    time.sleep(3)
    GPIO.output(LedPin, GPIO.LOW) 
    time.sleep(3)

def destroy():
  GPIO.output(LedPin, GPIO.LOW)   
  GPIO.cleanup()                 

if __name__ == '__main__':   
  setup()
  try:
    blink()
  except KeyboardInterrupt: 
    destroy()
