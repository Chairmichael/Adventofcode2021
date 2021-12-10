
def slt(n, i, data):
	if i == -1 or i == len(data):
		return True
	else:
		return n < data[i]

# for el: scan horizontally and then vertically
def main():
	data = [[int(x) for x in row] for row in open('input.txt').read().split()]
	

if __name__ == '__main__':
	main()
