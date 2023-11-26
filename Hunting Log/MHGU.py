import os
import pandas as pd
import shutil
import struct
import sys
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
os.chdir(os.path.dirname(sys.argv[0]))

offset_hex = ['0x192B42','0x192C54','0x192D66','0x192D68']
formats = {1:'B', 2:'H', 4:'I', 8:'Q'}
kills, caps, size_small, size_big = [None] * 137, [None] * 137, [None] * 137, [None] * 137

names = pd.read_csv('database/MHGU.csv')['Monster'].tolist()
sizes = pd.read_csv('database/MHGU.csv')
monsters = pd.read_csv('database/monsters.csv')

df = pd.DataFrame(data={'ID':0,'Size':0,'Type':0,'Variation':0,'Name':0,'Hunted':0,'Captured':0,'Killed':0,'Big Crown':0,'Small Crown':0,'Largest Size':0,'Smallest Size':0},index=(0,1))

save_path = os.getenv('APPDATA')+'\\Ryujinx\\bis\\user\\save\\0000000000000007\\0\\system'
shutil.copyfile(save_path, os.path.join(os.getcwd(), 'saves\\system'))

with open('saves/system', mode='rb') as file:
    for i in range(len(names)):
        offset = int(offset_hex[0], 16) + i*2
        file.seek(offset)
        kills[i] = struct.unpack(formats[2], file.read(2))[0]

        offset = int(offset_hex[1], 16) + i*2
        file.seek(offset)
        caps[i] = struct.unpack(formats[2], file.read(2))[0]

        offset = int(offset_hex[2], 16) + i*4
        file.seek(offset)
        size_small[i] = struct.unpack(formats[2], file.read(2))[0]

        offset = int(offset_hex[3], 16) + i*4
        file.seek(offset)
        size_big[i] = struct.unpack(formats[2], file.read(2))[0]
    
        hunts = kills[i] + caps[i]

        if names[i] not in monsters['Monster'].tolist():
            continue
        
        size = monsters[monsters['Monster'] == names[i]]['Size'].tolist()[0]

        threshold_silver = sizes[sizes['Monster'] == names[i]]['Silver'].tolist()[0]
        threshold_gold = sizes[sizes['Monster'] == names[i]]['Gold'].tolist()[0]
        threshold_small = sizes[sizes['Monster'] == names[i]]['Small'].tolist()[0]

        if size_big[i] >= threshold_gold and size_big[i] != 0:
            big_crown = '👑'
        elif size_big[i] >= threshold_silver and size_big[i] != 0:
            big_crown = '🥈'
        else:
            big_crown = ''
        
        if size_small[i] <= threshold_small and size_small[i] != 0:
            small_crown = '👑'
        else:
            small_crown = ''

        monster_type = monsters[monsters['Monster'] == names[i]]['Type'].tolist()[0]

        monster_var = monsters[monsters['Monster'] == names[i]]['Variation'].tolist()[0]

        s = pd.Series({'ID':i,'Size':size,'Type':monster_type,'Variation':monster_var,'Name':names[i],'Hunted':hunts,'Captured':caps[i],'Killed':kills[i],'Big Crown':big_crown,'Small Crown':small_crown,'Largest Size':size_big[i],'Smallest Size':size_small[i]})
        df = pd.concat([df, s.to_frame().T], ignore_index=True)

df = df[df['Name'] != 0]
df = df[df['Size'] != 'Unknown']
df.to_csv(r'logs/MHGU.csv',encoding='utf-8',index=False)