import csv
def register_verify():
    #naam, voornaam, telefoonnummer, kaartnummer
    kaas = 1
    naam = input()
    voornaam = input()
    telefoonnummer = input()
    kaartnummer = input()
    kaartnummerint = int(kaartnummer)
    telefoonnummerint = int(telefoonnummer)
    if type(naam) == str and len(telefoonnummer) == 10 and type(telefoonnummerint) == int and type(voornaam) == str and len(kaartnummer) == 16 and type(kaartnummerint) == int:
        with open("register.csv", "r", newline="") as myCSVfile:
            for row in myCSVfile:
                if kaartnummer in row:
                    print("kaas")
                    kaas = kaas + 1
                    break
        if kaas == 0:
            with open("register.csv", "a", newline="") as myCSVfile:
                writer = csv.writer(myCSVfile, delimiter=";")
                writer.writerow((voornaam, naam, telefoonnummer, kaartnummer))
    else:
        print("Help")
        achternaamentry.delete(0,END)
        voornaamentry.delete(0,END)
        telefoonnummerentry.delete(0,END)
        ovkaartnummerentry.delete(0,END)
        invalidlabel.grid(row = 7)

register_verify()

