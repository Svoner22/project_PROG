def bikenumber():
    global que
    forget(2)
    kaas = 0
    bikenumber = random.randomrange(10000,100000)
    with open("register.csv", "r") as myCSVfile:
        for row in myCSVfile:
            while bikenumber in row:
                bikenumber = random.randomrange(10000, 100000)
    bikenumberLabel = yellowlabel("Uw fietsnummer is : "+str(bikenumber))
    que[2] = [bikenumberLabel]
    bikenumberLabel.grid(row = 2, columspan = 2)
    return bikenumber
