import os
import sys
import pandas as pd
import warnings
from tkinter.filedialog import askopenfilename
from argparse import Namespace
import mhef.n3ds
import struct

warnings.simplefilter(action='ignore', category=FutureWarning)
os.chdir(os.path.dirname(sys.argv[0]))

offsets = [350, 352, 5950, 5952, 47950, 47952]
items = pd.DataFrame()
items['type'] = [0] * 1400
items['id'] = [None] * 1400
items['name'] = [None] * 1400
items['count'] = [None] * 1400
items['category'] = ['Items'] * 1400
dict_items = pd.read_csv('database/mh4u/items.csv')
equips = pd.DataFrame()
equips['type'] = [None] * 1500
equips['id'] = [None] * 1500
equips['name'] = [None] * 1500
equips['count'] = [1] * 1500
equips['category'] = ['Equipment'] * 1500
palicos = pd.DataFrame()
palicos['type'] = [None] * 600
palicos['id'] = [None] * 600
palicos['name'] = [None] * 600
palicos['count'] = [1] * 600
palicos['category'] = ['Palico Equipment'] * 600

dict_equips = [[0],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

for i in range(20):
    with open('database/mh4u/equipment/'+str(i+1)+'.txt') as f:
        dict_equips[i+1] = [line.rstrip() for line in f]

filename = askopenfilename()

args = Namespace(mode='d', inputfile=filename, outputfile='saves/mh4u_user.bin')
sc = mhef.n3ds.SavedataCipher(mhef.n3ds.MH4G_NA)
sc.decrypt_file(args.inputfile, args.outputfile)

with open('saves/mh4u_user.bin', mode='rb') as file:
    for i in range(1400):
        offset = offsets[0] + i * 4
        file.seek(offset)
        items.iloc[i,1] = struct.unpack('H', file.read(2))[0]
        items.iloc[i,2] = dict_items.loc[dict_items['ID'] == items.iloc[i,1], 'Name'].iloc[0]

        offset = offsets[1] + i * 4
        file.seek(offset)
        items.iloc[i,3] = struct.unpack('H', file.read(2))[0]

    for i in range(1500):
        offset = offsets[2] + i * 28
        file.seek(offset)
        equips.iloc[i,0] = struct.unpack('B', file.read(1))[0]

        offset = offsets[3] + i * 28
        file.seek(offset)
        equips.iloc[i,1] = struct.unpack('H', file.read(2))[0]

        equips.iloc[i,2] = dict_equips[equips.iloc[i,0]][equips.iloc[i,1]]
    
    for i in range(600):
        offset = offsets[4] + i * 4
        file.seek(offset)
        palicos.iloc[i,0] = struct.unpack('H', file.read(2))[0]

        offset = offsets[5] + i * 4
        file.seek(offset)
        palicos.iloc[i,1] = struct.unpack('H', file.read(2))[0]
    

inv = pd.concat([items, equips, palicos], axis=0)
inv = inv[(inv['id'] != 0) | ((inv['type'] != 0) & (inv['type'] != 255))]
inv = inv.groupby([inv['type'],inv['id'],inv['category']], sort=False).aggregate({'name': 'first', 'count': 'sum'})
inv.to_csv('inventory/mh4u.csv')