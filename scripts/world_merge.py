import os
import sys
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(os.path.dirname(sys.argv[0]))

def merge():
    # Load the outputs of inventory.py
    df_items = pd.read_csv('outputs/world_output_items.csv')
    df_equipment = pd.read_csv('outputs/world_output_equipment.csv')
    df_tool = pd.read_csv('outputs/world_output_tool.csv')
    df_layered = pd.read_csv('outputs/world_output_layered.csv')
    df_general = pd.DataFrame(data={'Name':0,'Quantity':0,'Level':0,'Experience':0,'Rarity':0,'Category':0,'Subcategory':0},index=(0,1))

    # Fill in the items
    for i in range(len(df_items)):
        s = {'Name':df_items.iloc[i,1],'Quantity':df_items.iloc[i,2],'Level':0,'Experience':0,'Rarity':df_items.iloc[i,5],'Category':df_items.iloc[i,6],'Subcategory':0}
        df_general = df_general.append(s,ignore_index=True)

    # Fill in the equipment
    for i in range(len(df_equipment)):
        s = {'Name':df_equipment.iloc[i,3],'Quantity':df_equipment.iloc[i,6],'Level':df_equipment.iloc[i,4],'Experience':df_equipment.iloc[i,5],'Rarity':df_equipment.iloc[i,7],'Category':df_equipment.iloc[i,8],'Subcategory':df_equipment.iloc[i,9]}
        df_general = df_general.append(s,ignore_index=True)

    # Fill in the tools
    for i in range(len(df_tool)):
        s = {'Name':df_tool.iloc[i,0],'Quantity':1,'Level':0,'Experience':df_tool.iloc[i,1],'Rarity':df_tool.iloc[i,2],'Category':'Palico Gadgets','Subcategory':0}
        df_general = df_general.append(s,ignore_index=True)

    # Fill in the layered armor    
    for i in range(len(df_layered)):
        s = {'Name':df_layered.iloc[i,2],'Quantity':1,'Level':0,'Experience':0,'Rarity':df_layered.iloc[i,3],'Category':'Layered Armor','Subcategory':df_layered.iloc[i,4]}
        df_general = df_general.append(s,ignore_index=True)

    # Clean and output the data
    df_general = df_general.groupby(df_general['Name']).aggregate({'Quantity':'sum','Level':'max','Experience':'max','Rarity':'first','Category':'first','Subcategory':'first'})
    df_general.to_csv(r'outputs/world_output.csv',encoding='utf-8')