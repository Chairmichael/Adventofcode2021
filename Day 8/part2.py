
def main():
	data = [l.split()[0:10]+l.split()[11:] for l in open('input.txt').readlines()]
	legend = ['' for x in range(10)]
	for line in data:
		for digit in line:
			if len(''.join(legend)) == 16:
				break # finished finding uniques
			elif len(digit) == 2:
				legend[1] = digit
			elif len(digit) == 3:
				legend[7] = digit
			elif len(digit) == 4:
				legend[4] = digit
			elif len(digit) == 7:
				legend[8] = digit
		





if __name__ == '__main__':
	main()