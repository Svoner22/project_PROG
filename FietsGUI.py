#Fietsenstalling

from tkinter import Tk, Label, Button, Entry, END, PhotoImage, Text, Scrollbar
import csv
import random
import threading
import datetime
import time

"""
Nog in te leveren/schrijven functies:
loginfuncties: wachtwoord minimaal 5 chars!
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

def maketime():
    global kaas
    kaas = True
    while kaas:
        currenttime = str(datetime.datetime.now())
        labeltext = currenttime[0:16]
        label = yellowlabel(labeltext)
        label.grid(row = 0, column = 10)
        time.sleep(10)
        label.grid_forget()

def main():
    global root
    root = Tk()
    root.configure(background = 'yellow')
    root.geometry("1920x1020")
    initiate()
    timethread = threading.Thread(target=maketime)
    timethread.start()
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
    titlelabel = yellowlabel('NS fietsenstalling      ')
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
        if kaas == True:
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
    global fietsnummer
    global wachtwoord
    csvlist = []
    with open("stallen.csv", "r") as myCSVfile:
        for row in myCSVfile:
            csvlist.append(row)
    if len(csvlist) < 500:
        fietsnummer = fietsnummerentry.get()
        wachtwoord = wachtwoordentry.get()
        kaas = False
        with open("register.csv", "r") as myCSVfile:
            for row in myCSVfile:
                if fietsnummer and wachtwoord in row and len(fietsnummer) == 5 and len(wachtwoord) == 5 :
                    kaas = True
        if kaas == True:
            stallen()
        else:
            invalidinput(1)
    else:
        vollestallinglabel = yellowlabel('Sorry, alle stallingen zijn vol')
        que[1] = [vollestallinglabel]
        vollestallinglabel.grid(row = 1, columnspan = 2)

def ophalen_verify():
    global fietsnummer
    global wachtwoord
    fietsnummer = fietsnummerentry.get()
    wachtwoord = wachtwoordentry.get()
    kaas = False
    with open("register.csv", "r") as myCSVfile:
        for line in myCSVfile:
            if fietsnummer and wachtwoord in line and len(fietsnummer) == 5 and len(wachtwoord) == 5:
                kaas = True
    if kaas == True:
        ophalen()
    else:
        invalidinput(1)

def informatie_verify():
    global fietsnummer
    global wachtwoord
    fietsnummer = fietsnummerentry.get()
    wachtwoord = wachtwoordentry.get()
    kaas = False
    with open("register.csv", "r") as myCSVfile:
        for line in myCSVfile:
            if fietsnummer and wachtwoord in line and len(fietsnummer) == 5 and len(wachtwoord) == 5:
                kaas = True
    if kaas == True:
        informatie()
    else:
        invalidinput(1)

def stallen():
    forget(1)
    stallenlijst = []
    with open("register.csv", "r") as myCSVfile:
        for row in myCSVfile:
            stallenlijst.append(row[3])
    for item in range(500):
        if item not in stallenlijst:
            stalnummer = item
            break
    with open("stallen.csv", "a", newline="") as doc:
        writer = csv.writer(doc, delimiter = ",")
        time = datetime.datetime.now()
        writer.writerow((fietsnummer, wachtwoord, time, stalnummer))
    stallenlabel = yellowlabel('Uw stalnummer is: '+str(stalnummer))
    que[1]=[stallenlabel]
    stallenlabel.grid(row = 1, columnspan = 2)

def ophalen():
    forget(1)
    eigenaarlst = []
    nummerlst = []
    time = []
    with open("./stallen.csv", "r") as doc:
        reader = csv.DictReader(doc)
        for row in reader:
            eigenaarlst.append(row["naam"])
            nummerlst.append(row["nummer van de fiets"])
            time.append(row["time"])
    while True:
        eigenaar = input("Naam: ")
        if eigenaar in eigenaarlst:
            break
        print("Naam onbekend")
    while True:
        num_fiets = input("Nummer van de fiets: ")
        if num_fiets == nummerlst[eigenaarlst.index(eigenaar)]:
            break
        print("error")
    eigenaarlst.remove(eigenaar)
    nummerlst.remove(num_fiets)
    with open("./stallen.csv", "w", newline="") as doc:
        writer = csv.writer(doc, delimiter = ",")
        writer.writerow(("naam", "nummer van de fiets", "time"))
        for i in eigenaarlst:
            timew = time[eigenaarlst.index(i)]
            naam = i
            nummer = nummerlst[eigenaarlst.index(i)]
            writer.writerow((naam, nummer, timew))
    print("ok")

def informatie():
    forget(1)
    print('informatie')

def overige():
    forget(1)
    print('overige')

main()
