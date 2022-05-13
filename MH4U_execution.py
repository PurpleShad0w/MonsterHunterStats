import os
import sys
import pandas as pd
import warnings
from scripts.MH4U_decryption import decode
from scripts.MH4U_inventory import gather
from scripts.MH4U_merge import merge

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(os.path.dirname(sys.argv[0]))

decode()
gather()
merge()