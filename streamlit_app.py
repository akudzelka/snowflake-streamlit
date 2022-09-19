import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🐔 Омлет')
streamlit.text('🥑🍞 Тост с авокадо')
streamlit.text('Чай чёрный, шоколад')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

df_my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(df_my_fruit_list)
