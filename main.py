from dynamic_probabilistic_penrose_banzhaf import probabilistic_PBI
import random
import math
import timeit
from plots import time_avg_plot
import statistics

# generating weighted voting games
def games_generator(n, number_of_players, max_weight):
    games_list = []
    
    for i in range(1,n+1):
        weight_list = [random.randint(1, max_weight+1) for _ in range(number_of_players)]
        weights_sum = sum(weight_list)
        quota = random.randint(math.floor(weights_sum/2)+1, weights_sum)
        games_list.append([weight_list,quota])
    
    return games_list


def calculating_power_indices(n):
    time_information_mean = []
    time_information_median = []
    for i in range(1, n+1):
        games = games_generator(100, 5*i, 30)

        time_values = []
        PB_indices = [] 
        for game in games:
            start = timeit.default_timer()
            PB_indices.append(probabilistic_PBI(game))
            end = timeit.default_timer()
            time_values.append(end-start)
        
        time_information_mean.append(statistics.mean(time_values))
        time_information_median.append(statistics.median(time_values))
        
    time_avg_plot(time_information_mean, 5, 'Arithmetic Mean')
    time_avg_plot(time_information_median, 5, 'Median')
    

calculating_power_indices(5)
