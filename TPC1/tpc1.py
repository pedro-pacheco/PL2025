import sys

def splits(line, delim):			#splits a string by the delimeter and also adds that delimiter to the resulting list
	res = line.split(delim)
	a = []
	for l in res:
		a.append(l)
		a.append(delim)
	op = a.pop()
	return a

def multisplit(line):				#splits a string into a list of strings separated by the different delimiters ('on', 'off' and '=') adding them to the list as well
	l = line
	c = []
	res = []
	a = splits(l, 'on')

	for s in a:
		c.extend(splits(s, "off"))
	
	for s in c:
			res.extend(splits(s, '='))
	
	return res
	
	
def getNumber(line):			#adds all the numbers in a string and returns the result
	cal = []
	num = 0
	for char in line:
		if char.isdigit():
			num=(10*num)+int(char)
		else:
			cal.append(num)
			num = 0
	cal.append(num)
	res = sum(tuple(cal))
	return res


def main():
	
	on = True
	mysum = 0

	for line in sys.stdin:
		if '***' == line.rstrip():
			break

		line = str.lower(line.rstrip('\n'))
		splitted = multisplit(line)

		for i in splitted:
			if i == "on":
				on = True
			elif i == "off":
				on = False
			elif i == "=":
				print(mysum)
			else:
				if on:
					mysum+=getNumber(i)
				else:
					mysum+=0

if __name__ == "__main__":
	main()