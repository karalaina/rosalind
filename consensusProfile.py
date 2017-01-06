
def processFile(filename):
	file = open(filename).read()
	l = file.split('>')
	for item in range(0, len(l)):
		i = l[item].find('\n')
		l[item] = l[i:]
	
	print l
			
processFile("testFile.txt")
		
		