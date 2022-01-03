# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 15:16:40 2021

@author: gianm
"""

#%% required libraries
from os import chdir, rename
from os import listdir
from os.path import isfile, join
import random
import argparse

#%% read all files in directory folder
def get_files(directory, file_ext):
    #directory = r"E:\Kuliah\Proyek Data Science\#_PROYEK\Retinanet-Tutorial\xml"
    #file_ext = '.xml'
    files = [f for f in listdir(directory) if f.endswith(file_ext)]
    return files


#%% rename all
def rename_files(files, file_ext, file_name, start):
    name = int(start)
    count = 0
    for f in files:
        rename(f, file_name+'{i}{j}'.format(i=name, j=file_ext))
        name = name + 1
        count += 1
    return count

#%%
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='batch rename.')
    parser.add_argument('--dir', help='file dir', default=None)
    parser.add_argument('--ext', help='file extension', default=None)
    parser.add_argument('--name', help='renamed file name', default='img')
    parser.add_argument('--start', help='starting number', default=1)

    args = parser.parse_args()
     
    directory = args.dir
    file_ext = args.ext 
    file_name = args.name
    start = args.start

    print('Directory:', directory)
    print('File extension:', file_ext)

    files = get_files(directory, file_ext)
    print('Found {f} file(s) with {e} extension'.format(f=len(files), e=file_ext))
    chdir(directory)
    print('Renamed {} file(s)'.format(rename_files(files, file_ext, file_name, start)))
    