import os
import sys
import pandas as pd
import warnings
from scripts.MHWI_decryption import decrypt
from scripts.MHWI_inventory import gather
from scripts.MHWI_merge import merge

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(os.path.dirname(sys.argv[0]))

# saveslot = int(input('Enter the save slot number (1,2,3) : '))
saveslot = 1

decrypt(saveslot)
gather()
merge()