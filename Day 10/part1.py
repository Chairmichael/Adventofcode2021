
def switch(c):
	table = {'(':')','{':'}','[':']','<':'>'}
	return table[c]

def main():
	data = (l.strip() for l in open('input.txt').readlines())
	total = 0
	table = {')': 3, ']': 57, '}': 1197, '>': 25137}
	for line in data:
		buffer = []
		for c in line:
			if c in '([{<':
				buffer.append(c)
			else:
				if c != switch(buffer[-1]):
					total += table[c]
					break
				else:
					buffer.pop()
	print(total)
if __name__ == '__main__':
	main()
