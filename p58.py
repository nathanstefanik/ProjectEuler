from sympy import isprime

diagonals = [8/13, [3, 5, 7, 13, 17, 31, 37, 43], [1, 9, 21, 25, 49]]
for size in range(9, 50000, 2):
	curr = size**2
	for i in range(0, 4):
		curr = size**2 + (-i * (size - 1))
		if isprime(curr):
			diagonals[1].append(curr)
		else:
			diagonals[2].append(curr)
	diagonals[0] = len(diagonals[1]) / ((size * 2) - 1)
	if diagonals[0] < 1/10:
		print(size)
		break