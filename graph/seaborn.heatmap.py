import numpy as np
import seaborn as sns

np.random.seed(0)

flights = sns.load_dataset("flights")
flights = flights.pivot("month", "year", "passengers")

# Documentation: https://seaborn.pydata.org/generated/seaborn.heatmap.html

# Annotate each cell with the numeric value using integer formatting: annot - fmt
# Use a different colormap: cmap
# Add lines between each cell: linewidth
ax = sns.heatmap(flights, annot=True, fmt="d", cmap="YlGnBu", linewidths=.5)
