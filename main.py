from dynamic_probabilistic_penrose_banzhaf import probabilistic_PBI
import random
import math

# generating a weighted voting game
weight_list = random.sample(range(1,21), 5)
weights_sum = sum(weight_list)
q = random.randint(math.floor(weights_sum/2)+1, weights_sum)
game = [weight_list,q]

print(game)
print(probabilistic_PBI(game))