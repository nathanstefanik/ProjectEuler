# I realized in commented approach, integer values get too large. Can find an easier way.
# we can define a recursion for the numerator and denominator
# n(t) = n(t - 1) + 2d(t - 1)
# d(t) = n(t - 1) + d(t - 1)
# Let v_t = [[n_t], [d_t]] and v_0 = [[1], [1].
# Then, v_t = (A^t)v_0 where A = [[1, 2], [1, 1]]
# To make calculations easier, we can diagonalize A = PDP^-1
# from numpy import matmul
# from math import sqrt, ceil
# v_0 = [[1], [1]]
# P = [[sqrt(2), -sqrt(2)], [1, 1]]
# A = [[1 + sqrt(2), 0], [0, 1 - sqrt(2)]]
# Pin = [[1 / (2*sqrt(2)), 0.5], [-1 / (2*sqrt(2)), 0.5]]
# ans = 0
# for i in range(1, 10001):
# 	A_i = matmul(matmul(P, [[(1 + sqrt(2))**i, 0], [0, (1 - sqrt(2))**i]]), Pin)
# 	v_i = matmul(A_i, v_0)
# 	if len(str(ceil(v_i[0][0]))) > len(str(ceil(v_i[1][0]))):
# 		ans += 1
# 		print(ans)
# print(ans)

denominators = []

def next(fraction):
	return [fraction[0] + (2 * fraction[1]), fraction[0] + fraction[1]]

hi = [1, 1]
for i in range(1, 1001):
	sup = next(hi)
	if int(str(sup[1])[:3]) > 700:
		denominators.append(sup)
	if len(str(sup[1])) > 10:
		sup[0] = int(str(sup[0])[:-3])
		sup[1] = int(str(sup[1])[:-3])
	hi = sup
print(len(denominators))


