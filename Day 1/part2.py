
def main():
	with open('input.txt') as input:
		sumation = 0
		last_sumation = 0
		increases = 0
		depths = [int(line) for line in input]
		for i in range(2, len(depths)):
			if last_sumation == 0 and sumation == 0:
				sumation = depths[i-2] + depths[i-1] + depths[i]
			else:
				sumation = depths[i-2] + depths[i-1] + depths[i]
				if sumation > last_sumation:
					increases += 1
				last_sumation = sumation
		print(increases)


if __name__ == '__main__':
	main()
