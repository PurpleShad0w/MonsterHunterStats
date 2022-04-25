import os
import sys
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(os.path.dirname(sys.argv[0]))

# Load the data
df = pd.read_csv('mhr_slot.csv')
df.set_index('Name', inplace=True)

# Create dataframes
df2 = pd.DataFrame(data={'Item ID':0,'Item Name':0,'Quantity':0,'Item Type':0},index=(0,1))
df3 = pd.DataFrame(data={'Weapon Index':0,'Weapon Name':0,'Weapon Level':0,'Weapon Type':0},index=(0,1))
df4 = pd.DataFrame(data={'Armor Index':0,'Armor Name':0,'Armor Level':0},index=(0,1))
df5 = pd.DataFrame(data={'Talisman ID':0,'Talisman Name':0,'Skill I':0,'Skill II':0},index=(0,1))

# Locate items, weapons, armor and talismans
index_item = df.index.get_loc('struct item i[1999]')
df_item = df.iloc[index_item:index_item+5998]
df_weapons = df.iloc[index_item+5999:index_item+10199]
df_armor = df.iloc[index_item+10200:index_item+19800]
df_talisman = df.iloc[index_item+19800:index_item+22801]
df_item.reset_index(inplace=True)
df_weapons.reset_index(inplace=True)
df_armor.reset_index(inplace=True)
df_talisman.reset_index(inplace=True)

# Gather items
for i in range(0,5998):
        if 'Item ID' in df_item.iloc[i,0]:
            id = df_item.iloc[i,1]
        if 'Amount' in df_item.iloc[i,0]:
            amount = df_item.iloc[i,1]
            s = {'Item ID':id,'Item Name':0,'Quantity':amount,'Item Type':0}
            df2 = df2.append(s,ignore_index=True)

# Gather weapons
for i in range(0,4200):
        if 'Weapon Type' in df_weapons.iloc[i,0]:
            type = df_weapons.iloc[i,1]
        if 'Weapon index' in df_weapons.iloc[i,0]:
            index = df_weapons.iloc[i,1]
        if 'Weapon Level' in df_weapons.iloc[i,0]:
            level = df_weapons.iloc[i,1]
            s = {'Weapon Index':index,'Weapon Name':0,'Weapon Level':level,'Weapon Type':type}
            df3 = df3.append(s,ignore_index=True)

# Gather armor
for i in range(0,9600):
        if 'Armor Index' in df_armor.iloc[i,0]:
            index = df_armor.iloc[i,1]
        if 'Armor Level' in df_armor.iloc[i,0]:
            level = df_armor.iloc[i,1]
            s = {'Armor Index':index,'Armor Name':0,'Armor Level':level}
            df4 = df4.append(s,ignore_index=True)

# Gather talismans
for i in range(0,3001):
        if 'Talisman Base ID' in df_talisman.iloc[i,0]:
            id = df_talisman.iloc[i,1]
        if 'Skill ID 1' in df_talisman.iloc[i,0]:
            skill_1 = df_talisman.iloc[i,1]
        if 'Skill ID 2' in df_talisman.iloc[i,0]:
            skill_2 = df_talisman.iloc[i,1]
            s = {'Talisman ID':id,'Talisman Name':0,'Skill I':skill_1,'Skill II':skill_2}
            df5 = df5.append(s,ignore_index=True)

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
df3 = df3.groupby(df3['Weapon Index'],sort=False).aggregate({'Weapon Name':'last','Weapon Level':'first','Weapon Type':'first'})
df4 = df4.groupby(df4['Armor Index'],sort=False).aggregate({'Armor Name':'last','Armor Level':'first'})
df5 = df5.groupby(df5['Talisman ID'],sort=False).aggregate({'Talisman Name':'last','Skill I':'first','Skill II':'first'})

# Outputting dataframes
df2.to_csv(r'stories_2_output_items.csv',encoding='utf-8')
df3.to_csv(r'stories_2_output_weapons.csv',encoding='utf-8')
df4.to_csv(r'stories_2_output_armor.csv',encoding='utf-8')
df5.to_csv(r'stories_2_output_talismans.csv',encoding='utf-8')