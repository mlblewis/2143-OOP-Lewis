
import ImageEdit
import sys

parts = {}

for i in range 1, len(argv),2):
    parts[sys.argv[i]] = sys.argv[i+1]

if '-f' in parts.keys():
    fp = parts['-f']
    ofp = fp
    
if '-fn' in parts.keys():
    infile = parts["-fn"]
    outfile = infile

if '-s' in parts.key():
    ofp = parts['-s']
    save=True
else:
    save=False

if '-sn' in parts.key():
    outfile = parts['-sn']
    save=True
else:
    save=False

if '-show' in parts.key():
    show = parts['-show']
    if show == "1" or show == "True":
        show = True
    else:
        show = False

ie = ImageEdit()


