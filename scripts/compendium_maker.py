import os
import pandas as pd
import sys
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
os.chdir(os.path.dirname(sys.argv[0]))


df_world_items = pd.read_csv('dictionaries/MHWI_items.csv')
df_world_equipment = pd.read_csv('dictionaries/MHWI_equipment.csv')
df_world_palico = pd.read_csv('dictionaries/MHWI_palico.csv')
df_world_layered = pd.read_csv('dictionaries/MHWI_layered.csv')
df_stories_2_items = pd.read_csv('dictionaries/MHS2_items.csv')
df_stories_2_armor = pd.read_csv('dictionaries/MHS2_armor.csv')
df_stories_2_weapons = pd.read_csv('dictionaries/MHS2_weapons.csv')
df_stories_2_talismans = pd.read_csv('dictionaries/MHS2_talismans.csv')
df_3u_items = pd.read_csv('dictionaries/MH3U_items.csv')
df_3u_equipment = pd.read_csv('dictionaries/MH3U_equipment.csv')
df_4u_items = pd.read_csv('dictionaries/MH4U_items.csv')
df_4u_equipment = pd.read_csv('dictionaries/MH4U_equipment.csv')
df_4u_palico = pd.read_csv('dictionaries/MH4U_palico.csv')

df_general = pd.DataFrame(data={'Name':0,'In MH3U':0,'In MH4U':0,'In MHWI':0,'In MHS2':0},index=(0,1))

df_world_items = df_world_items[(df_world_items['Category'] != '(None)') & (df_world_items['Category'] != 'Furniture') & 
    (df_world_items['Category'] != 'Currencies') & (df_world_items['Category'] != 'Soundtrack')]
df_4u_items = df_4u_items[df_4u_items['Rarity'] != 0]

for i in range(len(df_world_items)):
    s = {'Name':df_world_items.iloc[i,1],'In MH3U':False,'In MH4U':False,'In MHWI':True,'In MHS2':False}
    df_general = df_general.append(s,ignore_index=True)

for i in range(len(df_world_equipment)):
    s = {'Name':df_world_equipment.iloc[i,3],'In MH3U':False,'In MH4U':False,'In MHWI':True,'In MHS2':False}
    df_general = df_general.append(s,ignore_index=True)

for i in range(len(df_world_palico)):
    s = {'Name':df_world_palico.iloc[i,3],'In MH3U':False,'In MH4U':False,'In MHWI':True,'In MHS2':False}
    df_general = df_general.append(s,ignore_index=True)

for i in range(len(df_world_layered)):
    s = {'Name':df_world_layered.iloc[i,1],'In MH3U':False,'In MH4U':False,'In MHWI':True,'In MHS2':False}
    df_general = df_general.append(s,ignore_index=True)

for i in range(len(df_stories_2_items)):
    s = {'Name':df_stories_2_items.iloc[i,1],'In MH3U':False,'In MH4U':False,'In MHWI':False,'In MHS2':True}
    df_general = df_general.append(s,ignore_index=True)

for i in range(len(df_stories_2_armor)):
    s = {'Name':df_stories_2_armor.iloc[i,1],'In MH3U':False,'In MH4U':False,'In MHWI':False,'In MHS2':True}
    df_general = df_general.append(s,ignore_index=True)

for i in range(len(df_stories_2_weapons)):
    s = {'Name':df_stories_2_weapons.iloc[i,2],'In MH3U':False,'In MH4U':False,'In MHWI':False,'In MHS2':True}
    df_general = df_general.append(s,ignore_index=True)

for i in range(len(df_stories_2_talismans)):
    s = {'Name':df_stories_2_talismans.iloc[i,2],'In MH3U':False,'In MH4U':False,'In MHWI':False,'In MHS2':True}
    df_general = df_general.append(s,ignore_index=True)

for i in range(len(df_3u_items)):
    s = {'Name':df_3u_items.iloc[i,1],'In MH3U':True,'In MH4U':False,'In MHWI':False,'In MHS2':False}
    df_general = df_general.append(s,ignore_index=True)

for i in range(len(df_3u_equipment)):
    s = {'Name':df_3u_equipment.iloc[i,2],'In MH3U':True,'In MH4U':False,'In MHWI':False,'In MHS2':False}
    df_general = df_general.append(s,ignore_index=True)

for i in range(len(df_4u_items)):
    s = {'Name':df_4u_items.iloc[i,1],'In MH3U':False,'In MH4U':True,'In MHWI':False,'In MHS2':False}
    df_general = df_general.append(s,ignore_index=True)

for i in range(len(df_4u_equipment)):
    s = {'Name':df_4u_equipment.iloc[i,2],'In MH3U':False,'In MH4U':True,'In MHWI':False,'In MHS2':False}
    df_general = df_general.append(s,ignore_index=True)

for i in range(len(df_4u_palico)):
    s = {'Name':df_4u_palico.iloc[i,2],'In MH3U':False,'In MH4U':True,'In MHWI':False,'In MHS2':False}
    df_general = df_general.append(s,ignore_index=True)

df_general = df_general[df_general['Name'] != 0]
df_general = df_general.groupby('Name').aggregate({'In MH3U':'any','In MH4U':'any','In MHWI':'any','In MHS2':'any'})
df_general.to_csv('dictionaries/compendium.csv')