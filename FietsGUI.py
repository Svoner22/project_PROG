#Fietsenstalling

from tkinter import Tk, Label, Button, Entry, END, Text, Scrollbar
import csv
import random
import threading

"""
noot voor groep:
als userinput niet aan condities voldoet:
roep deze functie aan:

invalidinput(1)

Nog in te leveren/schrijven functies:
stallen()
ophalen()
informatie()
antirobotbeveiliging
telegrambeveiliging
tijddisplay
snelle functieoutputdisplay
"""

def bluebutton(buttontext, function):
    button = Button(text = buttontext,
                    height = 2,
                    width = 15,
                    font = ('Helvetica',16),
                    background = 'blue',
                    foreground = 'white',
                    command = function)
    return button

def yellowlabel(labeltext):
    label = Label(text = labeltext,
                  background = 'yellow',
                  foreground = 'blue',
                  font = ('Helvetica',16))
    return label

def display(index):
    global que
    for item in que[index]:
        item.grid(row = index, column = que[index].index(item))

def forget(index):
    global que
    for item in range(index, 5):
        for subitem in que[item]:
            subitem.grid_forget()

def invalidinput(index):
    global que
    global invalidlabel
    invalidlabel = yellowlabel('Ongeldige invoer. Probeer opnieuw')
    que[index].append(invalidlabel)
    for item in que[index]:
        if type(item) == Entry:
            item.delete(0, END)
    invalidlabel.grid(row = 10, columnspan = 2)

def main():
    global root
    root = Tk()
    root.configure(background = 'yellow')
    root.geometry("1920x1020")
    initiate()
    root.mainloop()

def initiate():
    global que
    global titlelabel
    global stallenbutton
    global ophalenbutton
    global informatiebutton
    global overigebutton
    global menukeuze
    menukeuze = ''
    que =[[],[],[],[],[]]
    forget(0)
    titlelabel = yellowlabel('NS fietsenstalling')
    registerbutton = bluebutton('Registreer', register)
    stallenbutton = bluebutton('Stal fiets', stallen_login)
    ophalenbutton = bluebutton('Haal fiets op', ophalen_login)
    informatiebutton = bluebutton('Informatie opvragen', informatie_login)
    overigebutton = bluebutton('Overige', overige)
    que[0] = [registerbutton, stallenbutton, ophalenbutton, informatiebutton, overigebutton, titlelabel]
    display(0)

def register():
    forget(1)
    global naamentry
    global telefoonnummerentry
    global ovkaartnummerentry
    global registerverifybutton
    naamlabel = yellowlabel('naam:')
    telefoonnummerlabel = yellowlabel('Telefoonnr: ')
    naamentry = Entry(root)
    telefoonnummerentry = Entry(root)
    registerverifybutton = bluebutton('Registreren', register_verify)
    que[1] = [naamlabel, telefoonnummerlabel, naamentry, telefoonnummerentry, registerverifybutton]
    naamlabel.grid(row = 2 ,column = 0)
    telefoonnummerlabel.grid(row = 3, column = 0)
    naamentry.grid(row = 2, column = 1)
    telefoonnummerentry.grid(row = 3, column = 1)
    registerverifybutton.grid(row = 4, column = 0)

def register_verify():
    naam = naamentry.get()
    telefoonnummer = telefoonnummerentry.get()
    kaas = True
    try:
        telefoonnummerint = int(telefoonnummer)
        with open("register.csv", "r") as myCSVfile:
                for row in myCSVfile:
                    if telefoonnummer in row or len(telefoonnummer) != 10:
                        kaas = False
        if kaas:
            forget(1)
            fietsnummer = str(random.randrange(10000,100000))
            with open("register.csv", "r") as myCSVfile:
                for row in myCSVfile:
                    while fietsnummer in row:
                        fietsnummer = random.randrange(10000, 100000)
            wachtwoord = str(random.randrange(10000, 100000))
            wachtwoordlabel = yellowlabel('uw wachtwoord is: '+wachtwoord)
            fietsnummerlabel = yellowlabel("Uw fietsnummer is : "+fietsnummer)
            que[1]=[wachtwoordlabel, fietsnummerlabel]
            fietsnummerlabel.grid(row = 1, columnspan = 2)
            wachtwoordlabel.grid(row = 2, columnspan = 2)
            with open("register.csv", "a", newline="") as myCSVfile:
                writer = csv.writer(myCSVfile, delimiter=";")
                writer.writerow((naam, telefoonnummer, fietsnummer, wachtwoord))
        else:
            invalidinput(1)
    except:
        invalidinput(1)

def stallen_login():
    forget(1)
    global fietsnummerentry
    global wachtwoordentry
    global loginbutton
    fietsnummerlabel = yellowlabel('Fietsnummer: ')
    wachtwoordlabel = yellowlabel('Wachtwoord:')
    fietsnummerentry = Entry()
    wachtwoordentry = Entry()
    loginbutton = bluebutton('Login', stallen_verify)
    que[1] = [fietsnummerlabel, wachtwoordlabel, fietsnummerentry, wachtwoordentry, loginbutton]
    fietsnummerlabel.grid(row = 2 ,column = 0)
    wachtwoordlabel.grid(row = 3, column = 0)
    fietsnummerentry.grid(row = 2, column = 1)
    wachtwoordentry.grid(row = 3, column = 1)
    loginbutton.grid(row = 4, column = 0)

def ophalen_login():
    forget(1)
    global fietsnummerentry
    global wachtwoordentry
    global loginbutton
    fietsnummerlabel = yellowlabel('Fietsnummer: ')
    wachtwoordlabel = yellowlabel('Wachtwoord:')
    fietsnummerentry = Entry()
    wachtwoordentry = Entry()
    loginbutton = bluebutton('Login', ophalen_verify)
    que[1] = [fietsnummerlabel, wachtwoordlabel, fietsnummerentry, wachtwoordentry, loginbutton]
    fietsnummerlabel.grid(row = 2 ,column = 0)
    wachtwoordlabel.grid(row = 3, column = 0)
    fietsnummerentry.grid(row = 2, column = 1)
    wachtwoordentry.grid(row = 3, column = 1)
    loginbutton.grid(row = 4, column = 0)

def informatie_login():
    forget(1)
    global fietsnummerentry
    global wachtwoordentry
    global loginbutton
    fietsnummerlabel = yellowlabel('Fietsnummer: ')
    wachtwoordlabel = yellowlabel('Wachtwoord:')
    fietsnummerentry = Entry()
    wachtwoordentry = Entry()
    loginbutton = bluebutton('Login', informatie_verify)
    que[1] = [fietsnummerlabel, wachtwoordlabel, fietsnummerentry, wachtwoordentry, loginbutton]
    fietsnummerlabel.grid(row = 2 ,column = 0)
    wachtwoordlabel.grid(row = 3, column = 0)
    fietsnummerentry.grid(row = 2, column = 1)
    wachtwoordentry.grid(row = 3, column = 1)
    loginbutton.grid(row = 4, column = 0)

def stallen_verify():
    fietsnummer = fietsnummerentry.get()
    wachtwoord = wachtwoordentry.get()
    kaas = False
    with open("register.csv", "r") as myCSVfile:
        for row in myCSVfile:
            if fietsnummer and wachtwoord in row:
                kaas = True
    if kaas:
        stallen()
    else:
        invalidinput(1)

def ophalen_verify():
    fietsnummer = fietsnummerentry.get()
    wachtwoord = wachtwoordentry.get()
    kaas = False
    with open("register.csv", "r") as myCSVfile:
        for line in myCSVfile:
            if fietsnummer and wachtwoord in line:
                kaas = True
    if kaas:
        ophalen()
    else:
        invalidinput(1)

def informatie_verify():
    fietsnummer = fietsnummerentry.get()
    wachtwoord = wachtwoordentry.get()
    kaas = False
    with open("register.csv", "r") as myCSVfile:
        for line in myCSVfile:
            if fietsnummer and wachtwoord  in line:
                kaas = True
    if kaas:
        informatie()
    else:
        invalidinput(1)

def stallen():
    forget(1)
    print('stallen')

def ophalen():
    forget(1)
    print('ophalen')

def informatie():
    forget(1)
    print('informatie')

def overige():
    forget(1)
    print('overige')

main()
