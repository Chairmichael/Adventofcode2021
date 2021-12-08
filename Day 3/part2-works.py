
def main():
	common = [l.strip() for l in open('input.txt').readlines()]
	least = common.copy()

	for i in range(len(common[0])):
		if len(common) > 1:
			compare_common = [0,0]
			compare_least = [0,0]
			for n in common:
				compare_common[int(n[i])] += 1
			common_bit = ''
			if compare_common[0] <= compare_common[1]: common_bit = '1'
			elif compare_common[0] > compare_common[1]: common_bit = '0'
			mask = set()
			for n in common:
				if n[i] != common_bit:
					mask.add(n)
			common = list(set(common) - mask)

		if len(least) > 1:
			for n in least:
				compare_least[int(n[i])] += 1
			least_bit = ''
			if compare_least[0] <= compare_least[1]: least_bit = '0'
			elif compare_least[0] > compare_least[1]: least_bit = '1'
			mask = set()
			for n in least:
				if n[i] != least_bit:
					mask.add(n)
			least = list(set(least) - mask)

		if len(common) == 1 and len(least) == 1: break


	print(f'{common}\n{least}')
	print(f'product = {int(common[0], 2) * int(least[0], 2)}')


if __name__ == '__main__':
	main()

