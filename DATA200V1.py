#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

df1=pd.read_csv('mountain_flowers.csv')
sel = st.radio("Select Petal height or Width",["Height","Width"])
sf=plt.figure()
plt.xlabel('Flower Name')

if sel=='Height':
    plt.ylabel('Petal Length')
    plt.title('Petal LENGTH of Flowers')
    plt.bar(df1['name'],df1['petal_length'],color='green')
    st.pyplot(sf)
    st.subheader('Bluebells are ~30% smaller than Colorado Lotus')
    
elif sel=='Width':
    plt.ylabel('Petal Width')
    plt.title('Petal WIDTH of Flowers')
    plt.bar(df1['name'],df1['petal_width'])
    st.pyplot(sf)
    st.subheader('Colorado Lotus is 3x wider than violets')
