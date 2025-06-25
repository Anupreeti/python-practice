import os
import argparse
import logging
import shutil

logging.basicConfig(level=logging.INFO, format = '%(levelname)s - %(message)s')

parser = argparse.ArgumentParser(description="Check Disk uage of directory")
parser.add_argument("path", help="Directory to check")
args = parser.parse_args()

if not os.path.exists(args.path):
    logging.error("Path Doesn't exist!")
else:
    total, used, free = shutil.disk_usage(args.path)
    logging.info(f"Disk usage for {args.path}:")
    print(f"Total : {total//2**30} GB")
    print(f"Used : {used // 2**30} GB")
    print(f"Free : {free //2**30} GB")
