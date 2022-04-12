import os
import sys
import pandas as pd
import warnings
from scripts.decryption import decrypt
from scripts.inventory import gather
from scripts.merge import merge

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(os.path.dirname(sys.argv[0]))

saveslot = int(input('Enter the save slot number (1,2,3) : '))

decrypt(saveslot)
gather()
merge()