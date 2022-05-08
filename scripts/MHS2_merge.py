import os
import sys
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(os.path.dirname(sys.argv[0]))

def merge():
    # Load the outputs of the inventory
    df_items = pd.read_csv('outputs/MHS2_output_items.csv')
    df_weapons = pd.read_csv('outputs/MHS2_output_weapons.csv')
    df_armor = pd.read_csv('outputs/MHS2_output_armor.csv')
    df_talismans = pd.read_csv('outputs/MHS2_output_talismans.csv')
    df_general = pd.DataFrame(data={'Name':0,'Quantity':0,'Level':0,'Category':0,'Subcategory':0},index=(0,1))

    # Fill in the items
    for i in range(len(df_items)):
        s = {'Name':df_items.iloc[i,1],'Quantity':df_items.iloc[i,2],'Level':0,'Category':df_items.iloc[i,3],'Subcategory':df_items.iloc[i,4]}
        df_general = df_general.append(s,ignore_index=True)

    # Fill in the weapons
    for i in range(len(df_weapons)):
        s = {'Name':df_weapons.iloc[i,2],'Quantity':df_weapons.iloc[i,4],'Level':df_weapons.iloc[i,3],'Category':'Weapons','Subcategory':df_weapons.iloc[i,6]}
        df_general = df_general.append(s,ignore_index=True)

    # Fill in the armor
    for i in range(len(df_armor)):
        s = {'Name':df_armor.iloc[i,1],'Quantity':df_armor.iloc[i,3],'Level':df_armor.iloc[i,2],'Category':'Armor','Subcategory':'Armor'}
        df_general = df_general.append(s,ignore_index=True)

    # Fill in the talismans
    for i in range(len(df_talismans)):
        s = {'Name':df_talismans.iloc[i,3],'Quantity':df_talismans.iloc[i,4],'Level':0,'Category':'Talismans','Subcategory':df_talismans.iloc[i,7]}
        df_general = df_general.append(s,ignore_index=True)

    # Clean and output the data
    df_general = df_general.groupby(df_general['Name']).aggregate({'Quantity':'sum','Level':'max','Category':'first','Subcategory':'first'})
    df_general.to_csv(r'outputs/MHS2_output.csv',encoding='utf-8')