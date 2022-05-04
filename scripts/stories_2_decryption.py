import os
import sys
import subprocess
import pandas as pd

os.chdir(os.path.dirname(sys.argv[0]))

def decode():
    # Decode the binary file
    subprocess.call("C:/Program Files/010 Editor/010Editor.exe saves/mhr_slot_1.bin -template:templates/MHStories2_SaveTemplate.bt -script:scripts/stories_2_editor.1sc -noui")

    # Load the file and drop useless columns
    df = pd.read_csv('saves/mhr_slot.csv')
    df.drop(['Start','Size','Color','Comment'], axis=1, inplace=True)

    # Export save
    df.to_csv(r'saves/mhr_slot.csv',index=False)