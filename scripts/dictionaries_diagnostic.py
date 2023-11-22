import os
import pandas as pd
import sys
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
os.chdir(os.path.dirname(sys.argv[0]))


df_world_items = pd.read_csv('dictionaries/MHWI_items.csv')
df_stories_2_items = pd.read_csv('dictionaries/MHS2_items.csv')
df_3u_items = pd.read_csv('dictionaries/MH3U_items.csv')
df_4u_items = pd.read_csv('dictionaries/MH4U_items.csv')

df_world_items = df_world_items['ID'].to_list()
df_stories_2_items = df_stories_2_items['ID'].to_list()
df_3u_items = df_3u_items['ID'].to_list()
df_4u_items = df_4u_items['ID'].to_list()
df_world_missing_IDs = []
df_stories_2_missing_IDs = []
df_3u_missing_IDs = []
df_4u_missing_IDs = []

for i in range(max(df_world_items)):
    if i+1 in df_world_items:
        continue
    else:
        df_world_missing_IDs.append(i+1)

for i in range(max(df_stories_2_items)):
    if i+1 in df_stories_2_items:
        continue
    else:
        df_stories_2_missing_IDs.append(i+1)

for i in range(max(df_3u_items)):
    if i+1 in df_3u_items:
        continue
    else:
        df_3u_missing_IDs.append(i+1)

for i in range(max(df_4u_items)):
    if i+1 in df_4u_items:
        continue
    else:
        df_4u_missing_IDs.append(i+1)

with open('status.txt', 'w') as f:
    f.write('--- Items Dictionary Completion Status ---')
    f.write('\n\nMHWI: ' + str(len(df_world_items)/max(df_world_items)*100) + ' %')
    f.write('\nMHS2: ' + str(len(df_stories_2_items)/max(df_stories_2_items)*100) + ' %')
    f.write('\nMH3U: ' + str(len(df_3u_items)/max(df_3u_items)*100) + ' %')
    f.write('\nMH4U: ' + str(len(df_4u_items)/max(df_4u_items)*100) + ' %')
    f.write('\n\nMHWI: ' + str(len(df_world_items)) + '/' + str(max(df_world_items)))
    f.write('\nMHS2: ' + str(len(df_stories_2_items)) + '/' + str(max(df_stories_2_items)))
    f.write('\nMH3U: ' + str(len(df_3u_items)) + '/' + str(max(df_3u_items)))
    f.write('\nMH4U: ' + str(len(df_4u_items)) + '/' + str(max(df_4u_items)))
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