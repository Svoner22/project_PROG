import csv

def ophalen():

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


ophalen()
