# http://dx.doi.org/10.15807/jorsj.43.71

import numpy as np

def deegan_packel_indices(game):
    player_weights = game[0]  # players' weights
    number_of_players = len(player_weights)  # number of players
    quota = game[1]  # quota
    weight_of_N = sum(player_weights)  # weight of the great coalition

    c = np.zeros([quota, number_of_players])
    c[0, 0] = 1

    numerator_of_index = 0
    alpha = np.zeros(number_of_players)



g = [[1,2,2,2,4],8]
deegan_packel_indices(g)