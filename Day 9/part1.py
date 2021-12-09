
def main():
	data = [[int(x) for x in row] for row in open('input.txt').read().split()]
	risk_level = 0
	for i, row in enumerate(data):
		for j, num in enumerate(row):
			passes = 0
			if (j+1 >= len(row) or num < data[i][j+1]) and num < data[i][j-1]:
				passes += 1
			elif (j-1 < 0 or num < data[i][j-1]) and num < data[i][j+1]:
				passes += 1
			if (i+1 >= len(data) or num < data[i+1][j]) and num < data[i-1][j]:
				passes += 1
			elif (i-1 < 0 or num < data[i-1][j]) and num < data[i+1][j]:
				passes += 1
			if passes == 2:
				risk_level += 1 + num
	print(risk_level)

if __name__ == '__main__':
	main()
