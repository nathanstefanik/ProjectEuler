def sameDigits(a, b):
	check = list(str(b))
	for i in str(a):
		if i in check:
			check.remove(i)
	return len(check) == 0

# Gambling that the answer is within this range
for i in range(1, 100000):
	good = '1' + str(i)
	check = int(good)
	if sameDigits(check, check * 2) and sameDigits(check, check * 3) and sameDigits(check, check * 4) and\
	sameDigits(check, check * 5) and sameDigits(check, check * 6):
		print(check)
		break