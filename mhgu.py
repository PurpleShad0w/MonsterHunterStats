import os
import sys
import pandas as pd
import warnings
from tkinter.filedialog import askopenfilename
import struct

warnings.simplefilter(action='ignore', category=FutureWarning)
os.chdir(os.path.dirname(sys.argv[0]))

offsets = [1625876, 1650570, 1650572]
items = pd.DataFrame()
items['type'] = [0] * 2300
items['id'] = [None] * 2300
items['name'] = [None] * 2300
items['count'] = [None] * 2300
items['category'] = ['Items'] * 2300
dict_items = pd.read_csv('dicts/mhgu/items.csv')
equips = pd.DataFrame()
equips['type'] = [None] * 2000
equips['id'] = [None] * 2000
equips['name'] = [None] * 2000
equips['count'] = [1] * 2000
equips['category'] = ['Equipment'] * 2000

dict_equips = [[0],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

for i in range(20):
    with open('dicts/mhgu/equipment/'+str(i+1)+'.txt') as f:
        dict_equips[i+1] = [line.rstrip() for line in f]

filename = askopenfilename()

def access_bit(data, num):
    base = int(num // 8)
    shift = int(num % 8)
    return (data[base] >> shift) & 0x1

with open(filename, mode='rb') as file:
    offset = offsets[0]
    file.seek(offset)
    item_box = file.read(5463)
    bits = [access_bit(item_box,i) for i in range(len(item_box)*8)]
    bits_array = [bits[i * 19:(i + 1) * 19] for i in range((len(bits) + 19 - 1) // 19)]

    for i in range(2300):
        bits_item = ''.join(map(str, bits_array[i]))
        bits_item = bits_item[::-1]
        count = bits_item[:7]
        id = bits_item[7:20]
        items.iloc[i,1] = int(id, 2)
        items.iloc[i,3] = int(count, 2)
        if items.iloc[i,1] == 0:
            continue
        items.iloc[i,2] = dict_items.loc[dict_items['_id'] == items.iloc[i,1], 'name'].iloc[0]
    
    for i in range(2000):
        offset = offsets[1] + i * 36
        file.seek(offset)
        equips.iloc[i,0] = struct.unpack('H', file.read(2))[0]

        offset = offsets[2] + i * 36
        file.seek(offset)
        equips.iloc[i,1] = struct.unpack('H', file.read(2))[0]

        if equips.iloc[i,0] > 20 or equips.iloc[i,1] == 0:
            continue
        equips.iloc[i,2] = dict_equips[equips.iloc[i,0]][equips.iloc[i,1]]


inv = pd.concat([items, equips], axis=0)
inv = inv.groupby([inv['type'],inv['id'],inv['category']], sort=False).aggregate({'name': 'first', 'count': 'sum'})
inv.to_csv('inv/mhgu.csv')