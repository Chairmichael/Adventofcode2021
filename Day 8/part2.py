from timeit import Timer

def main():
	data = [l.split()[0:10]+l.split()[11:] for l in open('input.txt').readlines()]
	legend = ['' for x in range(10)]
	for line in data:
		print(line)
		for digit in line:
			if len(''.join(legend)) == 16:
				break # finished finding uniques
			elif len(digit) == 2:
				legend[1] = digit
			elif len(digit) == 3:
				legend[7] = digit
			elif len(digit) == 4:
				legend[4] = digit
			elif len(digit) == 7:
				legend[8] = digit
		# segments
		top = [x for x in legend[7] if x not in legend[1]][0]
		print(legend[7], legend[1], top)
		# 9 = top-seg + four-segs + bottom-seg
		# bottom-seg = 9 - top-seg + four-segs
		bottom = ''
		print(''.join(sorted(legend[4] + top)))
		for digit in line:
			if ''.join(sorted(legend[4] + top)) in ''.join(sorted(digit)):
				bottom = [x for x in digit if x not in legend[4] + top][0]
		print(bottom)
		break



if __name__ == '__main__':
	main()