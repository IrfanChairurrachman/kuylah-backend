# importing pandas as pd
import pandas as pd
  
# Read the csv file and construct the dataframe
df = pd.read_csv('raw_data.csv')

# drop row yang ada NaN di kolom ini
df = df.dropna(subset=['description', 'type', 'latitude', 'longitude'])

# buat index baru
df = df.reset_index()
# hapus index no
df = df.drop('no', 1)
# export ke dataset.csv
df.to_csv('dataset.csv', index=False)

