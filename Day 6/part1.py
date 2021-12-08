
def main():
	fish = list(map(int, open('input.txt').read().strip().split(',')))
	for day in range(80):
		new_fish = 0
		for i, f in enumerate(fish):
			if f == 0:
				fish[i] = 6
				new_fish += 1
			else:
				fish[i] -= 1
		fish.extend(8 for x in range(new_fish))
	print(len(fish))

if __name__ == '__main__':
	main()
