import os,shutil

srcdir = "/storage/emulated/0/Music"
destdir = "/storage/emulated/0/Music"
a = os.walk(srcdir)

for i in a:
    if (i[0] == destdir):
        print("same as dest")
        continue

    b = i[2]
    for j in b:
        if (j.endswith(".mp3")):
            src = os.path.join(i[0],j)
            print(f"moving : " + src)
            shutil.move(src,destdir)
