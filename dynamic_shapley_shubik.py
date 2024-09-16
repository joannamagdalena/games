#https://doi.org/10.3390/g13010006
import numpy as np
import math

# winning coalitions per cardinality
def count_winning_coalitions(number_of_players,player_weights,weight_of_N,quota):
    C = np.zeros((weight_of_N-quota+1, number_of_players+1))
    if weight_of_N >= quota:
        C[weight_of_N-quota, number_of_players] = 1

    for i in range(1, number_of_players+1):
        if quota+player_weights[i-1] <= weight_of_N:
            for x in range(player_weights[i-1], weight_of_N-quota+1):
                for s in range(2, number_of_players+1):
                    C[x-player_weights[i-1], s-1] = C[x, s] + C[x-player_weights[i-1], s-1]

    return C



# winning coalitions per cardinality and weight
def count_winning_coalitions_for_weight(number_of_players, player_weights, weight_of_N, quota, C):
    weights_unique = list(set(player_weights))
    Cw = {}
    for weight in weights_unique:
        D = np.zeros((weight_of_N - quota + 1, number_of_players + 1))
        D[:weight_of_N - quota + 1, :] = C[:weight_of_N - quota + 1, :]
        for x in reversed(range(0, weight_of_N - quota - weight + 1)):
            for s in range(1, number_of_players):
                D[x, s] = C[x, s] - D[x + weight, s + 1]
        Cw[weight] = D
    return Cw




# the Shapley--Shubik power indices for all players in a given game
def SSI(game):
    player_weights = game[0]  # players' weights
    number_of_players = len(player_weights)  # number of players
    quota = game[1]  # quota
    weight_of_N = sum(player_weights)  # weight of the great coalition
    C = count_winning_coalitions(number_of_players,player_weights,weight_of_N,quota)
    Cw = count_winning_coalitions_for_weight(number_of_players, player_weights, weight_of_N, quota, C)
    indices = []

    for i in range(1, number_of_players+1):
        D = Cw[player_weights[i-1]]
        ssi = 0
        for s in range(0, number_of_players):
            for x in range(0,player_weights[i-1]):
                ssi += (math.factorial(s) * math.factorial(number_of_players -s-1) * D[x, s+1]) / math.factorial(number_of_players)
        indices.append(ssi)
        D = np.zeros((weight_of_N-quota+1, number_of_players+1))

    return indices


