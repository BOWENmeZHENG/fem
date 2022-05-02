import matplotlib.pyplot as plt


def plot_parts(parts):
    plt.figure(figsize=(8, 8))
    for part in parts:
        plt.plot(part[:, 0], part[:, 1])
    plt.show()
