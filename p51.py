# Claim: only need to check primes with n digit replacements where n = 3k for some natural number k
# Proof: Let k not divisible by 3 be the number of digits to be replaced. 
# Let p be the sum of the no-replace digits be 0 (mod 3).
# Then, by the pigeon hole principle, there can not be a prime family of size 8 since there will be at least 3
# final configurations that will be divisible by 3. The same can be done with p congruent to 1 (mod 3) and 2 (mod 3)

import itertools
with open('primes.txt', 'r') as myfile:
	lines = myfile.readlines()
	# Cutting down range to search
	primes = [int(p) for p in lines[168:]]
	primes_to_iterate = primes

def hasTriple(n):
	number = list(set([digit for digit in str(n)]))
	good = ''
	ans = [False, []]
	for i in number:
		if str(n).count(i) == 3:
			good = i
			ans[0] = True
	if type(ans) == list:
		for i in range(0, len(str(n))):
			if str(n)[i] == good:
				ans[1].append(i)
	return ans


def primeFamily(prime, digits_to_replace):
	family = []
	for i in range(0, 10):
		digits = [digit for digit in str(prime)]
		for place in digits_to_replace:
			digits[place] = str(i)
		if int(''.join(digits)) in primes:
			if ''.join(digits)[0] != '0':
				family.append(int(''.join(digits)))
	return family

def getAnswer():
	maxi = 0
	for prime in primes_to_iterate:
		if hasTriple(prime)[0]:
			combo = hasTriple(prime)[1]
			if len(primeFamily(prime, combo)) == 8:
				return min(primeFamily(prime, combo))

print(getAnswer())