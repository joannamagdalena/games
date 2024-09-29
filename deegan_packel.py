# http://dx.doi.org/10.15807/jorsj.43.71

import numpy as np

# partition of player set by players' weights, reversed sorted by weights
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

    weights = sorted(set(player_set), reverse=True)
    sorted_partition = []
    for w in weights:
        for s in partition:
            if player_set[s[0]] == w:
                sorted_partition.append(s)
                break

    return sorted_partition


def deegan_packel_indices(game, player):
    player_weights = game[0]  # players' weights
    number_of_players = len(player_weights)  # number of players
    quota = game[1]  # quota
    weight_of_N = sum(player_weights)  # weight of the great coalition

    partition_of_player_set = player_set_partition(player_weights)

    c = np.zeros([quota, number_of_players])
    c[0, 0] = 1
    t_star = 0

    numerator_of_index = 0
    min_winning_coalitions = 0
    alpha = np.zeros(number_of_players)

    for x in partition_of_player_set:
        if player_weights[x[0]] == player_weights[player - 1]:
            y_prime = len(x) - 1
        else:
            y_prime = len(x)

        for t in reversed(range(0, t_star+1)):
            for w in reversed(range(0, int(alpha[t]) + 1)):
                if c[w, t] > 0:
                    c_prime = 1
                    for y in range(1, y_prime + 1):
                        c_prime = c_prime * (y_prime - y + 1) / y

                        if w + (player_weights[x[0]] * y) <= quota - 1:
                            c[w + (player_weights[x[0]] * y), t + y] += c[w, t] * c_prime
                            alpha[t + y] = max(int(alpha[t + y]), w + (player_weights[x[0]] * y))

                        if quota - player_weights[player - 1] <= w + (player_weights[x[0]] * y) and w + (player_weights[x[0]] * y) <= min(quota - 1, quota - 1 - player_weights[player - 1] + player_weights[x[0]]):
                            numerator_of_index += (c[w, t] * c_prime) / (t + y + 1)

        t_star += y_prime
    dpi = numerator_of_index #/ min_winning_coalitions
    print(dpi)


g = [[1,2,2,2,4],8]
deegan_packel_indices(g, 5)
