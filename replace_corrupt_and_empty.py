import sys, os, PyPDF2, time
from PIL import Image

corrupt_list='/Users/kevindonovan/Desktop/Back_Consolidation/scan_SUBPAR/results_corrupt_finder_20200927_162448/corrupted_images.txt'
empty_list='/Users/kevindonovan/Desktop/Back_Consolidation/scan_SUBPAR/results_corrupt_finder_20200927_162448/empty_images.txt'

backups = ['/Users/kevindonovan/Dropbox (MIT)/Pictures KJD']

tS = time.time()
timeS = time.strftime('%X %x %Z')

#Read corrupt and empty file lists
cfile=open(corrupt_list,"r")
efile=open(empty_list,"r")
clist=cfile.readlines()
elist=efile.readlines()

print(clist[1])

for cpath in clist:
    c=cpath.rstrip()
    splitdir=os.path.split(c)
    filename=os.path.basename(c)
    parentdir=os.path.dirname(c)
    print('Next path:')
    print(c)
    print(splitdir)
    print(filename)
    print(parentdir)
    