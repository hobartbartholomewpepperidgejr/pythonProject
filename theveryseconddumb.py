import RPi.GPIO as GPIO #you should import yourself.. NOW!!!!!!!

ledPin = 11 #the pins
buttonPin = 12 #(wow)


def setup():
    GPIO.setmode(GPIO.BOARD) #set the board mode
    GPIO.setup(ledPin, GPIO.OUT) #oh my god its the pin setup itself!!!
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) #read the button stuffs


def loop():
    # die
    while True:
        if GPIO.input(buttonPin == GPIO.LOW): #read the button stuffs
            GPIO.output(ledPin, GPIO.HIGH) #okay NOW turn the led off
            print("its ALIIIVE >>>")
        else:
            GPIO.output(ledpin, GPIO.LOW) #turn it off
            print("nevermind <<<")


def destroy():
    GPIO.cleanup() #explode


if __name__ == '__buttonstuff__':

    print("starting...")
    setup() #run setup
    try:
        loop() #run loop
    except KeyboardInterrupt:
        destroy() #press ctrl c and die
