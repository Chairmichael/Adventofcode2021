
def main():
	with open('input.txt') as input:
		gamma = ''
		occurences = [0] * 12 # number of occurences for 1 in each bit position
		for length, line in enumerate(input):
			for i, n in enumerate(line.rstrip()):
				occurences[i] += int(n)
		else:
			print(occurences, length)
			for x in occurences:
				gamma += str(x // ((length+1)//2))
			epsilon = int(gamma, 2) ^ 0b111111111111
			print(int(gamma, 2) * epsilon)


if __name__ == '__main__':
	main()
