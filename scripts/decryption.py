import os
import sys
import subprocess
import pandas as pd

os.chdir(os.path.dirname(sys.argv[0]))

saveslot = 1

def decrypt(saveslot):
    # Remove save file encryption
    subprocess.call("java -jar res/lib/IceborneSavecrypt.jar SAVEDATA1000 SAVEDATA1000.bin")
    
    # Decode the binary file
    subprocess.call("C:/Program Files/010 Editor/010Editor.exe SAVEDATA1000.bin -template:res/mapping/SAVEDATA1000.bt -script:scripts/editor.1sc -noui")
    
    # Load the file
    df = pd.read_csv('SAVEDATA1000_full.csv')
    df.set_index('Name', inplace=True)

    # Select and save the useful part
    index_save = df.index.get_loc('struct mhw_save_slot saves['+str(saveslot-1)+']')
    df_save = df.iloc[index_save:index_save+1343604]
    df_save.reset_index(inplace=True)
    df_save.to_csv(r'SAVEDATA1000.csv',index=False)

    # Remove the useless file
    os.remove('SAVEDATA1000_full.csv')