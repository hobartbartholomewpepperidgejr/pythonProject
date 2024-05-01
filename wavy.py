import RPi.GPIO as GPIO
import time # the usual reverse deportation of our packages

ledPins = [11, 12, 13, 15, 16, 18, 22, 3 ,5 ,24] # pin list

def setup():
    GPIO.setmode(GPIO.BOARD) # use numbering relative 2 the board
    GPIO.setup(ledPins, GPIO.OUT) # make sure the pi makes sure that the pins are used explicitly for outgoing stuffs and not reading
    GPIO.output(ledPins, GPIO.HIGH) # turn them all on for reasons

def loop():
    while True:
        for pin in ledPins: # make lights shift from left 2 right
            GPIO.output(pin, GPIO.LOW) # on again but time travel so this comment makes sense
            time.sleep(0.1) # wait (snooork mimimimimimi)
            GPIO.output(pin, GPIO.HIGH) # off and see the above
        for pin in ledPins[::-1]: # does the above but in reverse (right 2 left) (just reads the list contents in reverse) (somehow)
            GPIO.output(pin, GPIO.LOW) # on
            time.sleep(0.1) # wait again but this time the order makes sense
            GPIO.output(pin, GPIO.HIGH) # off

def destroy(): # explode everything when called
    GPIO.cleanup() # release the pins

if __name__ == '__main__': #program entrance (wow!!)
    print('program be starting...')
    setup()
    try: # if loop() doesnt fire then explode
        print('yarr')
        loop()
    except KeyboardInterrupt: # explode
        destroy()