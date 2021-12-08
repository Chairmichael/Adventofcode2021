
def sign(n):
	if n == 0:
		return 0
	else:
		return n//abs(n)

def main():
	coords = []
	with open('input.txt') as input:
		for line in input:
			coords.append(list(map(int, line.replace('->','').replace(',',' ').split())))

	max_c = max(max(c) for c in coords) + 1
	chart = [[0 for x in range(max_c)] for y in range(max_c)]

	for c in coords:
		dx = c[0] - c[2]
		dy = c[1] - c[3]
		for i in range(max(abs(dx), abs(dy)) + 1):
			chart[c[3] + (sign(dy) * i)][c[2] + (sign(dx) * i)] += 1

	# [print(x) for x in coords]
	# [print(''.join([str(x) if x != 0 else '.' for x in row])) for row in chart]

	print(sum(sum([1 if n > 1 else 0 for n in row]) for row in chart))

if __name__ == '__main__':
	main()
