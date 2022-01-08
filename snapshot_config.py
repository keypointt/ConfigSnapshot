from datetime import datetime
from shutil import copyfile
from shutil import copytree
import os

### Todo: set below values
custom_description = "_alb_us_west_1"
root_dir = "/home/xin/config_backup/"

### create folder name with timestamp
today = datetime.now()
snapshot_dir = root_dir + today.strftime('%Y%m%d%H%M%S')
snapshot_dir = snapshot_dir + custom_description

if not os.path.exists(snapshot_dir):
    os.makedirs(snapshot_dir)


# whole folder
with open("./config_folder_list") as file:
    lines = file.readlines()
    for src in lines:
        src = src.rstrip()
        dst = snapshot_dir + "/" + src.split("/")[-1]
        print(src)
        print(dst)

        # set to false to avoid overwrite existing snapshot
        # but if above date format is to seconds, then here it does not matter
        copytree(src, dst, dirs_exist_ok=False)


# single files
with open("./config_file_list") as file:
    lines = file.readlines()
    for src in lines:
        src = src.rstrip()
        dst = snapshot_dir + "/" + src.split("/")[-1]
        print(src)
        print(dst)
        copyfile(src, dst)
