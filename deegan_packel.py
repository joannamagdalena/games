# http://dx.doi.org/10.15807/jorsj.43.71

import numpy as np

def player_set_partition(player_set):
    partition = []
    for p in range(0, len(player_set)):
        exists_set = False
        for s in partition:
            if player_set[p] == player_set[s[0]]:
                s.append(p)
                exists_set = True

        if not exists_set:
            partition.append([p])
    print(partition)


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
#deegan_packel_indices(g)
#player_set_partition(g[0])