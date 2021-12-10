from timeit import Timer

def str_sort_list(data):
	for l in data:
		yield [''.join(sorted(s)) for s in l]

def str_diff(a,b):
	c = ['','']
	for x in a:
		if x not in b:
			c[0] += x
	for x in b:
		if x not in a:
			c[1] += x
	return c # c[0]: a has, not b; c[1]: b has, not a

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

		# top segment
		top = next(x for x in legend[7] if x not in legend[1])

		# 9 = top-seg + four-segs + bottom-seg
		for digit in line:
			if ''.join(sorted(legend[4] + top)) in digit:
				legend[9] = digit
				line.remove(digit)
				break

		# 9 - 3 = top-left-seg
		# 3 = 9 - top-left-seg
		for digit in line:
			if digit in legend[9]:
				legend[3] = digit
				line.remove(digit)
				break

		# 0 = 8 - middle-seg
		for digit in line:
			if digit in legend[8]:
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
			if digit in legend[6]:
				legend[5] = digit
				line.remove(digit)
				break

		# 2 (leftover)
		legend[2] = line[0]

		print(legend, len(legend))
		print(outputs)
		return

		for i, output in enumerate(outputs):
			total_output += legend.index(output) * (10 ** (3 - i))

	print(total_output)



if __name__ == '__main__':
	# print(str_diff('abdefg','acdeg'))
	main()
