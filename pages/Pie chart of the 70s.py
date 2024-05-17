import pandas as pd
import matplotlib.pyplot as plt
import streamlit as s

s.title("Top 10 Countries From 70s till Now")
uf = r'pages/wp.csv'
year = s.selectbox

if uf is not None:
    sc = ['Country', '1970 Population']
    df = pd.read_csv(uf, names=sc)
    top5 = df.nsmallest(10, '1970 Population')


    df.set_index('Country', inplace=True)  

    df.plot(kind='pie', y=top5, figsize=(8, 8), autopct='%1.1f%%', startangle=140)
    plt.title('Population Distribution in 1970')
    plt.ylabel('')  
    plt.show()
