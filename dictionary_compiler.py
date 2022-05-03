import os
import sys
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(os.path.dirname(sys.argv[0]))

# Load the dictionaries
df_world_items = pd.read_csv('dictionaries/world_dictionary_items.csv')
df_world_equipment = pd.read_csv('dictionaries/world_dictionary_equipment.csv')
df_world_palico = pd.read_csv('dictionaries/world_dictionary_palico.csv')
df_world_layered = pd.read_csv('dictionaries/world_dictionary_layered.csv')
df_stories_2_items = pd.read_csv('dictionaries/stories_2_dictionary_items.csv')
df_stories_2_armor = pd.read_csv('dictionaries/stories_2_dictionary_armor.csv')
df_stories_2_weapons = pd.read_csv('dictionaries/stories_2_dictionary_weapons.csv')
df_stories_2_talismans = pd.read_csv('dictionaries/stories_2_dictionary_talismans.csv')

# Create dataframe
df_general = pd.DataFrame(data={'Name':0,'In MHWI':0,'In MHST2':0},index=(0,1))

# Input world items
for i in range(len(df_world_items)):
    s = {'Name':df_world_items.iloc[i,1],'In MHWI':True,'In MHST2':False}
    df_general = df_general.append(s,ignore_index=True)

# Input world equipment
for i in range(len(df_world_equipment)):
    s = {'Name':df_world_equipment.iloc[i,3],'In MHWI':True,'In MHST2':False}
    df_general = df_general.append(s,ignore_index=True)

# Input world palico equipment
for i in range(len(df_world_palico)):
    s = {'Name':df_world_palico.iloc[i,3],'In MHWI':True,'In MHST2':False}
    df_general = df_general.append(s,ignore_index=True)

# Input world layered armor
for i in range(len(df_world_layered)):
    s = {'Name':df_world_layered.iloc[i,1],'In MHWI':True,'In MHST2':False}
    df_general = df_general.append(s,ignore_index=True)

# Input stories 2 items
for i in range(len(df_stories_2_items)):
    s = {'Name':df_stories_2_items.iloc[i,1],'In MHWI':False,'In MHST2':True}
    df_general = df_general.append(s,ignore_index=True)

# Input stories 2 armor
for i in range(len(df_stories_2_armor)):
    s = {'Name':df_stories_2_armor.iloc[i,1],'In MHWI':False,'In MHST2':True}
    df_general = df_general.append(s,ignore_index=True)

# Input stories 2 weapons
for i in range(len(df_stories_2_weapons)):
    s = {'Name':df_stories_2_weapons.iloc[i,2],'In MHWI':False,'In MHST2':True}
    df_general = df_general.append(s,ignore_index=True)

# Input stories 2 talismans
for i in range(len(df_stories_2_talismans)):
    s = {'Name':df_stories_2_talismans.iloc[i,2],'In MHWI':False,'In MHST2':True}
    df_general = df_general.append(s,ignore_index=True)

# Clean and output data
df_general = df_general[df_general['Name'] != 0]
df_general = df_general.groupby('Name').aggregate({'In MHWI':'any','In MHST2':'any'})
df_general.to_csv('dictionaries/monster_hunter_item_compendium.csv')