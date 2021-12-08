
def main():
	with open('input.txt') as input:
		l = []
		dups = 0
		for x in input:
			x = x.rstrip()
			if x in l:
				dups += 1
			else:
				l.append(x)
		print(f'dups = {dups}\tlen = {len(l)}')

if __name__ == '__main__':
	main()
