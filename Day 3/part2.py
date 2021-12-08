###
### DOESNT WORK
###
def main():
	with open('input.txt') as input:
		numbers = [x.strip() for x in input]
		most_common = numbers.copy()
		least_common = numbers.copy()
		occurences = []
		for i in range(len(numbers[0])):
			occurences.append(0)
			for num in most_common:
				occurences[i] += int(num[i])
			# most common bit, if equally as common, then 1
			common_bit = str(occurences[i] // (len(most_common) // 2))
			temp = []
			for num in most_common:
				if num[i] == common_bit:
					temp.append(num)
			most_common = temp
			if len(most_common) == 1:
				print(f'finished: {i}')
				break

		occurences = []
		for i in range(len(numbers[0])):
			occurences.append(0)
			for num in least_common:
				occurences[i] += int(num[i])
			# most common bit, if equally as common, then 1
			common_bit = str(occurences[i] // (len(least_common) // 2))
			temp = []
			for num in least_common:
				if num[i] != common_bit:
					temp.append(num)
			least_common = temp
			if len(least_common) == 1:
				print(f'finished: {i}')
				break


		print(most_common)
		print(least_common)

		print(int(most_common[0],2) * int(least_common[0],2))


if __name__ == '__main__':
	main()

