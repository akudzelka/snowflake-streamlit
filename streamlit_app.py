import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🐔 Омлет')
streamlit.text('🥑🍞 Тост с авокадо')
streamlit.text('Чай чёрный, шоколад')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

df_my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
df_my_fruit_list = df_my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(df_my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(df_my_fruit_list)
