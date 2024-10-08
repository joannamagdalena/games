# http://dx.doi.org/10.15807/jorsj.43.71

import numpy as np
import pandas as pd
import itertools

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


def enumerate_function(given_set, n_prime, b_prime, weights):
    min_sets = []
    new_sets = []
    if n_prime == len(weights) - 1:
        given_set.append(n_prime)
        min_sets.append(given_set)
        print(min_sets)
    else:
        a = weights[n_prime:]
        if a[0] >= b_prime:
            given_set.append(n_prime)
            min_sets.append(given_set)
            print(min_sets)
        if sum(a[1:]) >= b_prime:
            new_sets = enumerate_function(given_set, n_prime + 1, b_prime, weights)
            min_sets = min_sets + new_sets
            print(min_sets)
        if a[0] < b_prime:
            given_set.append(n_prime)
            new_sets = enumerate_function(given_set, n_prime + 1, b_prime - a[0], weights)
            min_sets = min_sets + new_sets
            print(min_sets)
    print(min_sets)
    min_sets.sort()
    return list(min_sets for min_sets,_ in itertools.groupby(min_sets))


def minimal_sets_counter(player_weights, threshold):
    sorted_weights = sorted(player_weights, reverse=True)
    print(enumerate_function([], 0, threshold, sorted_weights))


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
    #min_winning_coalitions = len(minimal_sets_counter(player_weights, quota))
    dpi = numerator_of_index #/ min_winning_coalitions
    #print(minimal_sets_counter(player_weights, quota))
    minimal_sets_counter(player_weights, quota)
    print(dpi)


g = [[20,6,5,2,1,1,1,1],26]
deegan_packel_indices(g, 1)
