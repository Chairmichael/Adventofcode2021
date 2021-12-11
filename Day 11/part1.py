
def main():
	data = [[int(x) for x in row] for row in open('input.txt').read().split()]
	global count
	count = 0
	flashed = []
	# [print(''.join(str(x) for x in row)) for row in data]

	def flash(i, j, l=data, flashed=flashed):
		global count
		if data[i][j] > 9 and (i,j) not in flashed:
			data[i][j] = 0
			count += 1
			flashed.append((i,j))
			if i-1 != -1:
				data[i-1][j] += 1
				flash(i-1,j)
				if j-1 != -1:
					data[i-1][j-1] += 1
					flash(i-1,j-1)
				if j+1 != len(data[i-1]):
					data[i-1][j+1] += 1
					flash(i-1,j+1)
			if i+1 != len(data):
				data[i+1][j] += 1
				flash(i+1,j)
				if j-1 != -1:
					data[i+1][j-1] += 1
					flash(i+1,j-1)
				if j+1 != len(data[i+1]):
					data[i+1][j+1] += 1
					flash(i+1,j+1)
			if j-1 != -1:
				data[i][j-1] += 1
				flash(i,j-1)
			if j+1 != len(data[i]):
				data[i][j+1] += 1
				flash(i,j+1)

		else:
			return

	for x in range(100):
		flashed = []
		for i in range(len(data)):
			for j in range(len(data[i])):
				data[i][j] += 1
		for i in range(len(data)):
			for j in range(len(data[i])):
				flash(i,j)
		# print('')
		# [print(''.join(str(x) for x in row)) for row in data]
		# # breakpoint()
	print(count)

if __name__ == '__main__':
	main()
