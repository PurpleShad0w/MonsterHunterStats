import os
import sys
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(os.path.dirname(sys.argv[0]))

df = pd.read_csv('SAVEDATA1000.csv')
df.drop(['Start','Size','Color','Comment'], axis=1, inplace=True)
df.set_index('Name', inplace=True)

df2 = pd.DataFrame(data={'Item ID':0,'Item Name':0,'Total Quantity':0,'Quantity in box':0,'Quantity on hunter':0},index=(0,1))

# print(df.filter(like='rank',axis=0))
# print(df.loc['u32 hunter_rank']['Value'].iloc[0])
# print(df.loc['u32 master_rank']['Value'].iloc[0])

index_pouch = df.index.get_loc('struct mhw_item_pouch item_pouch')
# df_item_pouch = df.iloc[index_pouch:index_pouch+74] # item pouch without ammo
df_item_pouch = df.iloc[index_pouch:index_pouch+123]
df_item_pouch.reset_index(inplace=True)

for i in range(0,123):
    if 'id' in df_item_pouch.iloc[i,0]:
        id = df_item_pouch.iloc[i,1]
    if 'amount' in df_item_pouch.iloc[i,0]:
        amount = df_item_pouch.iloc[i,1]
        s = {'Item ID':id,'Item Name':0,'Total Quantity':0,'Quantity in box':0,'Quantity on hunter':amount}
        df2 = df2.append(s,ignore_index=True)

index_box = df.index.get_loc('struct mhw_storage storage')
df_item_box = df.iloc[index_box:index_box+6455]
df_item_box.reset_index(inplace=True)

for i in range(0,6455):
    if 'id' in df_item_box.iloc[i,0]:
        id = df_item_box.iloc[i,1]
    if 'amount' in df_item_box.iloc[i,0]:
        amount = df_item_box.iloc[i,1]
        s = {'Item ID':id,'Item Name':0,'Total Quantity':0,'Quantity in box':amount,'Quantity on hunter':0}
        df2 = df2.append(s,ignore_index=True)

df2 = df2.loc[(df2!=0).any(axis=1)]
df2.to_csv(r'output.csv',index=False)