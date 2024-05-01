import time
b = 0
inc = 1
while True:
    b += inc
    for i in range(b):
        time.sleep(0.1*(1/b))
        print(" ", end="")
    print("do your work")
    if b == 40 or b == 0:
        inc *= -1