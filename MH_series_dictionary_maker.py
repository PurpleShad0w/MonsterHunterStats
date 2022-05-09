import os
import sys
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(os.path.dirname(sys.argv[0]))

# Load the dictionaries
df_world_items = pd.read_csv('dictionaries/MHWI_dictionary_items.csv')
df_world_equipment = pd.read_csv('dictionaries/MHWI_dictionary_equipment.csv')
df_world_palico = pd.read_csv('dictionaries/MHWI_dictionary_palico.csv')
df_world_layered = pd.read_csv('dictionaries/MHWI_dictionary_layered.csv')
df_stories_2_items = pd.read_csv('dictionaries/MHS2_dictionary_items.csv')
df_stories_2_armor = pd.read_csv('dictionaries/MHS2_dictionary_armor.csv')
df_stories_2_weapons = pd.read_csv('dictionaries/MHS2_dictionary_weapons.csv')
df_stories_2_talismans = pd.read_csv('dictionaries/MHS2_dictionary_talismans.csv')
df_3u_items = pd.read_csv('dictionaries/MH3U_dictionary_items.csv')
df_3u_equipment = pd.read_csv('dictionaries/MH3U_dictionary_equipment.csv')
df_4u_items = pd.read_csv('dictionaries/MH4U_dictionary_items.csv')

# Create dataframe
df_general = pd.DataFrame(data={'Name':0,'In MH3U':0,'In MH4U':0,'In MHWI':0,'In MHS2':0},index=(0,1))

# Input world items
for i in range(len(df_world_items)):
    s = {'Name':df_world_items.iloc[i,1],'In MH3U':False,'In MH4U':False,'In MHWI':True,'In MHS2':False}
    df_general = df_general.append(s,ignore_index=True)

# Input world equipment
for i in range(len(df_world_equipment)):
    s = {'Name':df_world_equipment.iloc[i,3],'In MH3U':False,'In MH4U':False,'In MHWI':True,'In MHS2':False}
    df_general = df_general.append(s,ignore_index=True)

# Input world palico equipment
for i in range(len(df_world_palico)):
    s = {'Name':df_world_palico.iloc[i,3],'In MH3U':False,'In MH4U':False,'In MHWI':True,'In MHS2':False}
    df_general = df_general.append(s,ignore_index=True)

# Input world layered armor
for i in range(len(df_world_layered)):
    s = {'Name':df_world_layered.iloc[i,1],'In MH3U':False,'In MH4U':False,'In MHWI':True,'In MHS2':False}
    df_general = df_general.append(s,ignore_index=True)

# Input stories 2 items
for i in range(len(df_stories_2_items)):
    s = {'Name':df_stories_2_items.iloc[i,1],'In MH3U':False,'In MH4U':False,'In MHWI':False,'In MHS2':True}
    df_general = df_general.append(s,ignore_index=True)

# Input stories 2 armor
for i in range(len(df_stories_2_armor)):
    s = {'Name':df_stories_2_armor.iloc[i,1],'In MH3U':False,'In MH4U':False,'In MHWI':False,'In MHS2':True}
    df_general = df_general.append(s,ignore_index=True)

# Input stories 2 weapons
for i in range(len(df_stories_2_weapons)):
    s = {'Name':df_stories_2_weapons.iloc[i,2],'In MH3U':False,'In MH4U':False,'In MHWI':False,'In MHS2':True}
    df_general = df_general.append(s,ignore_index=True)

# Input stories 2 talismans
for i in range(len(df_stories_2_talismans)):
    s = {'Name':df_stories_2_talismans.iloc[i,2],'In MH3U':False,'In MH4U':False,'In MHWI':False,'In MHS2':True}
    df_general = df_general.append(s,ignore_index=True)

# Input 3u items
for i in range(len(df_3u_items)):
    s = {'Name':df_3u_items.iloc[i,1],'In MH3U':True,'In MH4U':False,'In MHWI':False,'In MHS2':False}
    df_general = df_general.append(s,ignore_index=True)

# Input 3u equipment
for i in range(len(df_3u_equipment)):
    s = {'Name':df_3u_equipment.iloc[i,2],'In MH3U':True,'In MH4U':False,'In MHWI':False,'In MHS2':False}
    df_general = df_general.append(s,ignore_index=True)

# Input 4u items
for i in range(len(df_4u_items)):
    s = {'Name':df_4u_items.iloc[i,1],'In MH3U':False,'In MH4U':True,'In MHWI':False,'In MHS2':False}
    df_general = df_general.append(s,ignore_index=True)

# Clean and output data
df_general = df_general[df_general['Name'] != 0]
df_general = df_general.groupby('Name').aggregate({'In MH3U':'any','In MH4U':'any','In MHWI':'any','In MHS2':'any'})
df_general.to_csv('dictionaries/MH_series_compendium.csv')