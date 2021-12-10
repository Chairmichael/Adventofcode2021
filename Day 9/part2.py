
def slt(n, i, data):
	if i == -1 or i == len(data):
		return True
	else:
		return n < data[i]

def main():
	data = [[int(x) for x in row] for row in open('input.txt').read().split()]
	with open('output.txt','w') as output:
		for line in data:
			output.write(''.join('.' if x != 9 else 'X' for x in line) + '\n')

if __name__ == '__main__':
	main()
