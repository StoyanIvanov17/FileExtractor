# Mod_Zipper

Short python script that allows us to extract files in our desired directory with some specific requirements.

However, this script is mainly aimed at a game called 'World of Tanks'. 
The game has an innacurate gun reticle and the community has designed a mod that replaces that broken reticle with a properly working one.
Since the game has somewhat frequent updates, the mod has to be manually downloaded and extracted into a last folder of the game's mod directory:
As long as we have the mod downloaded, we can simply run the script and it will find the zip file in the directory that we have specified.
Then the script will find the latest folder by taking the time it has been created at and unzip our files into it.
