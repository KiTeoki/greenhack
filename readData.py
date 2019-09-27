#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 15:12:02 2018

@author: luhao
"""

'''read csv file'''

import pandas as pd

def remove_whitespace(x):
    """
    Helper function to remove any blank space from a string
    x: a string
    """
    try:
        # Remove spaces inside of the string
        x = "".join(x.split())

    except:
        pass
    return x



df = pd.read_csv('/Users/zhanghong/Documents/GitHub/greenhack/data/fish_ca_m_Data.csv')
df = df.set_index('TIME')
usefulCols = ['GEO', 'SPECIES', 'FISHREG','Value']
df = df[usefulCols]
df = df[df['Value'] != ':']
df = df[df['FISHREG'] == 'Total fishing areas']
df['Value'] = df['Value'].apply(remove_whitespace)
df.head()

df.to_csv("out.csv")