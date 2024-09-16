# https://doi.org/10.3390/g13010006

import numpy as np
import math


# number of winning coalitions per weight
def count_winning_coalitions(number_of_players, player_weights, weight_of_N, quota):
    T = np.zeros(weight_of_N - quota + 1)
    T[weight_of_N - quota] = 1
    for i in range(number_of_players + 1):
        if quota + player_weights[i-1] <= weight_of_N:
            for x in range(player_weights[i-1], weight_of_N - quota + 1):
                T[x - player_weights[i-1]] += T[x]
    return T


# number of winning coalitions containing a player
def count_winning_coalitions_with_player(number_of_players, player_weights, weight_of_N, quota, T):
    Tw = np.zeros((number_of_players, weight_of_N - quota + 1))
    for i in range(number_of_players + 1):
        for x in range(weight_of_N - player_weights[i-1] + 1, weight_of_N + 1):
            Tw[i - 1, x - quota] = T[x - quota]
        for x in reversed(range(quota, weight_of_N - player_weights[i-1] + 1)):
            Tw[i - 1, x - quota] = T[x - quota] - Tw[i - 1, x - quota + player_weights[i-1]]
    return Tw


# the probabilistic Penrose--Banzhaf power indices for all players in a given game
def probabilistic_PBI(game):
    player_weights = game[0]  # players' weights
    number_of_players = len(player_weights)  # number of players
    quota = game[1]  # quota
    weight_of_N = sum(player_weights)  # weight of the great coalition

    T = count_winning_coalitions(number_of_players, player_weights, weight_of_N, quota)
    Tw = count_winning_coalitions_with_player(number_of_players, player_weights, weight_of_N, quota, T)
    print(Tw)

    indices = []
    for i in range(1, number_of_players+1):
        pbi = 0
        for x in range(quota, quota + player_weights[i-1]):
            pbi += Tw[i-1, x - quota] / math.pow(2, number_of_players - 1)
        indices.append(pbi)

    return indices

