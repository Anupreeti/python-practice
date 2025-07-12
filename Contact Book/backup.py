import argparse
import os
import shutil
from datetime import datetime

def backup(file):
    os.makedirs("backups", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = f"contacts_backup_{timestamp}.json"
    try:
        if os.path.exists(file):
            shutil.copy(file, f"backups/{backup}")
        else:
            print("File don't exists")
    except Exception as e:
        print("Error", e)

parser = argparse.ArgumentParser(description="Backup done manually")
parser.add_argument("--file", help="Mentione the file name to create backup")
args=parser.parse_args()

if args.file:
    backup(args.file)
else:
    print("please mentine file name to create backup")
