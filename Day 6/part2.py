
def main():
	fish = list(map(int, open('input.txt').read().strip().split(',')))
	fish_ages = [0 for x in range(9)]
	for f in fish:
		fish_ages[f] += 1
	for day in range(256):
		new_fish = fish_ages.pop(0)
		fish_ages.append(new_fish)
		fish_ages[6] += new_fish

	print(sum(fish_ages))

if __name__ == '__main__':
	main()
