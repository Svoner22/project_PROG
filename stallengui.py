def informatie():
    forget(1)
    for item in registerlist:
        if item[2] == fietsnummer:
            index = registerlist.index(item)
            break
    staltime = datetime.datetime.strptime(registerlist[index][5], "%Y-%m-%d %H:%M:%S.%f")
    stalledtime =  datetime.datetime.now() - staltime
    stallnumber = registerlist[index][4]
    staltimelabel = yellowlabel('Uw fiets is gestald op: '+staltime)
    stalledtimelabel = yellowlabel('Uw fiets is '+stalledtime+' gestald')
    stallnumberlabel = yellowlabel('Uw fiets is gestald in stalnummer: '+stallnumber)
    que[1] = [staltimelabel, stalledtimelabel, stallnumberlabel]
    staltimelabel.grid(row = 1, columnspan = 2)
    stalledtimelabel.grid(row = 2, columnspan = 2)
    stallnumberlabel.grid(row = 3, columnspan = 2)
