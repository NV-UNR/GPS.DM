import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

# Print the current working directory
print("Current working directory:", os.getcwd())

# Function to read points from the file
def read_points_from_file(filename):
    points = []
    first_values = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            first_value = int(parts[0])
            x, y, z = float(parts[-3]), float(parts[-2]), float(parts[-1])
            points.append([first_value, x, y, z])
            first_values.append(first_value)
    return points, list(set(first_values))

# Function to generate a unique color for each first value
def generate_colors(num_colors):
    return plt.cm.get_cmap('hsv', num_colors)

# Reading points from the file "chi1k17570.out"
filename = "chi1k17570.out"
points, unique_first_values = read_points_from_file(filename)

# Create a color map
cmap = generate_colors(len(unique_first_values))
color_map = {value: cmap(i) for i, value in enumerate(unique_first_values)}

# Extracting x, y, and z coordinates
x = [point[1] for point in points]
y = [point[2] for point in points]
z = [point[3] for point in points]
colors = [color_map[point[0]] for point in points]

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points with corresponding colors
scatter = ax.scatter(x, y, z, c=colors, marker='o')

# Plotting the sphere
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x_sphere = np.outer(np.cos(u), np.sin(v))
y_sphere = np.outer(np.sin(u), np.sin(v))
z_sphere = np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x_sphere, y_sphere, z_sphere, color='b', alpha=0.2)

# Toggle legend (comment out this block to hide the legend)
if False:  # Set to False to hide legend
    legend_entries = []
    for value in unique_first_values:
        legend_entries.append(plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color_map[value], markersize=10, label=str(value)))
    ax.legend(handles=legend_entries, title="First Values")

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
