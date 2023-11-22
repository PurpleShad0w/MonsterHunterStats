import os
import pandas as pd
import re
import subprocess
import sys
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
os.chdir(os.path.dirname(sys.argv[0]))


subprocess.call("C:/Program Files/010 Editor/010Editor.exe saves/mhr_slot.bin -template:templates/MHStories2_SaveTemplate.bt -script:scripts/MHS2.1sc -noui")

df = pd.read_csv('saves/mhr_slot.csv')
df.drop(['Start','Size','Color','Comment'], axis=1, inplace=True)
df.set_index('Name', inplace=True)

df2 = pd.DataFrame(data={'ID':0,'Name':0,'Quantity':0,'Category':0,'Subcategory':0},index=(0,1))
df3 = pd.DataFrame(data={'Index':0,'Type ID':0,'Name':0,'Level':0,'Quantity':0,'Type':0,'Subcategory':0},index=(0,1))
df4 = pd.DataFrame(data={'Index':0,'Name':0,'Level':0,'Quantity':0},index=(0,1))
df5 = pd.DataFrame(data={'ID':0,'Skill I ID':0,'Skill II ID':0,'Name':0,'Quantity':0,'Skill I':0,'Skill II':0,'Subcategory':0},index=(0,1))

index_item = df.index.get_loc('struct item i[1999]')
df_item = df.iloc[index_item:index_item+5998]
df_weapons = df.iloc[index_item+5998:index_item+17199]
df_armor = df.iloc[index_item+17199:index_item+26800]
df_talisman = df.iloc[index_item+26800:index_item+29801]
df_item.reset_index(inplace=True)
df_weapons.reset_index(inplace=True)
df_armor.reset_index(inplace=True)
df_talisman.reset_index(inplace=True)

for i in range(0,5998):
        if 'Item ID' in df_item.iloc[i,0]:
            id = df_item.iloc[i,1]
        if 'Amount' in df_item.iloc[i,0]:
            amount = df_item.iloc[i,1]
            s = {'ID':id,'Name':0,'Quantity':amount,'Category':0,'Subcategory':0}
            df2 = df2.append(s,ignore_index=True)

for i in range(0,4200):
        if 'Weapon Type' in df_weapons.iloc[i,0]:
            type = df_weapons.iloc[i,1]
            type_id = re.sub('[^0-9]','',type)
        if 'Weapon index' in df_weapons.iloc[i,0]:
            index = df_weapons.iloc[i,1]
        if 'Weapon Level' in df_weapons.iloc[i,0]:
            level = df_weapons.iloc[i,1]
            s = {'Index':index,'Type ID':type_id,'Name':0,'Level':level,'Quantity':1,'Type':type,'Subcategory':0}
            df3 = df3.append(s,ignore_index=True)

for i in range(0,9600):
        if 'Armor Index' in df_armor.iloc[i,0]:
            index = df_armor.iloc[i,1]
        if 'Armor Level' in df_armor.iloc[i,0]:
            level = df_armor.iloc[i,1]
            s = {'Index':index,'Name':0,'Level':level,'Quantity':1}
            df4 = df4.append(s,ignore_index=True)

for i in range(0,3001):
        if 'Talisman Base ID' in df_talisman.iloc[i,0]:
            id = df_talisman.iloc[i,1]
        if 'Skill ID 1' in df_talisman.iloc[i,0]:
            skill_1 = df_talisman.iloc[i,1]
            skill_1_id = re.sub('[^0-9]','',skill_1)
        if 'Skill ID 2' in df_talisman.iloc[i,0]:
            skill_2 = df_talisman.iloc[i,1]
            skill_2_id = re.sub('[^0-9]','',skill_2)
            s = {'ID':id,'Skill I ID':skill_1_id,'Skill II ID':skill_2_id,'Name':0,'Quantity':1,'Skill I':skill_1,'Skill II':skill_2,'Subcategory':0}
            df5 = df5.append(s,ignore_index=True)

df2 = df2[df2['ID'] != 0]

df_dict_items = pd.read_csv('dictionaries/MHS2_items.csv')
df_dict_items.set_index('ID', inplace=True)
df_dict_armor = pd.read_csv('dictionaries/MHS2_armor.csv')
df_dict_armor.set_index('Index', inplace=True)
df_dict_weapons = pd.read_csv('dictionaries/MHS2_weapons.csv')
df_dict_talismans = pd.read_csv('dictionaries/MHS2_talismans.csv')

for i in range(len(df2)):
    id = df2.iloc[i,0]
    try:
        s = {'ID':id,'Name':df_dict_items.loc[int(float(id)),'Name'],'Quantity':0,'Category':df_dict_items.loc[int(float(id)),'Category'],'Subcategory':df_dict_items.loc[int(float(id)),'Subcategory']}
        df2 = df2.append(s,ignore_index=True)
    except KeyError:
        continue

for i in range(len(df3)):
        index = df3.iloc[i,0]
        type_id = df3.iloc[i,1]
        df_temp = df_dict_weapons[(df_dict_weapons['Index'] == int(float(index))) & (df_dict_weapons['Type ID'] == int(float(type_id)))]
        try:
            df_temp.reset_index(inplace=True)
            s = {'Index':index,'Type ID':type_id,'Name':df_temp.loc[0,'Name'],'Level':0,'Quantity':0,'Type':0,'Subcategory':df_temp.loc[0,'Subcategory']}
            df3 = df3.append(s,ignore_index=True)
        except KeyError:
            continue

for i in range(len(df4)):
    index = df4.iloc[i,0]
    try:
        s = {'Index':index,'Name':df_dict_armor.loc[int(float(index)),'Name'],'Level':0,'Quantity':0}
        df4 = df4.append(s,ignore_index=True)
    except KeyError:
        continue

for i in range(len(df5)):
        skill_1_id = df5.iloc[i,1]
        skill_2_id = df5.iloc[i,2]
        df_temp = df_dict_talismans[(df_dict_talismans['Skill I ID'] == int(float(skill_1_id))) & (df_dict_talismans['Skill II ID'] == int(float(skill_2_id)))]
        try:
            df_temp.reset_index(inplace=True)
            s = {'ID':0,'Skill I ID':skill_1_id,'Skill II ID':skill_2_id,'Name':df_temp.loc[0,'Name'],'Quantity':0,'Skill I':0,'Skill II':0,'Subcategory':df_temp.loc[0,'Subcategory']}
            df5 = df5.append(s,ignore_index=True)
        except KeyError:
            continue

df2 = df2.groupby(df2['ID'],sort=False).aggregate({'Name':'last','Quantity':'first','Category':'last','Subcategory':'last'})
df3 = df3.groupby([df3['Index'],df3['Type ID']],sort=False).aggregate({'Name':'last','Level':'first','Quantity':'sum','Type':'first','Subcategory':'last'})
df4 = df4.groupby(df4['Index'],sort=False).aggregate({'Name':'last','Level':'first','Quantity':'sum'})
df5 = df5.groupby([df5['Skill I ID'],df5['Skill II ID']],sort=False).aggregate({'ID':'first','Name':'last','Quantity':'sum','Skill I':'first','Skill II':'first','Subcategory':'last'})

df_items = df2
df_weapons = df3
df_armor = df4
df_talismans = df5
df_general = pd.DataFrame(data={'Name':0,'Quantity':0,'Level':0,'Category':0,'Subcategory':0},index=(0,1))

for i in range(len(df_items)):
    s = {'Name':df_items.iloc[i,1],'Quantity':df_items.iloc[i,2],'Level':0,'Category':df_items.iloc[i,3],'Subcategory':df_items.iloc[i,4]}
    df_general = df_general.append(s,ignore_index=True)

for i in range(len(df_weapons)):
    s = {'Name':df_weapons.iloc[i,2],'Quantity':df_weapons.iloc[i,4],'Level':df_weapons.iloc[i,3],'Category':'Weapons','Subcategory':df_weapons.iloc[i,6]}
    df_general = df_general.append(s,ignore_index=True)

for i in range(len(df_armor)):
    s = {'Name':df_armor.iloc[i,1],'Quantity':df_armor.iloc[i,3],'Level':df_armor.iloc[i,2],'Category':'Armor','Subcategory':'Armor'}
    df_general = df_general.append(s,ignore_index=True)

for i in range(len(df_talismans)):
    s = {'Name':df_talismans.iloc[i,3],'Quantity':df_talismans.iloc[i,4],'Level':0,'Category':'Talismans','Subcategory':df_talismans.iloc[i,7]}
    df_general = df_general.append(s,ignore_index=True)

df_general = df_general.groupby(df_general['Name']).aggregate({'Quantity':'sum','Level':'max','Category':'first','Subcategory':'first'})
df_general.to_csv(r'outputs/MHS2.csv',encoding='utf-8')