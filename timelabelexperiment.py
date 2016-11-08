from tkinter import Tk, Label
import time
import datetime
import threading
root = Tk()
root.geometry("500x500")
def maketime():
    global kaas
    kaas = True
    while kaas:
        currenttime = str(datetime.datetime.now())
        labeltext = currenttime[0:16]
        label = Label(text = labeltext)
        label.grid(row = 0, column = 0)
        time.sleep(60)
        label.grid_forget()
timethread = threading.Thread(target=maketime)
timethread.start()
root.mainloop()
kaas = False
