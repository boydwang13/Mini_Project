# Preparations
import os  # for path operations
import pandas as pd     # for data processing
import matplotlib.pyplot as plt     # for plotting

script_dir = os.getcwd() # Get the current working directory
data_path=os.path.join(script_dir, "..", "data", "processed", "hotel_vienna_munged.csv") # Define the path to the processed data file
output_path=os.path.join(script_dir, "..", "output", "Scatter_Prices_VS_Distance.png")  # Define the path to save the output plot

df=pd.read_csv(data_path)   # Read the processed data into a DataFrame

# preparing data for scatter plot
x = df['distance']  
y = df['price'] 

# creating scatter plot
plt.scatter(x, y)

# adding title and labels
plt.title("Scatter Plot of Hotel Prices vs. Distance to City Center")
plt.xlabel("Distance to City Center (km)")
plt.ylabel("Price (EUR)")

# saving the plot to a file
plt.savefig(output_path, dpi=300, bbox_inches="tight")

plt.show()