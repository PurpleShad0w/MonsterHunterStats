import os
import sys
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(os.path.dirname(sys.argv[0]))

# Load the game outputs
df_world = pd.read_csv('outputs/MHWI_output.csv')
df_stories_2 = pd.read_csv('outputs/MHS2_output.csv')
df_3u = pd.read_csv('outputs/MH3U_output.csv')
df_general = pd.DataFrame(data={'Name':0,'Quantity in MH3U':0,'Quantity in MHWI':0,'Quantity in MHS2':0,'Level':0,'Experience':0,'Rarity':0,'Category':0,'Subcategory':0},index=(0,1))

# Load the world data
for i in range(len(df_world)):
    s = {'Name':df_world.iloc[i,0],'Quantity in MH3U':0,'Quantity in MHWI':df_world.iloc[i,1],'Quantity in MHS2':0,'Level':df_world.iloc[i,2],'Experience':df_world.iloc[i,3],'Rarity':df_world.iloc[i,4],'Category':df_world.iloc[i,5],'Subcategory':df_world.iloc[i,6]}
    df_general = df_general.append(s,ignore_index=True)

# Load the stories 2 data
for i in range(len(df_stories_2)):
    s = {'Name':df_stories_2.iloc[i,0],'Quantity in MH3U':0,'Quantity in MHWI':0,'Quantity in MHS2':df_stories_2.iloc[i,1],'Level':df_stories_2.iloc[i,2],'Experience':0,'Rarity':0,'Category':df_stories_2.iloc[i,3],'Subcategory':df_stories_2.iloc[i,4]}
    df_general = df_general.append(s,ignore_index=True)

# Load the 3u data
for i in range(len(df_3u)):
    s = {'Name':df_3u.iloc[i,0],'Quantity in MH3U':df_3u.iloc[i,1],'Quantity in MHWI':0,'Quantity in MHS2':0,'Level':df_3u.iloc[i,2],'Experience':0,'Rarity':df_3u.iloc[i,3],'Category':df_3u.iloc[i,4],'Subcategory':df_3u.iloc[i,5]}
    df_general = df_general.append(s,ignore_index=True)

# Clean and output the data
df_general = df_general.groupby(df_general['Name']).aggregate({'Quantity in MH3U':'sum','Quantity in MHWI':'sum','Quantity in MHS2':'sum','Level':'max','Experience':'max','Rarity':'max','Category':'last','Subcategory':'last'})
df_general.to_csv(r'outputs/MH_series_output.csv',encoding='utf-8')