with open('poker.txt', 'r') as myfile:
	lines = myfile.readlines()
	rounds = [hand.strip('\n').split() for hand in lines]

def rankSort(ranks):
	ranklist = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
	ranks.sort(key=lambda x: ranklist.get(x), reverse=True)
	return ranks

def isStraight(ranks):
	ranklist = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
	ranks.sort(key=lambda x: ranklist.get(x))
	for i in range(0, 4):
		if ranklist.get(ranks[i]) + 1 != ranklist.get(ranks[i + 1]):
			return False
	return True

def number(rank):
	ranklist = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
	return ranklist.get(rank)

# quickly done, functional but messy
def gethand(hand):
	suits, ranks = [card[1] for card in hand], [card[0] for card in hand]
	ranks = rankSort(ranks)
	score = 0
	high = number(rankSort(ranks)[0])
	kicker = 0
	# 5 - flush
	if suits.count(suits[0]) == 5:
		score = 5 + high / 100

	# 4 - straight
	if isStraight(ranks):
		score += 4 + high / 100
		return [round(score, 10), number(rankSort(ranks)[0])]
	
	# 7 - quads
	for card in ranks:
		if ranks.count(card) == 4:
			score = 7 + number(card) / 100
			break
	if score // 1 == 7:
		kicker = number(ranks[0]) if ranks.count(ranks[0]) == 1 else number(ranks[-1])
		return [round(score, 10), kicker]
	
	# 6 - full house
	unique = []
	for card in ranks:
		if card not in unique:
			unique.append(card)
	if len(unique) == 2:
		upper = number(ranks[0]) if ranks.count(ranks[0]) == 3 else number(ranks[-1])
		lower = number(unique[0]) if number(unique[0]) != upper else number(unique[1])
		return [round(6 + (upper / 100) + (lower / 10000), 10), max(upper, lower)]
	
	# 3 - trips, 2 - two pair
	if len(unique) == 3:
		trips = -3
		pair1 = -1
		pair2 = -2
		for card in ranks:
			if ranks.count(card) == 3:
				trips = card
			if ranks.count(card) == 2 :
				if pair1 != -1:
					pair2 = card
				else:
					pair1 = card 
			if ranks.count(card) == 1 and number(card) >= kicker:
				kicker = number(card)
		if trips != -3:
			for card in ranks:
				if card != trips and card != kicker:
					kicker2 = card
			return [round(3 + number(trips) / 100, 10), round(kicker + (number(kicker2) / 100), 1)]
		else:
			return [round(2 + max(number(pair1), number(pair2)) / 100 + min(number(pair1), number(pair2)) / 10000, 10), kicker]
	# 1 - one pair
	if len(unique) == 4:
		for card in ranks:
			if ranks.count(card) == 2:
				pair = card
			else:
				if number(card) >= kicker:
					kicker = number(card)
		return [round(1 + number(pair) / 100, 10), kicker]
	
	# 0 - high 
	return [round((number(ranks[4]) / 100 + number(ranks[3]) / 10000 + number(ranks[2]) / 1000000 + number(ranks[1]) / 100000000 +\
	number(ranks[0]) / 10000000000), 10), kicker]

ans = 0
for hand in rounds:
	if gethand(hand[:5])[0] > gethand(hand[5:])[0]:
		ans += 1
	elif gethand(hand[:5])[0] == gethand(hand[5:])[0]:
		if gethand(hand[:5])[1] > gethand(hand[5:])[1]:
			ans += 1
print(ans)
