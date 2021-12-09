
def slt(n, i, data):
	if i == -1 or i == len(data):
		return True
	else:
		return n < data[i]

def main():
	data = [[int(x) for x in row] for row in open('input.txt').read().split()]
	for line in data:
		for i, n in enumerate(line):
			pass

if __name__ == '__main__':
	main()
