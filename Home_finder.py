# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 22:18:12 2021

@author: harsi
"""

import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

seed=3**45+1
df=[]
df.append(seed)
def find(num):
    # code logic here
    if num%2 == 0:
        numtype="even"
    else:
        numtype = "odd"
    return numtype

while seed!=1:
    if find(seed) == 'odd':
        seed=3*seed+1
    if find(seed) == 'even':
        seed=seed/2
    df.append(seed)
    
plt.plot(df)
print(df[-10:])    