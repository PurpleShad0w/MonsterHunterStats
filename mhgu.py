import os
import sys
import pandas as pd
import warnings
from tkinter.filedialog import askopenfilename

warnings.simplefilter(action='ignore', category=FutureWarning)
os.chdir(os.path.dirname(sys.argv[0]))

offsets = [1625876]
items = pd.DataFrame()
items['id'] = [None] * 2300
items['name'] = [None] * 2300
items['count'] = [None] * 2300
dict_items = pd.read_csv('dicts/mhgu/items.csv')

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
        items.iloc[i,0] = int(id, 2)
        items.iloc[i,2] = int(count, 2)
        if items.iloc[i,0] == 0:
            continue
        items.iloc[i,1] = dict_items.loc[dict_items['_id'] == items.iloc[i,0], 'name'].iloc[0]


items.to_csv('inv/mhgu.csv')