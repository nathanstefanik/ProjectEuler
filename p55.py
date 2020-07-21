def isPalindrome(n):
	return int(''.join([digit for digit in str(n)[::-1]])) == n

def isLychrel(n):
	return isLychrelHelper(n, 1)

def isLychrelHelper(n, k):
	reverse = int(''.join([digit for digit in str(n)[::-1]]))
	x = reverse + n
	if isPalindrome(x):
		return (x, -1)
	elif k >= 50:
		return (x, k)
	else: 
		return isLychrelHelper(reverse + n, k + 1)

ans = []
for i in range(1, 10000):
	if isLychrel(i)[1] == 50:
		ans.append(i)
print(len(ans))
