
def main():
	with open('input.txt') as input:
		horizontal = 0
		vertical = 0
		aim = 0
		for line in input:
			command = line.split()
			if command[0] == 'forward':
				horizontal += int(command[1])
				vertical += aim * int(command[1])
			elif command[0] == 'down':
				aim += int(command[1])
			elif command[0] == 'up':
				aim -= int(command[1])

		print(horizontal * vertical)

if __name__ == '__main__':
	main()
