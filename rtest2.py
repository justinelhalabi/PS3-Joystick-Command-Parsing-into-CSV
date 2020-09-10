# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 11:36:47 2020
@author: Majd Awar - Justin Elhalabi
"""
import yaml
import pandas as pd
import os
import numpy as np
from matplotlib import pyplot as plt
import csv
from keras.preprocessing.sequence import pad_sequences

def yaml_as_python(val):
    """Convert YAML to dict"""
    try:
        return yaml.safe_load_all(val)
    except yaml.YAMLError as exc:
        return exc


rootdir = r"CHANGE DIRECOTRY HERE"  #CHANGE DIRECTORY TO A FOLDER THAT INCLUDES CSV FILES
df = pd.DataFrame({'secs': [], 'a':[], 'b':[], 'c':[]})


for file in os.listdir(rootdir):
    name = os.path.basename(file)
           
    try:
        results = pd.read_csv(rootdir + '/' + name)
        df = df.append(results)
        # for value in results:
        #       df2 = pd.DataFrame({'secs': [value['header']['stamp']['secs']], 'a':[value['axes'][0]], 'b':[value['axes'][1]]})
        #       df = df.append(df2, ignore_index=True)
        #       #print(df)
    except Exception as e:
        print("EOF:" + str(e))
count = 0
size = 90
seconds = 6 #set by user
vectors = []
vector = []
counts = []
sample_second = 0
start_second = 0
for index, row in df.iterrows():
    if (row['a'] !=0 and row['b'] !=0) and row['tri']==0 and row['cir']==0 and row['X']==0 and row['squ']==0:       
        sample_second = row['secs']
        if count == 0:
            start_second = sample_second #where the samples started recording samples
        if sample_second - start_second < seconds: #stores all samples belonging to one sample into a list
            vector.append([row['a'], row['b'], row['c']])
            count = count + 1
        #print(row['a'], row['b'])        
    else:
        if count > 0:
            if count >= size:
                vectors.append(vector[0:size]) #size is subject to change (do several trials)
            # elif count > 50: #Minimum size #USE THIS IF PADDING
            #     padding = [[0,0,0]]*(size - count)
            #     temp = vector[0:size]
            #     temp.extend(padding)
            #     vectors.append(temp)
            vector = []
            sample_second = 0
            counts.append(count)
            count = 0

print(len(vectors))
#%%
with open(r"NAME_OF_NEW_FILE.cvs", 'a', newline='') as myfile:  #CHANGE NAME OF NEW GERNEATED CSV FILE WITH VELOCITY COMMANDS AS ARRAYS
      wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
      for seq in vectors[0:400]:
          wr.writerow(seq + [1])
     
   #%% 


print("Vectors: ", vectors)
print("Samples: ", len(counts))
print("min size: ", min(counts))
print("max size: ", max(counts))
print("Mean: ", np.mean(counts))
print("Median: ", np.median(counts))
print("Deviation: ", np.std(counts))

plt.xlim([min(counts)-5, max(counts)+5])
bins = np.arange(0, 225, 5)
plt.hist(counts, bins=bins, alpha=0.5)
plt.title('TITLE_OF_GRAPH')                       #CHANGE TITLE OF GRAPH
plt.xlabel('Sample Sizes (bin size = 5)')
plt.ylabel('count')

plt.show()
    
    



