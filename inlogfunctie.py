def login_verify():
    fietsnummer = fietsnummerentry.get
    wachtwoord = wachtwoordentry.get
    kaas = 0
    with open("register.csv", "r") as myCSVfile:
        for line in myCSVfile:
            if fietsnummer and wachtwoord in line:
                kaas = 1
                break
        if kaas == 1:
            functie()
        else:
            invalidinput()
