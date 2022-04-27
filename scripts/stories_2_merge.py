import os
import sys
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(os.path.dirname(sys.argv[0]))

def merge():
    # Load the outputs of the inventory
    df_items = pd.read_csv('stories_2_output_items.csv')
    df_weapons = pd.read_csv('stories_2_output_weapons.csv')
    df_armor = pd.read_csv('stories_2_output_armor.csv')
    df_talismans = pd.read_csv('stories_2_output_talismans.csv')
    df_general = pd.DataFrame(data={'Item Name':0,'Quantity Possessed':0,'Item Level':0,'Item Category':0,'Item Subcategory':0},index=(0,1))

    # Fill in the items
    for i in range(len(df_items)):
        s = {'Item Name':df_items.iloc[i,1],'Quantity Possessed':df_items.iloc[i,2],'Item Level':0,'Item Category':df_items.iloc[i,3],'Item Subcategory':df_items.iloc[i,4]}
        df_general = df_general.append(s,ignore_index=True)

    # Fill in the weapons
    for i in range(len(df_weapons)):
        s = {'Item Name':df_weapons.iloc[i,2],'Quantity Possessed':df_weapons.iloc[i,4],'Item Level':df_weapons.iloc[i,3],'Item Category':'Weapons','Item Subcategory':df_weapons.iloc[i,6]}
        df_general = df_general.append(s,ignore_index=True)

    # Fill in the armor
    for i in range(len(df_armor)):
        s = {'Item Name':df_armor.iloc[i,1],'Quantity Possessed':df_armor.iloc[i,3],'Item Level':df_armor.iloc[i,2],'Item Category':'Armor','Item Subcategory':'Armor'}
        df_general = df_general.append(s,ignore_index=True)

    # Fill in the talismans
    for i in range(len(df_talismans)):
        s = {'Item Name':df_talismans.iloc[i,3],'Quantity Possessed':df_talismans.iloc[i,4],'Item Level':0,'Item Category':'Talismans','Item Subcategory':df_talismans.iloc[i,7]}
        df_general = df_general.append(s,ignore_index=True)

    # Clean and output the data
    df_general = df_general.groupby(df_general['Item Name']).aggregate({'Quantity Possessed':'sum','Item Level':'max','Item Category':'first','Item Subcategory':'first'})
    df_general.to_csv(r'stories_2_output.csv',encoding='utf-8')