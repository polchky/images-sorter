import os
from PIL import Image
path = './albums/'
bignumber = 2000
maxsize = 1600

def rename(path):
    files = os.listdir(path)
    name = path.split('/')[-1]
    if name[0] == "_" :
        name = name[1:]
    i = 0
    keeps = []
    
    for file in files:
        base = file.split('.')[0]
        index = base.split('_')[-1]
        index = int(index) if index.isdigit() else False
        if file.startswith(name) and index and index < bignumber and index > 0:
            keeps.append(file)
            index = int(index)
            i = index if index > i else i
    
    i = i+1

    for file in sorted(files):
        if file in keeps:
            print("skipping file : %s" % file)
            continue
        ext = os.path.splitext(file)[1]
        oldname = os.path.join(path, file)
        newname =  os.path.join(path, "%s_%0.3d%s" % (name, i, ext))
        os.rename(oldname, newname)
        i = i+1
        
        img = Image.open(newname)
        ratio = float(maxsize) / max(img.size[0], img.size[1])
        if ratio < 1:
            print("resizing image")
            img = img.resize((int(img.size[0] * ratio), int(img.size[1] * ratio)), Image.ANTIALIAS)
            img.save(newname)
    



folders = sorted(os.listdir(path))
maximum = 0
for folder in folders:
    if folder[0:3].isdigit():
        print("skipping folder %s" % folder)
        maximum = max(maximum, int(folder[0:3]))
    elif folder[0:2] == "__":
        print("skipping folder %s" % folder)
    elif folder[0:1] == "_":
        rename(os.path.join(path, folder))
        os.rename(os.path.join(path, folder), os.path.join(path, "_%s" % (folder)))
    else:
        maximum = maximum + 1
        rename(os.path.join(path, folder))
        os.rename(os.path.join(path, folder), os.path.join(path, "%0.3d_%s" % (maximum, folder)))
