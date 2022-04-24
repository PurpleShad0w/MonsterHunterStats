import os
import sys
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(os.path.dirname(sys.argv[0]))

# Load the data
df = pd.read_csv('mhr_slot.csv')
df.set_index('Name', inplace=True)

# Create items dataframe
df2 = pd.DataFrame(data={'Item ID':0,'Item Name':0,'Quantity':0,'Item Type':0},index=(0,1))

# Locate items
index_item = df.index.get_loc('struct item i[1999]')
df_item = df.iloc[index_item:index_item+5998]
df_item.reset_index(inplace=True)

# Gather items
for i in range(0,5998):
        if 'Item ID' in df_item.iloc[i,0]:
            id = df_item.iloc[i,1]
        if 'Amount' in df_item.iloc[i,0]:
            amount = df_item.iloc[i,1]
            s = {'Item ID':id,'Item Name':0,'Quantity':amount,'Item Type':0}
            df2 = df2.append(s,ignore_index=True)

# Cleaning dataframes
df2 = df2[df2['Item ID'] != 0]

# Adding dictionaries
df_dict_items = pd.read_csv('res/dict/stories_2_dictionary_items.csv')
df_dict_items.set_index('Item ID', inplace=True)

# Adding item information
for i in range(len(df2)):
    id = df2.iloc[i,0]
    try:
        s = {'Item ID':id,'Item Name':df_dict_items.loc[int(float(id)),'Item Name'],'Quantity':0,'Item Type':df_dict_items.loc[int(float(id)),'Category']}
        df2 = df2.append(s,ignore_index=True)
    except KeyError:
        continue

# Cleaning
df2 = df2.groupby(df2['Item ID'],sort=False).aggregate({'Item Name':'last','Quantity':'first','Item Type':'last'})

# Outputting dataframes
df2.to_csv(r'stories_2_output_items.csv',encoding='utf-8')
