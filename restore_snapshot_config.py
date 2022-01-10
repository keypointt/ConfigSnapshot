from shutil import copyfile
from shutil import copytree
from time import sleep

from constants import source_config_folder_list, source_config_file_list
import sys

path_to_be_restored_folder = sys.argv[1]
print("Path to the target snapshot to be restored: " + path_to_be_restored_folder)

# whole folder
with open(source_config_folder_list) as file:
    lines = file.readlines()
    for original_src in lines:
        original_src = original_src.rstrip()
        restore_from = path_to_be_restored_folder + "/" + original_src.split("/")[-1]

        print("restore config snapshot. from: " + restore_from + ", to: " + original_src)
        # suppose to overwrite existing, so set to True
        copytree(restore_from, original_src, dirs_exist_ok=True)


# single files
with open(source_config_file_list) as file:
    lines = file.readlines()
    for original_src in lines:
        original_src = original_src.rstrip()
        restore_from = path_to_be_restored_folder + "/" + original_src.split("/")[-1]

        print("restore config snapshot. from: " + restore_from + ", to: " + original_src)
        copyfile(restore_from, original_src)
