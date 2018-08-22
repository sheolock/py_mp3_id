# encoding=utf8
import eyed3
import os
import shutil

from eyed3.compat import unicode

path = "G:\\Music\\Albums\\Mai Kuraki"  # Audiofiles' path
os.chdir(path)
files = os.listdir(path)
s = []
for file in files:
    filepath = os.path.join(path, file)
    if os.path.isfile(filepath):  # ignore folders and other files
        if os.path.splitext(filepath)[-1] == ".mp3":
            s.append(file)
        else:
            pass

print(os.getcwd())
for file in s:
    filepath = os.path.join(path, file)
    eyed3.LOCAL_ENCODING = 'UTF-8'
    audiofile = eyed3.load(filepath)
    try:
        album = audiofile.tag.album

        albumfolder = os.path.join(path, album)
        if not album == "":
            if os.path.exists(albumfolder) and os.path.isdir(albumfolder):
                # shutil.move(file, album)
                pass
            else:
                try:
                    os.mkdir(str.replace(album, "/", " "))
                except FileExistsError:
                    pass
                # shutil.move(file, album)
    except AttributeError:
        print("skip " + file)
        pass
# audiofile.tag.artist = u"Integrity"
# audiofile.tag.album = u"Humanity Is The Devil"
# audiofile.tag.album_artist = u"Integrity"
# audiofile.tag.title = u"Hollow"
# audiofile.tag.track_num = 2
