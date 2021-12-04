# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 14:36:48 2021

@author: gianm
"""

#%% required libraries
from os import listdir
from os.path import isfile, join
from os import chdir
import xml.etree.ElementTree as ET

import pandas as pd 
from dfply import *

from shutil import copyfile

#%% read all files in directory folder
def get_files(directory, file_ext):
    #directory = r"E:\Kuliah\Proyek Data Science\#_PROYEK\Retinanet-Tutorial\Dataset_2\JPEGImages"
    files = [f for f in listdir(directory) if f.endswith(file_ext)]
    return files

#%%
path = 'Dataset\\Sedan\\'
path_xml = path + 'Annotations\\'
path_jpeg = path + 'JPEGImages\\'
xmls = get_files(path_xml, '.xml')

#%%
xml_dict = dict()
for i in xmls:
    class_counter = {'sedan' : 0,
                     'motor' : 0,
                     'mobil' : 0}
    xml = ET.parse(path_xml+i).getroot()
    for x in xml.findall('object'):
        if x.find('name').text == 'sedan':
            class_counter['sedan'] = class_counter['sedan'] + 1
        elif x.find('name').text == 'mobil':
            class_counter['mobil'] = class_counter['mobil'] + 1
        elif x.find('name').text == 'motor':
            class_counter['motor'] = class_counter['motor'] + 1
    xml_dict[i] = class_counter
    
#%% 
key_list = list(xml_dict.keys())
sedan_list = [xml_dict[x]['sedan'] for x in key_list]
mobil_list = [xml_dict[x]['mobil'] for x in key_list]
motor_list = [xml_dict[x]['motor'] for x in key_list]

#%%
df_xml = pd.DataFrame()
df_xml['xml'] = key_list
df_xml['sedan'] = sedan_list
df_xml['mobil'] = mobil_list
df_xml['motor'] = motor_list

df_summ = (df_xml
           >> summarize(total_sedan=X.sedan.sum(), total_mobil=X.mobil.sum(), total_motor=X.motor.sum()))

#%%
contain_sedan = (df_xml
                  >> filter_by(X.sedan != 0)
                  >> select(X.xml))

sedan_filenames = [f[0:-4] for f in contain_sedan['xml']]

#%%
for i in sedan_filenames:
    copyfile(path_xml+i+'.xml', 'Sedan\\Annotations\\'+i+'.xml')
    
for i in sedan_filenames:
    copyfile(path_jpeg+i+'.jpg', 'Sedan\\JPEGImages\\'+i+'.jpg')

