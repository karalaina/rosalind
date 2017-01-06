#counts num of each nucleotide base in DNA strand

def countNuc(fileName):
    s = open(fileName).read()
    l = list(s)
    d = dict({'A':0, 'C':0, 'G':0, 'T':0})
    for i in l:
        for k in d:
            if i==k:
                d[k] = d[k]+1
    print str(d['A'])+" "+str(d['C'])+" "+str(d['G'])+" "+str(d['T'])