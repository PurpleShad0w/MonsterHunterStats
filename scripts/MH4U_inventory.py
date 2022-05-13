import os
import sys
import pandas as pd
import warnings
import re

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(os.path.dirname(sys.argv[0]))

def gather():
    # Load the data
    df = pd.read_csv('saves/MH4U_user.csv')
    df.set_index('Name', inplace=True)

    # Create dataframes
    df2 = pd.DataFrame(data={'ID':0,'Name':0,'Total Quantity':0,'Quantity in box':0,'Quantity on hunter':0,'Rarity':0},index=(0,1))
    df3 = pd.DataFrame(data={'ID':0,'Type':0,'Name':0,'Quantity':1,'Rarity':0,'Category':0,'Subcategory':0,'Dict':0},index=(0,1))

    # Locate items
    index_item_box = df.index.get_loc('struct item i[1400]')
    df_item_box = df.iloc[index_item_box:index_item_box+4201]
    df_item_box.reset_index(inplace=True)
    index_equipment_box = df.index.get_loc('struct equipment_temp e[1500]')
    df_equipment_box = df.iloc[index_equipment_box:index_equipment_box+43501]
    df_equipment_box.reset_index(inplace=True)
    index_palico_box = df.index.get_loc('struct palico_equipment p[600]')
    df_palico_box = df.iloc[index_palico_box:index_palico_box+1801]
    df_palico_box.reset_index(inplace=True)

    # Gather item box items
    for i in range(0,4201):
        if 'ID' in df_item_box.iloc[i,0]:
            id = df_item_box.iloc[i,1]
        if 'amount' in df_item_box.iloc[i,0]:
            amount = df_item_box.iloc[i,1]
            s = {'ID':id,'Name':0,'Total Quantity':0,'Quantity in box':int(amount),'Quantity on hunter':0,'Rarity':0}
            df2 = df2.append(s,ignore_index=True)

    # Gather equipment box equipment
    for i in range(0,43501):
        if 'type' in df_equipment_box.iloc[i,0]:
            type = df_equipment_box.iloc[i,1]
        if 'ID' in df_equipment_box.iloc[i,0]:
            id = df_equipment_box.iloc[i,1]
            s = {'ID':id,'Type':type,'Name':0,'Quantity':1,'Rarity':0,'Category':0,'Subcategory':0,'Dict':'hunter'}
            df3 = df3.append(s,ignore_index=True)

    # Gather palico box equipment
    for i in range(0,1801):
        if 'type' in df_palico_box.iloc[i,0]:
            type = df_palico_box.iloc[i,1]
        if 'ID' in df_palico_box.iloc[i,0]:
            id = df_palico_box.iloc[i,1]
            s = {'ID':id,'Type':type,'Name':0,'Quantity':1,'Rarity':0,'Category':0,'Subcategory':0,'Dict':'palico'}
            df3 = df3.append(s,ignore_index=True)

    # Clean dataframes
    df2 = df2[df2['ID'] != 0]
    df3 = df3[(df3['ID'] != 0) | ((df3['Type'] != 0))]
    df2['Total Quantity'] = df2['Quantity in box'] + df2['Quantity on hunter']

    # Adding dictionaries
    df_dict_items = pd.read_csv('dictionaries/MH4U_dictionary_items.csv')
    df_dict_items.set_index('ID', inplace=True)
    df_dict_equipment = pd.read_csv('dictionaries/MH4U_dictionary_equipment.csv')
    df_dict_palico = pd.read_csv('dictionaries/MH4U_dictionary_palico.csv')

    # Add item information
    for i in range(len(df2)):
        id = df2.iloc[i,0]
        try:
            s = {'ID':id,'Name':df_dict_items.loc[int(float(id)),'Name'],'Total Quantity':0,'Quantity in box':0,'Quantity on hunter':0,'Rarity':df_dict_items.loc[int(float(id)),'Rarity']}
            df2 = df2.append(s,ignore_index=True)
        except KeyError:
            continue

    # Adding equipment information
    for i in range(len(df3)):
        id = df3.iloc[i,0]
        type = df3.iloc[i,1]
        if df3.iloc[i,7] == 'hunter':
            df_temp = df_dict_equipment[(df_dict_equipment['ID'] == int(float(id))) & (df_dict_equipment['Type'] == int(float(type)))]
        elif df3.iloc[i,7] == 'palico':
            df_temp = df_dict_palico[(df_dict_palico['ID'] == int(float(id))) & (df_dict_palico['Type'] == int(float(type)))]
        try:
            df_temp.reset_index(inplace=True)
            s = {'ID':id,'Type':type,'Name':df_temp.loc[0,'Name'],'Quantity':0,'Rarity':df_temp.loc[0,'Rarity'],'Category':df_temp.loc[0,'Category'],'Subcategory':df_temp.loc[0,'Subcategory'],'Dict':0}
            df3 = df3.append(s,ignore_index=True)
        except KeyError:
            continue

    # Cleaning
    df2 = df2.groupby(df2['ID'],sort=False).aggregate({'Name':'last','Total Quantity':'sum','Quantity in box':'sum','Quantity on hunter':'sum','Rarity':'last'})
    df3 = df3.groupby([df3['ID'],df3['Type']],sort=False).aggregate({'Name':'last','Quantity':'sum','Rarity':'last','Category':'last','Subcategory':'last','Dict':'first'})

    # Outputting dataframes
    df2.to_csv(r'outputs/MH4U_output_items.csv',encoding='utf-8')
    df3.to_csv(r'outputs/MH4U_output_equipment.csv',encoding='utf-8')