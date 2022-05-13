import os
import sys
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(os.path.dirname(sys.argv[0]))

def merge():
    # Load the outputs of the inventory
    df_items = pd.read_csv('outputs/MH4U_output_items.csv')
    df_equipment = pd.read_csv('outputs/MH4U_output_equipment.csv')
    df_general = pd.DataFrame(data={'Name':0,'Quantity':0,'Rarity':0,'Category':0,'Subcategory':0},index=(0,1))

    # Fill in the items
    for i in range(len(df_items)):
        s = {'Name':df_items.iloc[i,1],'Quantity':df_items.iloc[i,2],'Rarity':df_items.iloc[i,5],'Category':'Items','Subcategory':0}
        df_general = df_general.append(s,ignore_index=True)

    # Fill in the equipment
    for i in range(len(df_equipment)):
        s = {'Name':df_equipment.iloc[i,2],'Quantity':df_equipment.iloc[i,3],'Rarity':df_equipment.iloc[i,4],'Category':df_equipment.iloc[i,5],'Subcategory':df_equipment.iloc[i,6]}
        df_general = df_general.append(s,ignore_index=True)

    # Clean and output the data
    df_general = df_general.groupby(df_general['Name']).aggregate({'Quantity':'sum','Rarity':'max','Category':'first','Subcategory':'first'})
    df_general.to_csv(r'outputs/MH4U_output.csv',encoding='utf-8')