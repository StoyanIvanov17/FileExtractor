import os
import zipfile
from pathlib import Path

# Path where you download or store the file you wish to extract.
p = Path('C:\\Users\\freak\\Downloads')

# Directory where the game stores its mods.
directory = 'D:\\World_of_Tanks_EU\\mods\\'

# Finds the latest patch folder.
needed_folder = ""
for folder in os.listdir(directory):
    if folder != 'configs':
        needed_folder = folder

# Iterates over the path and looks for the specified file type.
for f in p.glob('*.zip'):
    with zipfile.ZipFile(f, 'r') as archive:
        archive.extractall(path=directory + needed_folder)
        print('Enjoy your modded gaming experience.')
