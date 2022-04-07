import os
import sys
from numpy import sort
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(os.path.dirname(sys.argv[0]))

# Load save data
df = pd.read_csv('SAVEDATA1000.csv')
df.drop(['Start','Size','Color','Comment'], axis=1, inplace=True)
df.set_index('Name', inplace=True)
# print(df.filter(like='rank',axis=0))
# print(df.loc['u32 hunter_rank']['Value'].iloc[0])
# print(df.loc['u32 master_rank']['Value'].iloc[0])
# Create items dataframe
df2 = pd.DataFrame(data={'Item ID':0,'Item Name':0,'Total Quantity':0,'Quantity in box':0,'Quantity on hunter':0,'Item Type':0},index=(0,1))
# Find item pouch items and ammo
index_pouch = df.index.get_loc('struct mhw_item_pouch item_pouch')
df_item_pouch_items = df.iloc[index_pouch:index_pouch+74]
df_item_pouch_ammo = df.iloc[index_pouch+75:index_pouch+123]
df_item_pouch_items.reset_index(inplace=True)
df_item_pouch_ammo.reset_index(inplace=True)
# Gather item pouch items
for i in range(0,74):
    if 'id' in df_item_pouch_items.iloc[i,0]:
        id = df_item_pouch_items.iloc[i,1]
    if 'amount' in df_item_pouch_items.iloc[i,0]:
        amount = df_item_pouch_items.iloc[i,1]
        s = {'Item ID':id,'Item Name':0,'Total Quantity':0,'Quantity in box':0,'Quantity on hunter':amount,'Item Type':'Support'}
        df2 = df2.append(s,ignore_index=True)
# Gather item pouch ammo
for i in range(0,48):
    if 'id' in df_item_pouch_ammo.iloc[i,0]:
        id = df_item_pouch_ammo.iloc[i,1]
    if 'amount' in df_item_pouch_ammo.iloc[i,0]:
        amount = df_item_pouch_ammo.iloc[i,1]
        s = {'Item ID':id,'Item Name':0,'Total Quantity':0,'Quantity in box':0,'Quantity on hunter':amount,'Item Type':'Ammo'}
        df2 = df2.append(s,ignore_index=True)
# Find item box items, ammo, materials and decorations
index_box = df.index.get_loc('struct mhw_storage storage')
df_item_box_items = df.iloc[index_box:index_box+602]
df_item_box_ammo = df.iloc[index_box+603:index_box+1203]
df_item_box_materials = df.iloc[index_box+1204:index_box+4954]
df_item_box_decorations = df.iloc[index_box+4955:index_box+6455]
df_item_box_items.reset_index(inplace=True)
df_item_box_ammo.reset_index(inplace=True)
df_item_box_materials.reset_index(inplace=True)
df_item_box_decorations.reset_index(inplace=True)
# Gather item box items
for i in range(0,602):
    if 'id' in df_item_box_items.iloc[i,0]:
        id = df_item_box_items.iloc[i,1]
    if 'amount' in df_item_box_items.iloc[i,0]:
        amount = df_item_box_items.iloc[i,1]
        s = {'Item ID':id,'Item Name':0,'Total Quantity':0,'Quantity in box':amount,'Quantity on hunter':0,'Item Type':'Support'}
        df2 = df2.append(s,ignore_index=True)
# Gather item box ammo
for i in range(0,600):
    if 'id' in df_item_box_ammo.iloc[i,0]:
        id = df_item_box_ammo.iloc[i,1]
    if 'amount' in df_item_box_ammo.iloc[i,0]:
        amount = df_item_box_ammo.iloc[i,1]
        s = {'Item ID':id,'Item Name':0,'Total Quantity':0,'Quantity in box':amount,'Quantity on hunter':0,'Item Type':'Ammo'}
        df2 = df2.append(s,ignore_index=True)
# Gather item box materials
for i in range(0,3750):
    if 'id' in df_item_box_materials.iloc[i,0]:
        id = df_item_box_materials.iloc[i,1]
    if 'amount' in df_item_box_materials.iloc[i,0]:
        amount = df_item_box_materials.iloc[i,1]
        s = {'Item ID':id,'Item Name':0,'Total Quantity':0,'Quantity in box':amount,'Quantity on hunter':0,'Item Type':'Materials'}
        df2 = df2.append(s,ignore_index=True)
# Gather item box decorations
for i in range(0,1500):
    if 'id' in df_item_box_decorations.iloc[i,0]:
        id = df_item_box_decorations.iloc[i,1]
    if 'amount' in df_item_box_decorations.iloc[i,0]:
        amount = df_item_box_decorations.iloc[i,1]
        s = {'Item ID':id,'Item Name':0,'Total Quantity':0,'Quantity in box':amount,'Quantity on hunter':0,'Item Type':'Decorations'}
        df2 = df2.append(s,ignore_index=True)
# Create equipment dataframe
df3 = pd.DataFrame(data={'Type':0,'ID':0,'Name':0,'Level':0,'Points':0},index=(0,1))
# Find equipment, palico equipment, palico tools, tools and pendants
df_equipment = df.iloc[index_box+6455:index_box+171456]
df_palico_equipment = df.iloc[index_box+205118:index_box+287618]
df_equipment.reset_index(inplace=True)
df_palico_equipment.reset_index(inplace=True)
index_palico = df.index.get_loc('str64 palico_name[64]')
df_palico_tool = df.iloc[index_palico+66:index_palico+72]
index_tool = df.index.get_loc('struct mhw_equipment tools[128]')
df_tool = df.iloc[index_tool:index_tool+8449]
df_tool.reset_index(inplace=True)
df_pendants = df.iloc[index_tool+8449:index_tool+8515]
# Gather equipment
for i in range(0,165001):
    if 'type' in df_equipment.iloc[i,0]:
        type = df_equipment.iloc[i,1]
    if 'id' in df_equipment.iloc[i,0]:
        id = df_equipment.iloc[i,1]
    if 'level' in df_equipment.iloc[i,0]:
        level = df_equipment.iloc[i,1]+1
    if 'points' in df_equipment.iloc[i,0]:
        points = df_equipment.iloc[i,1]
        s = {'Type':type,'ID':id,'Name':0,'Level':level,'Points':points}
        df3 = df3.append(s,ignore_index=True)
# Gather palico equipment
for i in range(0,82500):
    if 'type' in df_palico_equipment.iloc[i,0]:
        type = df_palico_equipment.iloc[i,1]
    if 'id' in df_palico_equipment.iloc[i,0]:
        id = df_palico_equipment.iloc[i,1]
    if 'level' in df_palico_equipment.iloc[i,0]:
        level = df_palico_equipment.iloc[i,1]
    if 'points' in df_palico_equipment.iloc[i,0]:
        points = df_palico_equipment.iloc[i,1]
        s = {'Type':type,'ID':id,'Name':0,'Level':level,'Points':points}
        df3 = df3.append(s,ignore_index=True)
# Create palico dataframe
df4 = pd.DataFrame(data={'Tool':0,'Experience':0},index=(0,1))
# Gather palico tool
df4 = df4.append({'Tool':'Vigorwasp Spray','Experience':df_palico_tool.iloc[0,0]},ignore_index=True)
df4 = df4.append({'Tool':'Flashfly Cage','Experience':df_palico_tool.iloc[1,0]},ignore_index=True)
df4 = df4.append({'Tool':'Shieldspire','Experience':df_palico_tool.iloc[2,0]},ignore_index=True)
df4 = df4.append({'Tool':'Coral Orchestra','Experience':df_palico_tool.iloc[3,0]},ignore_index=True)
df4 = df4.append({'Tool':'Plunderblade','Experience':df_palico_tool.iloc[4,0]},ignore_index=True)
df4 = df4.append({'Tool':'Meowlotov Cocktail','Experience':df_palico_tool.iloc[5,0]},ignore_index=True)
# Gather tools
for i in range(0,8449):
    if 'type' in df_tool.iloc[i,0]:
        type = df_tool.iloc[i,1]
    if 'id' in df_tool.iloc[i,0]:
        id = df_tool.iloc[i,1]
    if 'level' in df_tool.iloc[i,0]:
        level = df_tool.iloc[i,1]
    if 'points' in df_tool.iloc[i,0]:
        points = df_tool.iloc[i,1]
        s = {'Type':type,'ID':id,'Name':0,'Level':level,'Points':points}
        df3 = df3.append(s,ignore_index=True)
# Clean dataframes
df2 = df2[df2['Item ID'] != 0]
df3 = df3[(df3['ID'] != 0) | ((df3['Type'] != 0))]
# df3 = df3[df3['Type'].astype(float).astype(int) >= 0]
df4 = df4[df4['Tool'] != 0]
df2['Total Quantity'] = df2['Quantity in box'] + df2['Quantity on hunter']
# Define dictionaries
df_dict_items = pd.read_csv('dictionary_items.csv')
df_dict_items.set_index('Item ID', inplace=True)
df_dict_equipment = pd.read_csv('dictionary_equipment.csv')
df_type = df_dict_equipment.set_index('Type')
df_id = df_dict_equipment.set_index('ID')
# Add item information
for i in range(len(df2)):
    id = df2.iloc[i,0]
    if df_dict_items.index.__contains__(id):
        s = {'Item ID':id,'Item Name':df_dict_items.loc[id,'Item Name'],'Total Quantity':0,'Quantity in box':0,'Quantity on hunter':0,'Item Type':0}
        df2 = df2.append(s,ignore_index=True)
# Add equipment information
for i in range(len(df3)):
    type = df3.iloc[i,0]
    id = df3.iloc[i,1]
    if df_type.index.__contains__(type) and df_id.index.__contains__(id):
        df_temp = df_dict_equipment[df_dict_equipment['Type'] == type]
        df_temp.set_index('ID', inplace=True)
        s = {'Type':type,'ID':id,'Name':df_temp.loc[id,'Name'],'Level':0,'Points':0}
        df3 = df3.append(s,ignore_index=True)
# Rearranging dataframes
# Adding sort=False to groupby allows sorting by Game Order
df2 = df2.groupby(df2['Item ID'],sort=False).aggregate({'Item Name':'last','Total Quantity':'sum','Quantity in box':'sum','Quantity on hunter':'sum','Item Type':'first'})
df3 = df3.groupby([df3['Type'],df3['ID']],sort=False).aggregate({'Name':'last','Level':'first','Points':'first'})
df4 = df4.groupby(df4['Tool'],sort=False).aggregate({'Experience':'first'})
# Outputting dataframes
df2.to_csv(r'output_items.csv',encoding='utf-8')
df3.to_csv(r'output_equipment.csv',encoding='utf-8')
df4.to_csv(r'output_tool.csv',encoding='utf-8')