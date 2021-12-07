# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 08:33:55 2021

@author: gianm
"""
#%% required libraries
from os import listdir
from os.path import isfile, join
from os import chdir
import random
import argparse
import sys

#%% read all files in directory folder
def get_files(directory, file_ext):
    #directory = r"E:\Kuliah\Proyek Data Science\#_PROYEK\Retinanet-Tutorial\Dataset_2\JPEGImages"
    files = [f[0:-4] for f in listdir(directory) if f.endswith(file_ext)]
    return files

#%% split data into train & test
def split_dataset(files, ratio):
    random.shuffle(files)

    train_ratio = ratio
    train_len = int(len(files) * train_ratio)

    train = files[:train_len]
    val = files[train_len:]
    return train, val

def create_imagesets(files, train, val):
    #create train.txt
    with open('train.txt', 'w') as writefile:
        for i in train:
            writefile.write(i + '\n')
        print('created train.txt')

    #create test.txt
    with open('val.txt', 'w') as writefile:
        for i in val:
            writefile.write(i + '\n')
        print('created val.txt')
            
    #create trainval.txt
    with open('trainval.txt', 'w') as writefile:
        for i in files:
            writefile.write(i + '\n')
        print('created trainval.txt')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='batch rename.')
    parser.add_argument('--dir', help='file dir', default=None)
    parser.add_argument('--ext', help='file extension', default='.jpg')
    parser.add_argument('--ratio', help='train ratio', default=0.7)
    
    args = parser.parse_args()

    directory = args.dir
    file_ext = args.ext
    ratio = float(args.ratio)

    print('Directory:', directory)
    print('File extension:', file_ext)
    print('Train ratio:', ratio)

    files = get_files(directory, file_ext)
    print('Found {f} file(s) with {e} extension'.format(f=len(files), e=file_ext))

    train, val = split_dataset(files, ratio)
    print('{} file(s) for training'.format(len(train)))
    print('{} file(s) for validation'.format(len(val)))

    chdir(directory)
    create_imagesets(files, train, val)

