import matplotlib.pyplot as plt


def plot_parts(parts):
    plt.figure(figsize=(8, 8))
    for part in parts:
        plt.plot(part[:, 0], part[:, 1])
    plt.show()


def scatter_nodes(mesh_points):
    plt.figure(figsize=(8, 8))
    plt.scatter(mesh_points[:, 0], mesh_points[:, 1])
    plt.show()
