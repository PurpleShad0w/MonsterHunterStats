import os
import pandas as pd
import pymem
import sys
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
os.chdir(os.path.dirname(sys.argv[0]))

pm = pymem.Pymem('MonsterHunterRise.exe')

pointer = pm.read_long(pm.base_address + 0xFB30C20)
pointer = pm.read_long(pointer + 0x70)
pointer = pm.read_long(pointer + 0x138)
pointer += 0x20

hunt_pointer = pointer - 0x4
capture_pointer = hunt_pointer + 0x420
anomaly_pointer = hunt_pointer + 0x210

names = pd.read_csv('database/MHRS.csv')['Monster'].tolist()
monsters = pd.read_csv('database/monsters.csv')

df = pd.DataFrame(data={'ID':0,'Size':0,'Type':0,'Variation':0,'Name':0,'Hunted':0,'Captured':0,'Killed':0,'Anomalies':0,'Big Crown':0,'Small Crown':0,'Largest Size':0,'Smallest Size':0},index=(0,1))

for i in range(len(names)):
    hunt_pointer += 0x4
    capture_pointer += 0x4
    anomaly_pointer += 0x4

    hunts = pm.read_int(hunt_pointer)
    caps = pm.read_int(capture_pointer)
    anoms = pm.read_int(anomaly_pointer)

    if names[i] not in monsters['Monster'].tolist():
            continue
    
    size = monsters[monsters['Monster'] == names[i]]['Size'].tolist()[0]

    mtype = monsters[monsters['Monster'] == names[i]]['Type'].tolist()[0]

    mvar = monsters[monsters['Monster'] == names[i]]['Variation'].tolist()[0]

    kills = hunts - caps

    s = pd.Series({'ID':i,'Size':size,'Type':mtype,'Variation':mvar,'Name':names[i],'Hunted':hunts,'Captured':caps,'Killed':kills,'Anomalies':anoms,'Big Crown':'','Small Crown':'','Largest Size':0,'Smallest Size':0})
    df = pd.concat([df, s.to_frame().T], ignore_index=True)

df = df[df['Name'] != 0]
df = df[df['Size'] != 'Unknown']

df.to_csv(r'logs/MHRS.csv',encoding='utf-8',index=False)