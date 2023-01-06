import os
import sys
import pandas as pd
import warnings
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from argparse import Namespace
import mhef.n3ds
import struct

warnings.simplefilter(action='ignore', category=FutureWarning)
os.chdir(os.path.dirname(sys.argv[0]))

offsets = [350, 352]
items = pd.DataFrame()
items['id'] = [None] * 1400
items['name'] = [None] * 1400
items['count'] = [None] * 1400
dict_items = pd.read_csv('dicts/mh4u_items.csv')

# Tk().withdraw()
filename = askopenfilename()

args = Namespace(mode='d', inputfile=filename, outputfile='saves/MH4U_user.bin')
sc = mhef.n3ds.SavedataCipher(mhef.n3ds.MH4G_NA)
sc.decrypt_file(args.inputfile, args.outputfile)

with open('saves/MH4U_user.bin', mode='rb') as file:
    for i in range(1400):
        offset = offsets[0] + i * 4
        file.seek(offset)
        items.iloc[i,0] = struct.unpack('H', file.read(2))[0]
        items.iloc[i,1] = dict_items.loc[dict_items['ID'] == items.iloc[i,0], 'Name'].iloc[0]
    
    for i in range(1400):
        offset = offsets[1] + i * 4
        file.seek(offset)
        items.iloc[i,2] = struct.unpack('H', file.read(2))[0]

items.to_csv('inv/items.csv', index=False)