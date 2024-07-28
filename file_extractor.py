import glob
import os
import zipfile
from pathlib import Path

# Path where you download or store the file you wish to extract.
p = Path('C:\\Users\\freak\\Downloads')

# Directory where the game stores its mods.
directory = 'D:\\World_of_Tanks_EU\\mods\\'

# Finds the folder with the latest update.
newest_patch = max(glob.glob(os.path.join(directory, '*/')), key=os.path.getmtime)

# Iterates over the path and looks for the specified file type.
for f in p.glob('*.zip'):
    with zipfile.ZipFile(f, 'r') as archive:
        archive.extractall(path=newest_patch)
        print('Enjoy your modded gaming experience.')
