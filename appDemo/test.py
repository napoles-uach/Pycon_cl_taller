import streamlit as st
import pandas as pd
import altair as alt

#make a title for this demo using emojis
st.title('DataFrame Demo')

## Elements on the sidebar
st.sidebar.selectbox('Choose a demo', ['DataFrame Demo', 'Other'])
check=st.sidebar.checkbox('Show code')

#write some text describing the app
'''
This is a demo shows how to use `st.write` to visualize Pandas DataFrames

[Data courtesy of the [UN Data Explorer](http://data.un.org/Data.aspx?d=FAO&f=itemCode%3a2051).)
'''

df = pd.read_csv('UNdata_Export_20211101_202548548.csv')

# make a list with the countries in the dataframe
countries = df['Country or Area'].unique()
#st.write(countries)

##make a multiselect box with the countries
country_select = st.multiselect('Choose Countries', countries, default=['Chile','Mexico'])
#st.write(country_select)

df2=df[df['Country or Area'].isin(country_select)]

st.subheader('Gross Production Index Number')
st.write(df2.head())

df_plot=df2[['Year','Value','Country or Area']]

c = alt.Chart(df_plot).mark_area(opacity=0.3).encode(
    x='Year',
    y='Value',
    color='Country or Area'
)

st.altair_chart(c,use_container_width=True)

#use st.code to show the code of this app.py
if check:
    text=open('app.py').read()
    st.code(text,language='python')









