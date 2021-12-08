
def main():
	with open('input.txt') as input:
		measure = -1
		count = -1
		for line in input:
			if int(line) > measure:
				count += 1
			measure = int(line)
		print(count)


if __name__ == '__main__':
	main()
