
def main():
	with open('input.txt') as input:
		horizontal = 0
		vertical = 0
		for line in input:
			print(line)
			command = line.split()
			print(command)
			if command[0] == 'forward':
				horizontal += int(command[1])
			elif command[0] == 'down':
				vertical += int(command[1])
			elif command[0] == 'up':
				vertical -= int(command[1])
		print(horizontal * vertical)

if __name__ == '__main__':
	main()
