
def main():
	with open('input.txt') as input:
		count = 0
		for line in input:
			nums = line.split()[-4:]
			# digits with length of 2,3,4 or 7 are unique
			for n in nums:
				if len(n) in [2,3,4,7]: count += 1
		print(count)


if __name__ == '__main__':
	main()