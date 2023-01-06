import os
import sys
import pandas as pd
import warnings
from bitstring import BitArray
from tkinter import Tk
from tkinter.filedialog import askopenfilename

warnings.simplefilter(action='ignore', category=FutureWarning)
os.chdir(os.path.dirname(sys.argv[0]))

offset_hex = ['0x18CF14']
# 5463 box length, 19 bits each item

Tk().withdraw()
filename = askopenfilename()

with open(filename, mode='rb') as file:
    offset = int(offset_hex[0], 16)
    file.seek(offset)
    item_box = file.read(1)
    print(BitArray(hex=str(item_box)).bin)