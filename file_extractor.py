import os
import zipfile
from pathlib import Path

p = Path('C:\\Users\\freak\\Downloads')

directory = 'D:\\World_of_Tanks_EU\\mods\\'

needed_folder = ""
for folder in os.listdir(directory):
    if folder != 'configs':
        needed_folder = folder

for f in p.glob('*.zip'):
    with zipfile.ZipFile(f, 'r') as archive:
        archive.extractall(path=directory + needed_folder)
        print('Enjoy your modded gaming experience.')
