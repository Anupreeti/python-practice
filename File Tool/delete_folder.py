import file_tool
import argparse

parser = argparse.ArgumentParser("Folder name to be deleted")
parser.add_argument("--delete", required = True, help = "name of the folder to be deleted")
args = parser.parse_args()
file_tool.delete_folder(args.delete)
