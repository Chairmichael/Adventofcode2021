
def switch(c):
	table = {'(':')','{':'}','[':']','<':'>'}
	return table[c]

def main():
	data = [l.strip() for l in open('input.txt').readlines()]
	total = 0
	table = {')': 3, ']': 57, '}': 1197, '>': 25137}
	for line in data.copy():
		buffer = []
		for c in line:
			if c in '([{<':
				buffer.append(c)
			else:
				if c != switch(buffer[-1]):
					total += table[c]
					data.remove(line)
					break
				else:
					buffer.pop()
	print(total)

	scores = []
	table2 = {'(': 1, '[': 2, '{': 3, '<': 4}
	for line in data.copy():
		buffer = []
		for c in line:
			if c in '([{<':
				buffer.append(c)
			else:
				if c != switch(buffer[-1]):
					total += table[c]
					data.remove(line)
					break
				else:
					buffer.pop()
		score = 0
		for x in buffer[::-1]:
			score *= 5
			score += table2[x]
		scores.append(score)
	print(sorted(scores)[(len(scores)//2)])


if __name__ == '__main__':
	main()
