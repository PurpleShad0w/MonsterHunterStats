import os
import sys
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(os.path.dirname(sys.argv[0]))

def gather():
    # Load save data
    df = pd.read_csv('SAVEDATA1000.csv')
    df.drop(['Start','Size','Color','Comment'], axis=1, inplace=True)
    df.set_index('Name', inplace=True)

    # print(df.filter(like='rank',axis=0))
    # print(df.loc['u32 hunter_rank']['Value'].iloc[0])
    # print(df.loc['u32 master_rank']['Value'].iloc[0])

    # Create items dataframe
    df2 = pd.DataFrame(data={'ID':0,'Name':0,'Total Quantity':0,'Quantity in box':0,'Quantity on hunter':0,'Rarity':0,'Type':0},index=(0,1))

    # Locate item pouch items and ammo
    index_pouch = df.index.get_loc('struct mhw_item_pouch item_pouch')
    df_item_pouch_items = df.iloc[index_pouch:index_pouch+74]
    df_item_pouch_ammo = df.iloc[index_pouch+75:index_pouch+123]
    df_item_pouch_items.reset_index(inplace=True)
    df_item_pouch_ammo.reset_index(inplace=True)

    # Gather item pouch items
    for i in range(0,74):
        if 'id' in df_item_pouch_items.iloc[i,0]:
            id = df_item_pouch_items.iloc[i,1]
        if 'amount' in df_item_pouch_items.iloc[i,0]:
            amount = df_item_pouch_items.iloc[i,1]
            s = {'ID':id,'Name':0,'Total Quantity':0,'Quantity in box':0,'Quantity on hunter':amount,'Rarity':0,'Type':0}
            df2 = df2.append(s,ignore_index=True)

    # Gather item pouch ammo
    for i in range(0,48):
        if 'id' in df_item_pouch_ammo.iloc[i,0]:
            id = df_item_pouch_ammo.iloc[i,1]
        if 'amount' in df_item_pouch_ammo.iloc[i,0]:
            amount = df_item_pouch_ammo.iloc[i,1]
            s = {'ID':id,'Name':0,'Total Quantity':0,'Quantity in box':0,'Quantity on hunter':amount,'Rarity':0,'Type':0}
            df2 = df2.append(s,ignore_index=True)

    # Locate item box items, ammo, materials and decorations
    index_box = df.index.get_loc('struct mhw_storage storage')
    df_item_box_items = df.iloc[index_box:index_box+602]
    df_item_box_ammo = df.iloc[index_box+603:index_box+1203]
    df_item_box_materials = df.iloc[index_box+1204:index_box+4954]
    df_item_box_decorations = df.iloc[index_box+4955:index_box+6455]
    df_item_box_items.reset_index(inplace=True)
    df_item_box_ammo.reset_index(inplace=True)
    df_item_box_materials.reset_index(inplace=True)
    df_item_box_decorations.reset_index(inplace=True)

    # Gather item box items
    for i in range(0,602):
        if 'id' in df_item_box_items.iloc[i,0]:
            id = df_item_box_items.iloc[i,1]
        if 'amount' in df_item_box_items.iloc[i,0]:
            amount = df_item_box_items.iloc[i,1]
            s = {'ID':id,'Name':0,'Total Quantity':0,'Quantity in box':amount,'Quantity on hunter':0,'Rarity':0,'Type':0}
            df2 = df2.append(s,ignore_index=True)

    # Gather item box ammo
    for i in range(0,600):
        if 'id' in df_item_box_ammo.iloc[i,0]:
            id = df_item_box_ammo.iloc[i,1]
        if 'amount' in df_item_box_ammo.iloc[i,0]:
            amount = df_item_box_ammo.iloc[i,1]
            s = {'ID':id,'Name':0,'Total Quantity':0,'Quantity in box':amount,'Quantity on hunter':0,'Rarity':0,'Type':0}
            df2 = df2.append(s,ignore_index=True)

    # Gather item box materials
    for i in range(0,3750):
        if 'id' in df_item_box_materials.iloc[i,0]:
            id = df_item_box_materials.iloc[i,1]
        if 'amount' in df_item_box_materials.iloc[i,0]:
            amount = df_item_box_materials.iloc[i,1]
            s = {'ID':id,'Name':0,'Total Quantity':0,'Quantity in box':amount,'Quantity on hunter':0,'Rarity':0,'Type':0}
            df2 = df2.append(s,ignore_index=True)

    # Gather item box decorations
    for i in range(0,1500):
        if 'id' in df_item_box_decorations.iloc[i,0]:
            id = df_item_box_decorations.iloc[i,1]
        if 'amount' in df_item_box_decorations.iloc[i,0]:
            amount = df_item_box_decorations.iloc[i,1]
            s = {'ID':id,'Name':0,'Total Quantity':0,'Quantity in box':amount,'Quantity on hunter':0,'Rarity':0,'Type':0}
            df2 = df2.append(s,ignore_index=True)

    # Create equipment dataframe
    df3 = pd.DataFrame(data={'Serial':0,'Type':0,'ID':0,'Name':0,'Level':0,'Points':0,'Quantity':0,'Rarity':0,'Category':0,'Subcategory':0,'Dict':0},index=(0,1))

    # Locate equipment, palico equipment, palico tools, tools and pendants
    df_equipment = df.iloc[index_box+6455:index_box+171456]
    df_palico_equipment = df.iloc[index_box+205118:index_box+287618]
    df_equipment.reset_index(inplace=True)
    df_palico_equipment.reset_index(inplace=True)
    index_palico = df.index.get_loc('str64 palico_name[64]')
    df_palico_tool = df.iloc[index_palico+66:index_palico+72]
    index_tool = df.index.get_loc('struct mhw_equipment tools[128]')
    # df_tool = df.iloc[index_tool:index_tool+8449]
    # df_tool.reset_index(inplace=True)
    df_pendants = df.iloc[index_tool+8449:index_tool+8515]
    df_deco = pd.DataFrame({'ID':0},index=(0,1))

    # Gather equipment
    for i in range(0,165001):
        if 'serial_item_category' in df_equipment.iloc[i,0]:
            serial = df_equipment.iloc[i,1]
        if 'type' in df_equipment.iloc[i,0]:
            type = df_equipment.iloc[i,1]
        if 'id' in df_equipment.iloc[i,0]:
            id = df_equipment.iloc[i,1]
        if 'level' in df_equipment.iloc[i,0]:
            level = df_equipment.iloc[i,1]+1
        if 'points' in df_equipment.iloc[i,0]:
            points = df_equipment.iloc[i,1]
            s = {'Serial':serial,'Type':type,'ID':id,'Name':0,'Level':level,'Points':points,'Quantity':1,'Rarity':0,'Category':0,'Subcategory':0,'Dict':'hunter'}
            df3 = df3.append(s,ignore_index=True)
        if 'decos' in df_equipment.iloc[i,0]:
            if df_equipment.iloc[i,1] > -1:
                deco = df_equipment.iloc[i,1]
                s = {'ID':deco}
                df_deco = df_deco.append(s,ignore_index=True)

    # Gather palico equipment
    for i in range(0,82500):
        if 'serial_item_category' in df_palico_equipment.iloc[i,0]:
            serial = df_palico_equipment.iloc[i,1]
        if 'type' in df_palico_equipment.iloc[i,0]:
            type = df_palico_equipment.iloc[i,1]
        if 'id' in df_palico_equipment.iloc[i,0]:
            id = df_palico_equipment.iloc[i,1]
        if 'level' in df_palico_equipment.iloc[i,0]:
            level = df_palico_equipment.iloc[i,1]
        if 'points' in df_palico_equipment.iloc[i,0]:
            points = df_palico_equipment.iloc[i,1]
            s = {'Serial':serial,'Type':type,'ID':id,'Name':0,'Level':level,'Points':points,'Quantity':1,'Rarity':0,'Category':0,'Subcategory':0,'Dict':'palico'}
            df3 = df3.append(s,ignore_index=True)

    # Create palico dataframe
    df4 = pd.DataFrame(data={'Tool':0,'Experience':0},index=(0,1))

    # Gather palico tool
    df4 = df4.append({'Tool':'Vigorwasp Spray','Experience':df_palico_tool.iloc[0,0],'Rarity':4},ignore_index=True)
    df4 = df4.append({'Tool':'Flashfly Cage','Experience':df_palico_tool.iloc[1,0],'Rarity':4},ignore_index=True)
    df4 = df4.append({'Tool':'Shieldspire','Experience':df_palico_tool.iloc[2,0],'Rarity':4},ignore_index=True)
    df4 = df4.append({'Tool':'Coral Orchestra','Experience':df_palico_tool.iloc[3,0],'Rarity':4},ignore_index=True)
    df4 = df4.append({'Tool':'Plunderblade','Experience':df_palico_tool.iloc[4,0],'Rarity':4},ignore_index=True)
    df4 = df4.append({'Tool':'Meowlotov Cocktail','Experience':df_palico_tool.iloc[5,0],'Rarity':4},ignore_index=True)

    # Clean dataframes
    df2 = df2[df2['ID'] != 0]
    df3 = df3[(df3['ID'] != 0) | ((df3['Type'] != 0))]
    # df3 = df3[df3['Type'].astype(float).astype(int) >= 0]
    df4 = df4[df4['Tool'] != 0]
    df2['Total Quantity'] = df2['Quantity in box'] + df2['Quantity on hunter']

    # Define dictionaries
    df_dict_items = pd.read_csv('res/dict/world_dictionary_items.csv')
    df_dict_items.set_index('ID', inplace=True)
    df_dict_equipment = pd.read_csv('res/dict/world_dictionary_equipment.csv')
    df_dict_palico = pd.read_csv('res/dict/world_dictionary_palico.csv')

    # Add item information
    for i in range(len(df2)):
        id = df2.iloc[i,0]
        if df_dict_items.index.__contains__(id):
            s = {'ID':id,'Name':df_dict_items.loc[id,'Name'],'Total Quantity':0,'Quantity in box':0,'Quantity on hunter':0,'Rarity':df_dict_items.loc[id,'Rarity'],'Type':df_dict_items.loc[id,'Category']}
            df2 = df2.append(s,ignore_index=True)

    # Add equipment information
    for i in range(len(df3)):
        serial = df3.iloc[i,0]
        type = df3.iloc[i,1]
        id = df3.iloc[i,2]
        if df3.iloc[i,10] == 'hunter':
            df_temp = df_dict_equipment[(df_dict_equipment['Serial'] == serial) & (df_dict_equipment['ID'] == id) & (df_dict_equipment['Type'] == type)]
        elif df3.iloc[i,10] == 'palico':
            df_temp = df_dict_palico[(df_dict_palico['Serial'] == int(float(serial))) & (df_dict_palico['ID'] == int(float(id))) & (df_dict_palico['Type'] == int(float(type)))]
        try:
            df_temp.reset_index(inplace=True)
            s = {'Serial':serial,'Type':type,'ID':id,'Name':df_temp.loc[0,'Name'],'Level':0,'Points':0,'Quantity':0,'Rarity':df_temp.loc[0,'Rarity'],'Category':df_temp.loc[0,'Category'],'Subcategory':df_temp.loc[0,'Subcategory'],'Dict':0}
            df3 = df3.append(s,ignore_index=True)
        except KeyError:
            continue

    # Locate progress flags and extract layered armor out of them
    index_flags = df.index.get_loc('struct mhw_progress_flags progress')
    df_flags = df.iloc[index_flags:index_flags+863]
    df_layered = df_flags[df_flags.index.str.contains('layered')]
    df_layered = df_layered[df_layered['Value'].astype(int) == 1]
    df_layered.reset_index(inplace=True)

    # Define layered armor dataframes
    df_dict_layered = pd.read_csv('res/dict/world_dictionary_layered.csv')
    df5 = pd.DataFrame(data={'Flag':0,'Name':0,'Rarity':0,'Subcategory':0},index=(0,1))

    # Add layered armor information
    for i in range(len(df_layered)):
        name = df_layered.iloc[i,0]
        for j in range(len(df_dict_layered)):
            if df_dict_layered.iloc[j,0] == name:
                s = {'Flag':df_dict_layered.iloc[j,0],'Name':df_dict_layered.iloc[j,1],'Rarity':df_dict_layered.iloc[j,2],'Subcategory':df_dict_layered.iloc[j,3]}
                df5 = df5.append(s,ignore_index=True)

    # Rearranging dataframes
    # Adding sort=False to groupby allows sorting by Game Order
    df2 = df2.groupby(df2['ID'],sort=False).aggregate({'Name':'last','Total Quantity':'sum','Quantity in box':'sum','Quantity on hunter':'sum','Rarity':'last','Type':'last'})
    df3 = df3.groupby([df3['Serial'],df3['Type'],df3['ID']],sort=False).aggregate({'Name':'last','Level':'first','Points':'first','Quantity':'sum','Rarity':'last','Category':'last','Subcategory':'last','Dict':'first'})
    df4 = df4.groupby(df4['Tool'],sort=False).aggregate({'Experience':'first','Rarity':'first'})
    df5 = df5[df5['Flag'] != 0]

    # Outputting dataframes
    df2.to_csv(r'world_output_items.csv',encoding='utf-8')
    df3.to_csv(r'world_output_equipment.csv',encoding='utf-8')
    df4.to_csv(r'world_output_tool.csv',encoding='utf-8')
    df5.to_csv(r'world_output_layered.csv',encoding='utf-8')