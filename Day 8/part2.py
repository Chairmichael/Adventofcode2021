from timeit import Timer

def str_sort_list(data):
	for l in data:
		yield [''.join(sorted(s)) for s in l]

def str_same(a,b):
	if len(a) != len(b):
		return False
	for x in a:
		if x not in b:
			return False
	return True

def str_in(a,b):
	for c in b:
		if c not in a:
			return False
	return True

def main():
	data = open('input.txt').readlines()
	signal_paterns = str_sort_list(l.split()[0:10] for l in data)
	output_signals = str_sort_list(l.split()[11:] for l in data)
	total_output = 0

	for line, outputs in zip(signal_paterns, output_signals):
		legend = [''] * 10
		for digit in line.copy():
			if len(''.join(legend)) == 16:
				break # finished finding uniques
			elif len(digit) == 2:
				legend[1] = digit
				line.remove(digit)
			elif len(digit) == 3:
				legend[7] = digit
				line.remove(digit)
			elif len(digit) == 4:
				legend[4] = digit
				line.remove(digit)
			elif len(digit) == 7:
				legend[8] = digit
				line.remove(digit)

		# 9 = top-seg + four-segs + bottom-seg
		for digit in line:
			if len(digit) == 6 and str_in(digit, legend[4]):
				legend[9] = digit
				line.remove(digit)
				break

		# 9 - 3 = top-left-seg
		# 3 = 9 - top-left-seg
		for digit in line:
			if len(digit) == 5 and str_in(digit, legend[1]):
				legend[3] = digit
				line.remove(digit)
				break

		# 0 = 8 - middle-seg
		for digit in line:
			if str_in(digit, legend[1]) and len(digit) == 6:
				legend[0] = digit
				line.remove(digit)
				break

		# 6: only signal left with length of 6
		for digit in line:
			if len(digit) == 6:
				legend[6] = digit
				line.remove(digit)
				break

		# 5 = 6 - top-right-seg
		for digit in line:
			if str_in(legend[6], digit):
				legend[5] = digit
				line.remove(digit)
				break

		# 2 (leftover)
		if len(line) == 1:
			legend[2] = line[0]
		else:
			breakpoint()

		sumation = 0
		for n, output in enumerate(outputs):
			for i, x in enumerate(legend):
				if str_same(x, output):
					total_output += i * (10 ** (3 - n))
					break
		# total_output += sumation
		# sumation = []
		# for n, output in enumerate(outputs):
		# 	for i, x in enumerate(legend):
		# 		if str_same(x, output):
		# 			sumation.append(str(i))
		# 			break
		# total_output += int(''.join(sumation))

	print(total_output)
	# 974512



if __name__ == '__main__':
	# print(str_diff('abdefg','acdeg'))
	main()
