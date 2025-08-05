import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import pearsonr


class GaussianPopulation:
    def __init__(self, mean:float, std:float):
        self.mean = mean
        self.std = std

def generate_pearson_data(n_samples:int,
                          pop_noise: GaussianPopulation,
                          a:float):
    x = np.linspace(-100, 100, n_samples)
    noise = np.random.normal(loc=pop_noise.mean, scale=pop_noise.std, size=n_samples)
    y = a * x + noise

    return x, y


def plot_scatter_with_fit(x, y, save_path = None):

    r, _ = pearsonr(x, y)
    r_squared = r ** 2

    plt.figure(figsize=(8, 5))

    plt.scatter(x, y, color='blue', label='Data points')

    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m * x + b, color='red', label=f'Fit line: y = {m:.2f}x + {b:.2f}')

    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.legend()
    plt.grid(True)
    plt.title(f'Pearson={r:.2f} | $r^2={r_squared:.2f}$')
    plt.tight_layout()

    if save_path is not None:
        plt.savefig(save_path)
        plt.close()
    else:
        plt.show()

    return r, r_squared


if __name__ == "__main__":
    n = 1000
    noises = [2, 10, 50, 100, 500]
    factors = [-5, -1, 0, 1, 5]

    r_2_list = []
    for noise_range in noises:
        noise_r2_list = []
        for relation_factor in factors:

            noise = GaussianPopulation(0, noise_range)
            x,y = generate_pearson_data(n ,noise, 1)
            r, r_2 = plot_scatter_with_fit(x, y, f'noise{noise_range}_factor{relation_factor}.png')

            noise_r2_list.append(r_2)

            print(f'Noise {noise_range}, Factor {relation_factor}: Pearson={r:.2f} | r^2={r_2:.2f}')

        r_2_list.append(np.mean(noise_r2_list))


    plt.figure(figsize = (8,5))

    plt.plot(noises, r_2_list, '-o')
    plt.xlabel('Noise level')
    plt.ylabel('$r^2$')
    plt.grid()

    plt.savefig('noise_r2.png')
    plt.close()


