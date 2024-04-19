import random

card_type = ["黑桃","红桃","梅花","方块"]
number = [i for i in range(2, 11)] + ["A", "J", "Q", "K"]
# number = [i for i in range(2,11)]
# number.extend(["A","J","Q","K"])
result = [(c,n) for c in card_type for n in number]
print(result)
# draw = random.choice(result)
# print(draw)
#
# draw2 = random.sample(result,5)
# print(draw2)