from os import listdir, rename, getcwd, chdir
from os.path import isfile, join
from string import translate
# removes all numbers from filenames using the os and string library


onlyfiles = [ f for f in listdir("/home/austinchowong/Documents/Pythonfiles/50pictures/prank")
              if isfile(join("/home/austinchowong/Documents/Pythonfiles/50pictures/prank", f)) ]


def rename_files():
    chdir("/home/austinchowong/Documents/Pythonfiles/50pictures/prank")
    for f in onlyfiles:
        renamed_string = f.translate(None, "1234567890")
        rename(f, renamed_string)
        print renamed_string
        saved_path = getcwd()
        print saved_path
rename_files()
