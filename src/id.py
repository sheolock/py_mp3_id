# encoding=utf8
import eyed3
import os
import shutil

path = "G:\Music"  # Audiofiles' path
os.chdir(path)
files = os.listdir(path)
s = []
for file in files:
    filepath = os.path.join(path, file)
    if os.path.isfile(filepath):  # ignore folders and other files
        if os.path.splitext(filepath)[-1].lower() == ".mp3":
            s.append(file)
        else:
            pass

print(os.getcwd())
for file in s:
    print("Current file:" + file)
    os.rename(file, "temp.mp3")  # because eyed3 cannot load file path with japanese characters
    filepath = os.path.join(path, "temp.mp3")
    eyed3.LOCAL_ENCODING = 'UTF-8'
    audiofile = eyed3.load(filepath)
    try:
        album = audiofile.tag.album
        if album is not None and not album == "":
            for character in ["\\", "/", ":", "*", "?", "\"", "<", ">", "|"]:
                album = album.replace(character, " ")
            album = str.strip(album.strip("."))
            albumfolder = os.path.join(path, album)
            if os.path.exists(albumfolder) and os.path.isdir(albumfolder):
                os.rename("temp.mp3", file)
                shutil.move(file, album)
                pass
            else:
                try:
                    os.mkdir(str.replace(album, "/", " "))
                except FileExistsError:
                    pass
                os.rename("temp.mp3", file)
                shutil.move(file, album)
        else:
            print("skip file " + file + " since there's no album")
            os.rename("temp.mp3", file)
    except AttributeError:
        print("skip " + file)
        pass

# audiofile.tag.artist = u"Integrity"
# audiofile.tag.album = u"Humanity Is The Devil"
# audiofile.tag.album_artist = u"Integrity"
# audiofile.tag.title = u"Hollow"
# audiofile.tag.track_num = 2
