import os
import sys
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(os.path.dirname(sys.argv[0]))

df = pd.read_csv('SAVEDATA1000.csv')
df.drop(['Start','Size','Color','Comment'], axis=1, inplace=True)
df.set_index('Name', inplace=True)

df2 = pd.DataFrame(data={'Item ID':0,'Item Name':0,'Total Quantity':0,'Quantity in box':0,'Quantity on hunter':0,'Item Type':0},index=(0,1))

# print(df.filter(like='rank',axis=0))
# print(df.loc['u32 hunter_rank']['Value'].iloc[0])
# print(df.loc['u32 master_rank']['Value'].iloc[0])

index_pouch = df.index.get_loc('struct mhw_item_pouch item_pouch')
df_item_pouch_items = df.iloc[index_pouch:index_pouch+74]
df_item_pouch_ammo = df.iloc[index_pouch+75:index_pouch+123]
df_item_pouch_items.reset_index(inplace=True)
df_item_pouch_ammo.reset_index(inplace=True)

for i in range(0,74):
    if 'id' in df_item_pouch_items.iloc[i,0]:
        id = df_item_pouch_items.iloc[i,1]
    if 'amount' in df_item_pouch_items.iloc[i,0]:
        amount = df_item_pouch_items.iloc[i,1]
        s = {'Item ID':id,'Item Name':0,'Total Quantity':0,'Quantity in box':0,'Quantity on hunter':amount,'Item Type':'Support'}
        df2 = df2.append(s,ignore_index=True)

for i in range(0,48):
    if 'id' in df_item_pouch_ammo.iloc[i,0]:
        id = df_item_pouch_ammo.iloc[i,1]
    if 'amount' in df_item_pouch_ammo.iloc[i,0]:
        amount = df_item_pouch_ammo.iloc[i,1]
        s = {'Item ID':id,'Item Name':0,'Total Quantity':0,'Quantity in box':0,'Quantity on hunter':amount,'Item Type':'Ammo'}
        df2 = df2.append(s,ignore_index=True)

index_box = df.index.get_loc('struct mhw_storage storage')
df_item_box_items = df.iloc[index_box:index_box+602]
df_item_box_ammo = df.iloc[index_box+603:index_box+1203]
df_item_box_materials = df.iloc[index_box+1204:index_box+4954]
df_item_box_decorations = df.iloc[index_box+4955:index_box+6455]
df_item_box_items.reset_index(inplace=True)
df_item_box_ammo.reset_index(inplace=True)
df_item_box_materials.reset_index(inplace=True)
df_item_box_decorations.reset_index(inplace=True)

for i in range(0,602):
    if 'id' in df_item_box_items.iloc[i,0]:
        id = df_item_box_items.iloc[i,1]
    if 'amount' in df_item_box_items.iloc[i,0]:
        amount = df_item_box_items.iloc[i,1]
        s = {'Item ID':id,'Item Name':0,'Total Quantity':0,'Quantity in box':amount,'Quantity on hunter':0,'Item Type':'Support'}
        df2 = df2.append(s,ignore_index=True)

for i in range(0,600):
    if 'id' in df_item_box_ammo.iloc[i,0]:
        id = df_item_box_ammo.iloc[i,1]
    if 'amount' in df_item_box_ammo.iloc[i,0]:
        amount = df_item_box_ammo.iloc[i,1]
        s = {'Item ID':id,'Item Name':0,'Total Quantity':0,'Quantity in box':amount,'Quantity on hunter':0,'Item Type':'Ammo'}
        df2 = df2.append(s,ignore_index=True)

for i in range(0,3750):
    if 'id' in df_item_box_materials.iloc[i,0]:
        id = df_item_box_materials.iloc[i,1]
    if 'amount' in df_item_box_materials.iloc[i,0]:
        amount = df_item_box_materials.iloc[i,1]
        s = {'Item ID':id,'Item Name':0,'Total Quantity':0,'Quantity in box':amount,'Quantity on hunter':0,'Item Type':'Materials'}
        df2 = df2.append(s,ignore_index=True)

for i in range(0,1500):
    if 'id' in df_item_box_decorations.iloc[i,0]:
        id = df_item_box_decorations.iloc[i,1]
    if 'amount' in df_item_box_decorations.iloc[i,0]:
        amount = df_item_box_decorations.iloc[i,1]
        s = {'Item ID':id,'Item Name':0,'Total Quantity':0,'Quantity in box':amount,'Quantity on hunter':0,'Item Type':'Decorations'}
        df2 = df2.append(s,ignore_index=True)


df2 = df2[df2['Item ID'] != 0]
df2['Total Quantity'] = df2['Quantity in box'] + df2['Quantity on hunter']

df_dict = pd.read_csv('item_dict.csv')
df_dict.set_index('Item ID', inplace=True)

for i in range(len(df2)):
    id = df2.iloc[i,0]
    if df_dict.index.__contains__(id):
        s = {'Item ID':id,'Item Name':df_dict.loc[id,'Item Name'],'Total Quantity':0,'Quantity in box':0,'Quantity on hunter':0,'Item Type':0}
        df2 = df2.append(s,ignore_index=True)

# Add sort=False to line below to sort by Game Order
df2 = df2.groupby(df2['Item ID'],sort=False).aggregate({'Item Name':'last','Total Quantity':'sum','Quantity in box':'sum','Quantity on hunter':'sum','Item Type':'first'})
df2.to_csv(r'output.csv')