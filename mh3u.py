import os
import sys
import pandas as pd
import warnings
from tkinter.filedialog import askopenfilename
import struct

warnings.simplefilter(action='ignore', category=FutureWarning)
os.chdir(os.path.dirname(sys.argv[0]))

offsets = [396, 398, 4396, 4398]
items = pd.DataFrame()
items['type'] = [0] * 1000
items['id'] = [None] * 1000
items['name'] = [None] * 1000
items['count'] = [None] * 1000
items['category'] = ['Items'] * 1000
equips = pd.DataFrame()
equips['type'] = [None] * 1000
equips['id'] = [None] * 1000
equips['name'] = [None] * 1000
equips['count'] = [1] * 1000
equips['category'] = ['Equipment'] * 1000

filename = askopenfilename()

with open(filename, mode='rb') as file:
    for i in range(1000):
        offset = offsets[0] + i * 4
        file.seek(offset)
        items.iloc[i,1] = struct.unpack('H', file.read(2))[0]

        offset = offsets[1] + i * 4
        file.seek(offset)
        items.iloc[i,3] = struct.unpack('H', file.read(2))[0]
    
    for i in range(1000):
        offset = offsets[2] + i * 16
        file.seek(offset)
        equips.iloc[i,0] = struct.unpack('B', file.read(1))[0]

        offset = offsets[3] + i * 16
        file.seek(offset)
        equips.iloc[i,1] = struct.unpack('H', file.read(2))[0]


inv = pd.concat([items, equips], axis=0)
inv = inv[(inv['id'] != 0) | ((inv['type'] != 0) & (inv['type'] != 255))]
inv = inv.groupby([inv['type'],inv['id'],inv['category']], sort=False).aggregate({'name': 'first', 'count': 'sum'})
inv.to_csv('inventory/mh3u.csv')