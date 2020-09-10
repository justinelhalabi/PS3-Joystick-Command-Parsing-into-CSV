# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 11:36:47 2020

@author: Majd Awar - Justin Elhalabi
"""
import os
import yaml
import pandas as pd

def yaml_as_python(val):
    """Convert YAML to dict"""
    try:
        return yaml.safe_load_all(val)
    except yaml.YAMLError as exc:
        return exc



with open(r'CHANGE_DIRECTORY_HERE.YAML') as file:    #CHANGE DIRECTORY FOR YAML FILE HERE
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    try:
        results = yaml_as_python(file)
        df = pd.DataFrame({'secs': [], 'a':[], 'b':[], 'c':[]})
        print (results)
        for value in results:
              df2 = pd.DataFrame({'secs': [float(value['header']['stamp']['secs'] + float(value['header']['stamp']['nsecs'])/10**9)], 'a':[value['axes'][0]], 'b':[value['axes'][1]], 'c':[value['axes'][3]], 'tri':[value['buttons'][2]], 'cir':[value['buttons'][1]], 'X':[value['buttons'][0]], 'squ':[value['buttons'][3]]})
              df = df.append(df2, ignore_index=True)
    except:
        print("EOF")

df.to_csv('NAME_OF_NEW_FILE.csv', index=False)  #CHANGE NAME OF NEW GENERATED CSV FILE

