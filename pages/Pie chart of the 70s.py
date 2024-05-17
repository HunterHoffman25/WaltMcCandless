import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title("Top 10 Countries From 70s till Now")

# Use st.sidebar.selectbox if you want it in the sidebar
year = st.selectbox("Select Year", [1970, 1980, 1990, 2000, 2010, 2020])

uf = r'pages/wp.csv'

if uf is not None:
    df = pd.read_csv(uf)
    
    # Debugging: Print out column names
    print("Column Names:", df.columns)
    
    # Filter data for the selected year
    year_column = str(year) + ' Population'
    df_year = df[['Country', year_column]]
    
    # Debugging: Print out selected DataFrame
    print("Selected DataFrame:", df_year)
    
    top10 = df_year.nlargest(10, year_column)
    
    # Plotting
    fig, ax = plt.subplots()
    ax.pie(top10[year_column], labels=top10['Country'], autopct='%1.1f%%', startangle=140)
    ax.set_title('Population Distribution in {}'.format(year))
    plt.show()
    st.pyplot(fig)
