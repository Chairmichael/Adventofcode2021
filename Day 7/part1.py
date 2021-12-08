
from statistics import median

def main():
	pos = list(map(int,open('input.txt').read().strip().split(',')))
	print(sum(abs(x-median(pos)) for x in pos))

if __name__ == '__main__':
	main()
