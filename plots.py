import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker

def time_avg_plot(time_data, game_size_coeff, avg_type):
    xpoints = np.arange(1, len(time_data)+1)*game_size_coeff
    ypoints = np.array(time_data)
    
    plt.plot(xpoints, ypoints)
    
    plt.title('Avg Time - ' + avg_type)
    plt.xlabel('game size')
    plt.ylabel('time avg')
    
    plt.xticks(xpoints)
    
    plt.show()
