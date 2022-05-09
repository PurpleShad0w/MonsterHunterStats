import os
import sys
import pandas as pd
import warnings
import re

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(os.path.dirname(sys.argv[0]))

# Load the data
df = pd.read_csv('saves/MH4U_user.csv')
df.set_index('Name', inplace=True)

# Create dataframes
df2 = pd.DataFrame(data={'ID':0,'Name':0,'Total Quantity':0,'Quantity in box':0,'Quantity on hunter':0,'Rarity':0},index=(0,1))

# Locate items
index_item_box = df.index.get_loc('struct item i[1400]')
df_item_box = df.iloc[index_item_box:index_item_box+4201]
df_item_box.reset_index(inplace=True)

# Gather item box items
for i in range(0,4201):
    if 'ID' in df_item_box.iloc[i,0]:
        id = df_item_box.iloc[i,1]
    if 'amount' in df_item_box.iloc[i,0]:
        amount = df_item_box.iloc[i,1]
        s = {'ID':id,'Name':0,'Total Quantity':0,'Quantity in box':int(amount),'Quantity on hunter':0,'Rarity':0}
        df2 = df2.append(s,ignore_index=True)

# Clean dataframes
df2['Total Quantity'] = df2['Quantity in box'] + df2['Quantity on hunter']

# Adding dictionaries
df_dict_items = pd.read_csv('dictionaries/MH4U_dictionary_items.csv')
df_dict_items.set_index('ID', inplace=True)

# Add item information
for i in range(len(df2)):
    id = df2.iloc[i,0]
    try:
        s = {'ID':id,'Name':df_dict_items.loc[int(float(id)),'Name'],'Total Quantity':0,'Quantity in box':0,'Quantity on hunter':0,'Rarity':df_dict_items.loc[int(float(id)),'Rarity']}
        df2 = df2.append(s,ignore_index=True)
    except KeyError:
        continue

# Cleaning
df2 = df2.groupby(df2['ID'],sort=False).aggregate({'Name':'last','Total Quantity':'sum','Quantity in box':'sum','Quantity on hunter':'sum','Rarity':'last'})

# Outputting dataframes
df2.to_csv(r'outputs/MH4U_output_items.csv',encoding='utf-8')