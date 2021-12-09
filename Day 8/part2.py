from timeit import Timer

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
	data = [l.split()[0:10]+l.split()[11:] for l in open('input.txt').readlines()]
	total_output = 0
	for l in data:
		legend = ['' for x in range(10)]
		line = [''.join(sorted(digit)) for digit in l]
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

		# 9 = top-seg + four-segs + bottom-seg
		for digit in filter(lambda x: x not in legend, line):
			diff = str_diff(digit, legend[4] + top)
			if len(diff[0]) == 1 and diff[1] == '':
				legend[9] = digit

		# 9 - 3 = top-left-seg
		# 3 = 9 - top-left-seg
		for digit in filter(lambda x: x not in legend, line):
			diff = str_diff(legend[9], digit)
			if len(diff[0]) == 1 and diff[1] == '':
				legend[3] = digit

		# 0 = 8 - middle-seg
		for digit in filter(lambda x: x not in legend, line):
				diff = str_diff(legend[8], digit)
				if len(diff[0]) == 1 and diff[1] == '':
					if str_diff(digit, legend[1])[1] == '': # check if digit contains 1
						legend[0] = digit
					else:
						legend[6] = digit

		# 5 = 6 - top-right-seg
		for digit in filter(lambda x: x not in legend, line):
				diff = str_diff(legend[6], digit)
				if len(diff[0]) == 1 and diff[1] == '':
					legend[5] = digit

		# 2 (leftover)
		for digit in filter(lambda x: x not in legend, line):
				diff = str_diff(legend[6], digit)
				if len(diff[0]) == 2 and diff[1] == 1:
					legend[2] = digit

		output_signals = filter(lambda x: ''.join(sorted(x)), line[-4:])
		for i, output in enumerate(output_signals):
			try:
				total_output += legend.index(output) * (10 ** (3 - i))
			except Exception as e:
				print(e)
				breakpoint()
	print(total_output)



if __name__ == '__main__':
	# print(str_diff('abdefg','acdeg'))
	main()
