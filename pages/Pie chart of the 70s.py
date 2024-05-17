import pandas as pd
import matplotlib.pyplot as plt
import streamlit as s

s.title("Top 10 Countries From Your Choice of year")
uf = r'pages/wp.csv'
year = s.selectbox("Select Year", [1970, 1980, 1990, 2000, 2010, 2015, 2020, 2022])

if uf is not None:
    sc = ['Country', '1970 Population']
    df = pd.read_csv(uf, names=sc)
    df_year = df[['Country', str(year) + ' Population']]
    top10 = df_year.nlargest(10, str(year) + ' Population')


    fig, ax = plt.subplots()
    ax.pie(top10[str(year) + ' Population'], labels=top10['Country'], autopct='%1.1f%%', startangle=140)
    ax.set_title('Population Distribution in {}'.format(year))
    plt.show()
    st.pyplot(fig)
