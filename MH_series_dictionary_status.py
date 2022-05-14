import os
import sys
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(os.path.dirname(sys.argv[0]))

# Load the dictionaries
df_world_items = pd.read_csv('dictionaries/MHWI_dictionary_items.csv')
df_stories_2_items = pd.read_csv('dictionaries/MHS2_dictionary_items.csv')
df_3u_items = pd.read_csv('dictionaries/MH3U_dictionary_items.csv')
df_4u_items = pd.read_csv('dictionaries/MH4U_dictionary_items.csv')

# Select IDs
df_world_items = df_world_items['ID'].to_list()
df_stories_2_items = df_stories_2_items['ID'].to_list()
df_3u_items = df_3u_items['ID'].to_list()
df_4u_items = df_4u_items['ID'].to_list()
df_world_missing_IDs = []
df_stories_2_missing_IDs = []
df_3u_missing_IDs = []
df_4u_missing_IDs = []

# Locate missing IDs for MHWI
for i in range(max(df_world_items)):
    if i+1 in df_world_items:
        continue
    else:
        df_world_missing_IDs.append(i+1)

# Locate missing IDs for MHS2
for i in range(max(df_stories_2_items)):
    if i+1 in df_stories_2_items:
        continue
    else:
        df_stories_2_missing_IDs.append(i+1)

# Locate missing IDs for MH3U
for i in range(max(df_3u_items)):
    if i+1 in df_3u_items:
        continue
    else:
        df_3u_missing_IDs.append(i+1)

# Locate missing IDs for MH4U
for i in range(max(df_4u_items)):
    if i+1 in df_4u_items:
        continue
    else:
        df_4u_missing_IDs.append(i+1)

with open('status.txt', 'w') as f:
    f.write('--- Items Dictionary Completion Status ---')
    f.write('\n\nMHWI: ' + str(len(df_world_items)/max(df_world_items)*100) + '%')
    f.write('\nMHS2: ' + str(len(df_stories_2_items)/max(df_stories_2_items)*100) + '%')
    f.write('\nMH3U: ' + str(len(df_3u_items)/max(df_3u_items)*100) + '%')
    f.write('\nMH4U: ' + str(len(df_4u_items)/max(df_4u_items)*100) + '%')
    f.write('\n\n--- Amount of missing IDs ---')
    f.write('\n\nMHWI: ' + str(len(df_world_missing_IDs)))
    f.write('\nMHS2: ' + str(len(df_stories_2_missing_IDs)))
    f.write('\nMH3U: ' + str(len(df_3u_missing_IDs)))
    f.write('\nMH4U: ' + str(len(df_4u_missing_IDs)))
    f.write('\n\n--- Missing Item IDs ---')
    f.write('\n\nMHWI Missing IDs: ' + str(df_world_missing_IDs))
    f.write('\n\nMHS2 Missing IDs: ' + str(df_stories_2_missing_IDs))
    f.write('\n\nMH3U Missing IDs: ' + str(df_3u_missing_IDs))
    f.write('\n\nMH4U Missing IDs: ' + str(df_4u_missing_IDs))