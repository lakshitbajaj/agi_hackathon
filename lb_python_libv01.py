# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 20:36:02 2022

@author: laksh
"""

import pandas as pd
import numpy as np

#from pathlib import Path

#Returns a list of column names conatining a particular string
def col_like(df,col_string):
    colstring_upper = col_string.upper()
    return df.columns[df.columns.str.upper().str.contains(colstring_upper)]


#Creates columns of year and months based on particular date
def month_year_col_create(df, col_date):
    df[col_date + '_year'] = df[col_date].dt.year
    df[col_date +'_month'] = df[col_date].dt.to_period('M')
    return df
    
#Returns aggregation on a set of columns and can have different columns for 
# mean, median, count, nunique
def agg_metric(df, list_gpby, agg_dict):
    df_agg = df.groupby(list_gpby).agg(agg_dict).reset_index()
    return df_agg

#Function to display nulls against column names
def display_nulls(df):
    for col in df.columns:
        print(col)
        print(df.col.isna().sum(),"\n")
   
#Function to display nulls percent against column names
def display_nulls_percent(df):
    for col in df.columns:
        print(col)
        print(df.col.isna().sum()*100/len(df),"\n")        

#Stores percentage of missing values in a dictionary
def miss_cols_dict(df):
    missing_col_dict = {}

    for col in df.columns:    
        if df[col].isna().sum()>0:
            missing_col_dict[col] = df[col].isna().sum()*100/len(df)
            
    return missing_col_dict


#Returns a list of columns that can be excluded if they have a 
#certain percent of nulls
def mis_col_filterout(df, threshold):
    missing_col_dict =  miss_cols_dict(df)
    max_missing = [k for k, v in missing_col_dict.items() if v > threshold]
    return max_missing
    
            
            

    

