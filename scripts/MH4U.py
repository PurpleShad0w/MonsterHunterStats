import mhef.n3ds
import os
import pandas as pd
import subprocess
import sys
import warnings

from argparse import Namespace

warnings.simplefilter(action='ignore', category=FutureWarning)
os.chdir(os.path.dirname(sys.argv[0]))


args = Namespace(mode='d', inputfile='saves/MH4U', outputfile='saves/MH4U.bin')

sc = mhef.n3ds.SavedataCipher(mhef.n3ds.MH4G_NA)
sc.decrypt_file(args.inputfile, args.outputfile)

subprocess.call("C:/Program Files/010 Editor/010Editor.exe saves/MH4U.bin -template:templates/MH4U.bt -script:scripts/MH4U.1sc -noui")

df = pd.read_csv('saves/MH4U.csv')
df.drop(['Start','Size','Color','Comment'], axis=1, inplace=True)
df.set_index('Name', inplace=True)

df2 = pd.DataFrame(data={'ID':0,'Name':0,'Total Quantity':0,'Quantity in box':0,'Quantity on hunter':0,'Rarity':0},index=(0,1))
df3 = pd.DataFrame(data={'ID':0,'Type':0,'Name':0,'Quantity':1,'Rarity':0,'Category':0,'Subcategory':0,'Dict':0},index=(0,1))

index_item_box = df.index.get_loc('struct item i[1400]')
df_item_box = df.iloc[index_item_box:index_item_box+4201]
df_item_box.reset_index(inplace=True)
index_equipment_box = df.index.get_loc('struct equipment_temp e[1500]')
df_equipment_box = df.iloc[index_equipment_box:index_equipment_box+43501]
df_equipment_box.reset_index(inplace=True)
index_palico_box = df.index.get_loc('struct palico_equipment p[600]')
df_palico_box = df.iloc[index_palico_box:index_palico_box+1801]
df_palico_box.reset_index(inplace=True)

for i in range(0,4201):
    if 'ID' in df_item_box.iloc[i,0]:
        id = df_item_box.iloc[i,1]
    if 'amount' in df_item_box.iloc[i,0]:
        amount = df_item_box.iloc[i,1]
        s = {'ID':id,'Name':0,'Total Quantity':0,'Quantity in box':int(amount),'Quantity on hunter':0,'Rarity':0}
        df2 = df2.append(s,ignore_index=True)

for i in range(0,43501):
    if 'type' in df_equipment_box.iloc[i,0]:
        type = df_equipment_box.iloc[i,1]
    if 'ID' in df_equipment_box.iloc[i,0]:
        id = df_equipment_box.iloc[i,1]
        s = {'ID':id,'Type':type,'Name':0,'Quantity':1,'Rarity':0,'Category':0,'Subcategory':0,'Dict':'hunter'}
        df3 = df3.append(s,ignore_index=True)

for i in range(0,1801):
    if 'type' in df_palico_box.iloc[i,0]:
        type = df_palico_box.iloc[i,1]
    if 'ID' in df_palico_box.iloc[i,0]:
        id = df_palico_box.iloc[i,1]
        s = {'ID':id,'Type':type,'Name':0,'Quantity':1,'Rarity':0,'Category':0,'Subcategory':0,'Dict':'palico'}
        df3 = df3.append(s,ignore_index=True)

df2 = df2[df2['ID'] != 0]
df3 = df3[(df3['ID'] != 0) | ((df3['Type'] != 0))]
df2['Total Quantity'] = df2['Quantity in box'] + df2['Quantity on hunter']

df_dict_items = pd.read_csv('dictionaries/MH4U_items.csv')
df_dict_items.set_index('ID', inplace=True)
df_dict_equipment = pd.read_csv('dictionaries/MH4U_equipment.csv')
df_dict_palico = pd.read_csv('dictionaries/MH4U_palico.csv')

for i in range(len(df2)):
    id = df2.iloc[i,0]
    try:
        s = {'ID':id,'Name':df_dict_items.loc[int(float(id)),'Name'],'Total Quantity':0,'Quantity in box':0,'Quantity on hunter':0,'Rarity':df_dict_items.loc[int(float(id)),'Rarity']}
        df2 = df2.append(s,ignore_index=True)
    except KeyError:
        continue

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

df2 = df2.groupby(df2['ID'],sort=False).aggregate({'Name':'last','Total Quantity':'sum','Quantity in box':'sum','Quantity on hunter':'sum','Rarity':'last'})
df3 = df3.groupby([df3['ID'],df3['Type']],sort=False).aggregate({'Name':'last','Quantity':'sum','Rarity':'last','Category':'last','Subcategory':'last','Dict':'first'})

df_items = df2
df_equipment = df3
df_general = pd.DataFrame(data={'Name':0,'Quantity':0,'Rarity':0,'Category':0,'Subcategory':0},index=(0,1))

for i in range(len(df_items)):
    s = {'Name':df_items.iloc[i,1],'Quantity':df_items.iloc[i,2],'Rarity':df_items.iloc[i,5],'Category':'Items','Subcategory':0}
    df_general = df_general.append(s,ignore_index=True)

for i in range(len(df_equipment)):
    s = {'Name':df_equipment.iloc[i,2],'Quantity':df_equipment.iloc[i,3],'Rarity':df_equipment.iloc[i,4],'Category':df_equipment.iloc[i,5],'Subcategory':df_equipment.iloc[i,6]}
    df_general = df_general.append(s,ignore_index=True)

df_general = df_general.groupby(df_general['Name']).aggregate({'Quantity':'sum','Rarity':'max','Category':'first','Subcategory':'first'})
df_general.to_csv(r'outputs/MH4U.csv',encoding='utf-8')