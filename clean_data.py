# The purpose of this code is to see if the chinese text can be viewed in the csv file

import pandas as pd

df = pd.read_csv('Dataset/books.csv')

# create a boolean mask that indicates which values are missing
mask = df['authors'].isna()

# fill the missing values with an empty string
df['authors'] = df['authors'].fillna('')

# create a boolean mask that indicates which values contain 'J.K.'
mask_jk = df['authors'].str.contains('J.K.')

# filter the DataFrame using the boolean masks
df_filtered = df[mask_jk & ~mask]

print(df_filtered[['title', 'authors']])