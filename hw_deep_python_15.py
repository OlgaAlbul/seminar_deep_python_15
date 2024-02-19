import argparse
import os
import logging
from collections import namedtuple

logging.basicConfig(filename='directory_info.log', level=logging.INFO, format='%(asctime)s - %(message)s')

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'parent_directory'])
FolderInfo = namedtuple('FolderInfo', ['dir_name', 'parent_dir'])


def get_directory_info():
    parser = argparse.ArgumentParser(description='getting path  from console')
    parser.add_argument('directory_path', type=str,
                        help='enter path to file or directory ')
    args = parser.parse_args()
    files_info = []

    for root, dirs, files in os.walk(args.directory_path):
        for file in files:
            file_name, extension = os.path.splitext(file)
            parent_dir = root.split('/')[-1]
            file = FileInfo(extension, file_name, parent_dir)
            files_info.append(file)
            logging.info(file)
        for dir_ in dirs:
            path = os.path.join(root, dir_)
            dir_name = dir_
            parent_dir = root.split('/')[-1]
            folder = FolderInfo(dir_name, parent_dir)
            files_info.append(folder)
            logging.info(folder)
        return files_info


get_directory_info()




