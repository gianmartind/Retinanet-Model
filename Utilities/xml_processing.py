# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 14:36:48 2021

@author: gianm
"""

#%% required libraries
from os import listdir
import xml.etree.ElementTree as ET

import pandas as pd 
import argparse

from shutil import copyfile

#%% read all files in directory folder
def get_files(directory, file_ext='.xml'):
    #directory = r"E:\Kuliah\Proyek Data Science\#_PROYEK\Retinanet-Tutorial\Dataset_2\JPEGImages"
    files = [f for f in listdir(directory) if f.endswith(file_ext)]
    return files, directory

def get_xml_dict(xmls, path_xml):
    xml_dict = dict()
    for i in xmls:
        class_count = dict()
        xml = ET.parse(path_xml+i).getroot()
        for x in xml.findall('object'):
            class_name = x.find('name').text
            if class_name not in class_count.keys():
                class_count[class_name] = 1
            else:
                class_count[class_name] = class_count[class_name] + 1
        xml_dict[i] = class_count
    return xml_dict

def get_class_set(xml_dict):
    class_set = set()
    for key, item in xml_dict.items():
        for k in item.keys():
            class_set.add(k)
    return class_set

def get_class_count(directory):
    df_xml = pd.DataFrame(columns=['xml'])
    
    xmls_directory = get_files(directory)
    xmls = xmls_directory[0]
    directory = xmls_directory[1]
    
    xml_dict = get_xml_dict(xmls ,directory)
    class_set = get_class_set(xml_dict)
    
    for i in class_set:
        df_xml[i] = list()
    
    for key, val in xml_dict.items():
        to_append = val
        to_append['xml'] = key
        df_xml = df_xml.append(to_append, ignore_index=True)
    
    df_xml = df_xml.fillna(0)
    
    return df_xml

#%%
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='class count')
    parser.add_argument('--dir', help='file dir', default=None)
    parser.add_argument('--filename', help='file name', default='class_count')
    
    args = parser.parse_args()
    directory = args.dir
    filename = args.filename
    
    print('Directory:', directory)

    if directory[-1] != '/':
        directory = directory + '/'
        
    xml_class_count = get_class_count(directory)
    xml_class_count.to_csv(filename+'.csv', index=False)
    print('{} generated.'.format('\'' + filename+'.csv\''))


