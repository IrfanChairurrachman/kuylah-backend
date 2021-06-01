# importing pandas as pd
import pandas as pd
  
# Read the csv file and construct the dataframe
df = pd.read_csv('inventory/raw_data.csv')

# drop row yang ada NaN di kolom ini
df = df.dropna(subset=['description', 'type', 'latitude', 'longitude'])

# buat index baru
df = df.reset_index()
df['index'] = range(0, len(df))
# hapus index no
df = df.drop('no', 1)
# export ke dataset.csv
df.to_csv('inventory/dataset.csv', index=False)

