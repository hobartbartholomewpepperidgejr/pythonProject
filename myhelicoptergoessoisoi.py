import time

soi1 = ["     ROFL:ROFL:ROFL:ROFL",
        "           ___^____ ",
        "  L    __/      [] \ ",
        " LOL===__           \ ",
        "  L      \___ ___ ___] ",
        "              I   I",
        "         ----------/"]

soi2 = ["                :",
        "             ___^____ ",
        "         __/      [] \ ",
        " LLOLL===__           \ ",
        "           \___ ___ ___]",
        "                I   I",
        "           ----------/"]


def soi():
    while True:

        for soi in soi1:
            print(soi)
        time.sleep(0.5)
        clearthescreenTHESECOND()

        for soisoi in soi2:
            print(soisoi)
        time.sleep(0.5)
        clearthescreenTHESECOND()

def clearthescreenTHESECOND():
    for i in range(1, 20):
        print('\n')

try:
    soi()
except KeyboardInterrupt():
    print("dead")
    exit()