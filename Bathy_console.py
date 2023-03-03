import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np
from scipy.interpolate import griddata
from scipy.ndimage.filters import uniform_filter
import matplotlib.pyplot as plt

# Create the main window
root = tk.Tk()
root.title('Bathymetric Data')


# Define the function to load the data and plot the grid
def plot_grid():
    # Open a file dialog to select the data file
    file_path = filedialog.askopenfilename()

    # Load the data into a pandas DataFrame
    data = pd.read_csv(file_path)
    x = data['x']
    y = data['y']
    z = data['z']

    # Convert the data to a grid format using linear interpolation
    xi = np.linspace(min(x), max(x), 100)
    yi = np.linspace(min(y), max(y), 100)
    zi = griddata((x, y), z, (xi[None, :], yi[:, None]), method='linear')

    # Smooth out the grid using a uniform filter
    zi_smooth = uniform_filter(zi, size=3)

    # Plot the grid using a filled contour plot
    plt.contourf(xi, yi, zi_smooth, cmap='coolwarm')
    plt.colorbar()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Bathymetric Data')
    plt.show()


# Create a button to plot the grid
plot_button = tk.Button(root, text='Plot Grid', command=plot_grid)
plot_button.pack()

# Run the main loop
root.mainloop()