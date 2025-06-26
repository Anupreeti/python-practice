import argparse
import os
from datetime import datetime
import logging

logging.basicConfig(filename="app.log", level=logging.INFO, format='%(asctime)s-%(levelname)s-%(message)s')

def create_folder(folder):
    try:
        os.makedirs(folder, exist_ok=True)
        logging.info("Folder created")
        time_now = datetime.now().strftime('%Y%m%d%H%M')
        files = ["main.py","README.md","notes.txt"]
        for file in files:
            with open(f"{folder}/{file}","w") as f:
                f.write(f"#Current time = {time_now}")
                logging.info(f"file Created {file}")
        os.rename(f"{folder}/notes.txt", f"{folder}/logs.txt")
        logging.info("notes.txt File is renamed to logs.txt")
    except Exception as e:
        print(f"Error: {e}")
        logging.exception(e)

def delete_folder(folder):
    try:
        files = os.listdir(folder)
        for file in files:
            os.remove(f"{folder}/{file}")
        os.rmdir(folder)
        logging.info(f"Folder deleted : {folder}")
    except Exception as e:
        logging.exception(e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a folder with base files")
    parser.add_argument("--folder", required=False, help = "name of the folder to create")
    parser.add_argument("--delete", required=False, help="name of the folder to be deleted")
    args = parser.parse_args()
    if args.folder:
        create_folder(args.folder)
    if args.delete:
        delete_folder(args.delete)
