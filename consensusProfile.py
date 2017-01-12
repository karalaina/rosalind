def processFile(filename):
	file = open(filename).read()
	l = file.split('>')
	l = l[1:]
	dnaList = []
	for i in l:
		index = i.find("\n")
		dnaList.append(i[index:].replace("\n", ""))
	
	aList = profileCalc(dnaList, "A")
	cList = profileCalc(dnaList, "C")
	gList = profileCalc(dnaList, "G")
	tList = profileCalc(dnaList, "T")
	
	return [aList, cList, gList, tList]
		
def profileCalc(dnaList, base):
	profile = []
	for i in dnaList[0]:
		profile.append(0);
	index = 0
	for i in dnaList:
		for j in range(0, len(i)):
			if i[j] == base:
				profile[j] += 1
	return profile
			
def makeConsensus():
	profileList = processFile("in.txt")
	consensus = ""
	count = 0
	while count < len(profileList[0]):
		currIndex = []
		for i in range(0,4):
			currIndex.append(profileList[i][count])
		base = findLargest(currIndex)
		consensus += base
		count += 1
	return consensus, profileList
	
def findLargest(list):
	largest = list[0]
	base = 0
	for i in range(0, len(list)):
		if list[i] > largest:
			largest = list[i]
			base = i
	baseLet = findBase(base)
	return baseLet

def findBase(base):
	#0 = A, 1 = C, 2 = G, 3 = T
	if base == 0:
		return "A"
	elif base == 1:
		return "C"
	elif base == 2:
		return "G"
	elif base == 3:
		return "T"

def makeOutput():
	consensus, profileList = makeConsensus()
	file = open("out.txt", 'w')
	file.write(consensus + '\n')
	for i in range(0, len(profileList)):
		profileList[i] = map(str, profileList[i])
		profileList[i] = " ".join(profileList[i])
	file.write("A: "+profileList[0]+'\n')
	file.write("C: "+profileList[1]+'\n')
	file.write("G: "+profileList[2]+'\n')
	file.write("T: "+profileList[3]+'\n')
	
makeOutput()