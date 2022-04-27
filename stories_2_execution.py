import os
import sys
import pandas as pd
import warnings
from scripts.stories_2_decryption import decode
from scripts.stories_2_inventory import gather
from scripts.stories_2_merge import merge

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(os.path.dirname(sys.argv[0]))

decode()
gather()
merge()