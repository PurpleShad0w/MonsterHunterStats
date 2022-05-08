from argparse import Namespace
import mhef.n3ds

args = Namespace(mode='d', inputfile='MH4U_user', outputfile='MH4U_user.bin')

sc = mhef.n3ds.SavedataCipher(mhef.n3ds.MH4G_NA)
sc.decrypt_file(args.inputfile, args.outputfile)