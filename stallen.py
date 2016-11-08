import csv
import datetime


def stallen():

    with open("./stallen.csv", "r+", newline="") as doc:
        reader = csv.DictReader(doc)
        for row in reader:
            continue


        writer = csv.writer(doc, delimiter = ",")
        naam = input("Naam")
        nummer = input("nummer")
        time = datetime.datetime.now()
        writer.writerow((naam, nummer, time))

stallen()
