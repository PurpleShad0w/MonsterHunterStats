import os
import pandas as pd
import pymem
import struct
import sys
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
os.chdir(os.path.dirname(sys.argv[0]))

pm = pymem.Pymem('MonsterHunterWorld.exe')

slot = 1

rcx = pm.read_long(pm.base_address + 0x5011710)
rcx = rcx + 0xA8
rcx = pm.read_longlong(rcx)
rdx = 0x27E9F0 * (slot-1)
rcx = rcx + rdx
rcx = rcx + 0xF4EA8

capture_pointer = rcx - 0x4
kill_pointer = capture_pointer + 0x200
large_pointer = capture_pointer + 0xC00
small_pointer = capture_pointer + 0xE00
xp_pointer = capture_pointer + 0x1000
level_pointer = capture_pointer + 0x1200

names = pd.read_csv('database/MHWI.csv')['Monster'].tolist()
sizes = pd.read_csv('database/MHWI.csv')
monsters = pd.read_csv('database/monsters.csv')

df = pd.DataFrame(data={'ID':0,'Size':0,'Type':0,'Variation':0,'Name':0,'Hunted':0,'Captured':0,'Killed':0,'Big Crown':0,'Small Crown':0,'Largest Size':0,'Smallest Size':0,'XP':0,'Research Level':0},index=(0,1))

for i in range(len(names)):
    capture_pointer += 0x4
    kill_pointer += 0x4
    large_pointer += 0x4
    small_pointer += 0x4
    xp_pointer += 0x4
    level_pointer += 0x4
    caps = pm.read_int(capture_pointer)
    kills = pm.read_int(kill_pointer)
    large = pm.read_int(large_pointer)
    small = pm.read_int(small_pointer)
    xp = pm.read_int(xp_pointer)
    level = pm.read_int(level_pointer)

    if names[i] not in monsters['Monster'].tolist():
        continue

    size = monsters[monsters['Monster'] == names[i]]['Size'].tolist()[0]

    threshold_silver = sizes[sizes['Monster'] == names[i]]['Silver'].tolist()[0]
    threshold_gold = sizes[sizes['Monster'] == names[i]]['Gold'].tolist()[0]
    threshold_small = sizes[sizes['Monster'] == names[i]]['Small'].tolist()[0]

    if large >= threshold_gold and large != 0:
        big_crown = '👑'
    elif large >= threshold_silver and large != 0:
        big_crown = '🥈'
    else:
        big_crown = ''
    
    if small <= threshold_small and small != 0:
        small_crown = '👑'
    else:
        small_crown = ''

    mtype = monsters[monsters['Monster'] == names[i]]['Type'].tolist()[0]

    mvar = monsters[monsters['Monster'] == names[i]]['Variation'].tolist()[0]

    hunts = caps + kills

    xp = struct.unpack("@f", struct.pack("@I", xp))[0]

    s = pd.Series({'ID':i,'Size':size,'Type':mtype,'Variation':mvar,'Name':names[i],'Hunted':hunts,'Captured':caps,'Killed':kills,'Big Crown':big_crown,'Small Crown':small_crown,'Largest Size':large,'Smallest Size':small,'XP':xp,'Research Level':level})
    df = pd.concat([df, s.to_frame().T], ignore_index=True)

df = df[df['Name'] != 0]
df = df[df['Size'] != 'Unknown']

df.to_csv(r'logs/MHWI.csv',encoding='utf-8',index=False)