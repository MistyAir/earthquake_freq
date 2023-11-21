import pandas as pd

# Read in the data
df = pd.read_csv('data/earthquake.csv')

# Drop unnecessary columns
necessary_columns = ['time', 'latitude', 'longitude', 'depth', 'mag', 'magType']
df = df[necessary_columns]

# Save the data
df.to_csv('data/earthquake_clean.csv', index=False)
