# will have to run python3.8 to use math.comb()
from math import comb
counter = 0
for n in range(20, 100):
	good = 0
	for r in range(4, (n // 2) + 1):
		if comb(n + 1, r) >= 1000000:
			good += 2
	if n % 2 == 1 and comb(n + 1, (n + 1) // 2) >= 1000000:
		good += 1
	counter += good
print(counter)