from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

points = [[1, 4], [5, 8], [7, 2], [9, 9], [6, 5], [3, 7], [8, 1], [4, 6], [2, 9], [5, 3],
          [10, 4], [7, 6], [3, 2], [6, 8], [9, 3],  [1,1], [2,5]]

colors = ["Red","Blue","Green","Yellow","Orange","Pink","Purple","Cyan","Magenta","Lime","Black",
          "Gray", "Brown", "Violet", "Indigo", "Turquoise", "Teal", "Gold", "Silver", 
          "Maroon", "Beige", "Olive"]

vor = Voronoi(points)

fig, ax = plt.subplots()

voronoi_plot_2d(vor, ax=ax, show_vertices=True, line_colors='black', line_width=2)

ax.set_xlim(0, 10)
ax.set_xticks([1,2,3,4,5,6,7,8,9,10])
ax.set_ylim(0, 10)
ax.set_yticks([1,2,3,4,5,6,7,8,9,10])
ax.set_aspect('equal')

ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")
ax.grid(False)

for region_idx, region in enumerate(vor.regions):
    if not -1 in region and len(region) > 0:
        polygon = [vor.vertices[i] for i in region]
        ax.fill(*zip(*polygon), color=colors[region_idx], alpha=0.3)

plt.show()