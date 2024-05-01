for y in range(5):
    for x in range(5):
        exec("current=y"+str(y))
        exec(current+" = ()")
        exec(current+".add[0, 0]")
        for i in current:
            print(i)