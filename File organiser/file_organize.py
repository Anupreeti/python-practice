import os
import shutil
import argparse

def organize(folder):
    if os.path.isdir(folder):
        file = os.listdir(folder)
        moved = False
        for f in file:
            extension = os.path.splitext(f)[1]
            dest_dir = ""
            if os.path.isdir(os.path.join(folder, f)):
                continue  # Skip directories
            if extension in [".docx", ".pdf"]:
                print(f"File {f} moved to document folder")
                dest_dir = "Documents"
            elif extension in [".py"]:
                print(f"File {f} moved to Python folder")
                dest_dir = "Python"
            elif extension in [".jpg", ".png"]:
                print(f"File {f} moved to Images folder")
                dest_dir = "Images"
            else:
                dest_dir = "Others"
                print(f"File {f} moved to Others folder")
            if dest_dir:
                os.makedirs(os.path.join(folder, dest_dir), exist_ok=True)
                try:
                    shutil.move(os.path.join(folder,f), os.path.join(folder,dest_dir,f))
                    moved = True
                except Exception as e:
                    print("Error moving file: ", e)
        if not moved:
            print("No Files to move")
    else:
        print("Folder don't exist")

parser = argparse.ArgumentParser(description="Organizing files")
parser.add_argument("--path", type=str, help="The folder path which we need to organize")
args=parser.parse_args()

if args.path:
    print(args.path)
    organize(args.path)
else:
    print("Please enter the path of the folder you want to organize")
