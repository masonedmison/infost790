import matplotlib.pyplot as plt

cmap = plt.cm.get_cmap('viridis')

rgba = cmap(.001, bytes=True)
print(rgba)

print('#{:02x}{:02x}{:02x}'.format(*rgba))