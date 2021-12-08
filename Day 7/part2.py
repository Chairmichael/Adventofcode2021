
from statistics import mean
from math import floor

# 1:1, 2:2+1, 3:3+3, 4:4+6
def fuel_cost(x):
	n = 0
	for i in range(x+1):
		n += i
	return n

def main():
	pos = list(map(int,open('input.txt').read().strip().split(',')))
	print(min(sum(fuel_cost(abs(x-floor(mean(pos)))) for x in pos),
			sum(fuel_cost(abs(x-floor(mean(pos))+1)) for x in pos)))
	# costs = []
	# for i in range(len(pos)):
	# 	total = 0
	# 	for x in pos:
	# 		total += fuel_cost(abs(x-i))
	# 	costs.append(total)
	# print(f'minimum: {min(costs)}')
	# print(f'index:   {costs.index(min(costs))}')

if __name__ == '__main__':
	main()
