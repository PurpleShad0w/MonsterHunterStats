import os
import sys
import subprocess
import pandas as pd
from argparse import Namespace
import mhef.n3ds

os.chdir(os.path.dirname(sys.argv[0]))

# Setup the decryption
args = Namespace(mode='d', inputfile='saves/MH4U_user', outputfile='saves/MH4U_user.bin')

# Decrypt the save file
sc = mhef.n3ds.SavedataCipher(mhef.n3ds.MH4G_NA)
sc.decrypt_file(args.inputfile, args.outputfile)

# Decode the binary file
subprocess.call("C:/Program Files/010 Editor/010Editor.exe saves/MH4U_user.bin -template:templates/MH4U_template.bt -script:scripts/MH4U_editor.1sc -noui")

# Load the file
df = pd.read_csv('saves/MH4U_user.csv')
df.drop(['Start','Size','Color','Comment'], axis=1, inplace=True)

# Export save
df.to_csv(r'saves/MH4U_user.csv',index=False)