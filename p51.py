import itertools
with open('primes.txt', 'r') as myfile:
	lines = myfile.readlines()
	primes = [int(p) for p in lines]
	primes_to_iterate = primes

def primeFamily(prime, digits_to_replace):
	family = []
	for i in range(0, 10):
		digits = [digit for digit in str(prime)]
		for place in digits_to_replace:
			digits[place - 1] = str(i)
		if int(''.join(digits)) in primes:
			if ''.join(digits)[0] != '0':
				family.append(int(''.join(digits)))
	return family

def getAnswer():
	maxi = 0
	for prime in primes_to_iterate[1616:]:
		currIndex = primes_to_iterate.index(prime)
		for i in range(1, 4):
			combos_to_replace = list(itertools.combinations([j for j in range(1, len(str(prime)))], i))
			for combo in combos_to_replace:
				if len(primeFamily(prime, combo)) > maxi:
					maxi = len(primeFamily(prime, combo))
					print('\n--------',prime,'----------')
					print(combo, ': ', primeFamily(prime, combo))
					print('length: ', maxi)
				if len(primeFamily(prime, combo)) == 8:
					return min(primeFamily(prime, combo))

print(getAnswer())
