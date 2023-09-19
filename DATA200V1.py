#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

df1=pd.read_csv('mountain_flowers.csv')
sel = st.radio("Select Petal height or Width",["Height","Width"])

if sel=='Height':
    sf=plt.figure()
    plt.xlabel('Flower Name')
    plt.ylabel('Petal Length')
    plt.title('Petal LENGTH of Flowers')
    plt.bar(df1['name'],df1['petal_length'],color='green')
    st.pyplot(sf)
    
elif sel=='Width':
    sf=plt.figure()
    plt.xlabel('Flower Name')
    plt.ylabel('Petal Width')
    plt.title('Petal WIDTH of Flowers')
    plt.bar(df1['name'],df1['petal_width'])
    st.pyplot(sf)

"""sf1=plt.subplot()
sf=plt.figure()
plt.bar(df1['name'],df1['petal_length'])
#st.bar_chart(d)
st.pyplot(sf)


plt.scatter(df1['petal_width'],df1['petal_length'])
st.pyplot()"""

# 

# In[ ]:




"""plt.figure()
plt.ylabel('length of flower')
plt.xlabel('name')
#data=[df1['name'],df1['petal_length']]
plt.bar(df1['name'],df1['petal_length'])"""
