#calcs GC content of DNA strands returns one with highest value

def calcGC(fileName):
    s = open(fileName).read()
    l = s.split('>')
    l.remove('')
    for i in range(0,len(l)):
        l[i] = l[i].replace('\n','')

    cont = []
    gc = 0
    highest = 0
    index = 0
    for i in range(0,len(l)):
        for k in l[i]:
            if (k == 'C') or (k == 'G'):
                gc += 1.000
        gcCont = (gc/(len(l[i])-13))*100
        cont.append(gcCont)
        gc = 0
        if gcCont > highest:
            index = i
            highest = gcCont
    print l[index][0:13]
    print cont[index]