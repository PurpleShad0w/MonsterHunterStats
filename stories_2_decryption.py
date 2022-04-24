import os
import sys
import subprocess
import pandas as pd

os.chdir(os.path.dirname(sys.argv[0]))

# Decode the binary file
subprocess.call("C:/Program Files/010 Editor/010Editor.exe mhr_slot_1.bin -template:res/mapping/MonstieEgger.bt -script:scripts/stories_2_editor.1sc -noui")

# Load the file and drop useless columns
df = pd.read_csv('mhr_slot.csv')
df.drop(['Start','Size','Color','Comment'], axis=1, inplace=True)

# Export save
df.to_csv(r'mhr_slot.csv',index=False)