import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🐔 Омлет')
streamlit.text('🥑🍞 Тост с авокадо')
streamlit.text('Чай чёрный, шоколад')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

df_my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
df_my_fruit_list = df_my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(df_my_fruit_list.index), ['Avocado', 'Strawberries'])

fruits_to_show = df_my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)


streamlit.header("Fruityvice Fruit Advice!")
try:
 fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
 if not fruit_choice:
  streamlit.error("Please select a fruit!")
 else:
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  streamlit.dataframe(fruityvice_normalized)
except URLError as e:
 streamlit.error()

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

streamlit.stop()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_rows = my_cur.fetchall()
streamlit.header("The list contains fruits:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like to add?','Apple')
streamlit.write('Thanks for adding ', add_my_fruit)
my_cur.execute("INSERT INTO FRUIT_LOAD_LIST VALUES ('" + add_my_fruit + "')")
