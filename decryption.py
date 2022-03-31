import os
import sys
import subprocess
import pandas as pd

os.chdir(os.path.dirname(sys.argv[0]))

saveslot = 1

subprocess.call("java -jar IceborneSavecrypt.jar SAVEDATA1000 SAVEDATA1000.bin")

subprocess.call("C:/Program Files/010 Editor/010Editor.exe SAVEDATA1000.bin -template:SAVEDATA1000.bt -script:editor_script.1sc -noui")

df = pd.read_csv('SAVEDATA1000_full.csv')
df.set_index('Name', inplace=True)

index_save = df.index.get_loc('struct mhw_save_slot saves['+str(saveslot-1)+']')
df_save = df.iloc[index_save:index_save+1343604]
df_save.reset_index(inplace=True)
df_save.to_csv(r'SAVEDATA1000.csv',index=False)

os.remove('SAVEDATA1000_full.csv')