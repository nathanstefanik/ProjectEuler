with open('p059_cipher.txt', 'r') as myfile:
	line = myfile.readline()
	codes = [int(n) for n in line.split(',')]

def binary(n):
	return '{:b}'.format(n).zfill(8)

def xor(a, b):
	return int(''.join(['1' if binary(a)[i] != binary(b)[i] else '0' for i in range(0, 8)]), 2)

# # possible lowercase letters
# good = [[i for i in range(97, 123)], [i for i in range(97, 123)], [i for i in range(97, 123)]]
# # used the following code to weed out possible letters for positions
# for i in range(3, 55, 3):
# 	for j in range(97, 123):
# 		result = [xor(code, j) for code in codes[i - 3:i]]
# 		print('\n', j)
# 		print(result)
# 		print(good)
# 		for char in result:
# 			# not a letter
# 			if (char > 122 or char < 65) and char != 32 and char != 56 and char != 54 and (j in good[result.index(char)]):
# 				print(j, ' made ', char, ' bad')
# 				print(result.index(char))
# 				good[result.index(char)].remove(j)
# # code is either exp or sxp: [101, 120, 112] or [115, 120, 112]

chars = []
ans = []
good = [101, 120, 112]
for i in range(2, len(codes), 3):
	chars.append(chr(xor(codes[i - 2], good[0])))
	ans.append(xor(codes[i - 2], good[0]))
	chars.append(chr(xor(codes[i - 1], good[1])))
	ans.append(xor(codes[i - 1], good[1]))
	chars.append(chr(xor(codes[i], good[2])))
	ans.append(xor(codes[i], good[2]))

print(''.join(chars))
print(sum(ans))
