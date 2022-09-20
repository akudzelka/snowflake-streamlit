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

def get_fruitvice_data(this_fruit_choice):
 fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
 fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
 return fruityvice_normalized 

streamlit.header("Fruityvice Fruit Advice!")
try:
 fruit_choice = streamlit.text_input('What fruit would you like information about?')
 if not fruit_choice:
  streamlit.error("Please select a fruit!")
 else:
  df_from_def = get_fruitvice_data(fruit_choice)
  streamlit.dataframe(df_from_def)
  
except URLError as e:
 streamlit.error()

streamlit.header("The list contains fruits:")

def get_fruit_load_list():
 with my_cnx.cursor() as my_cur:
  my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
  return my_cur.fetchall()
 
if streamlit.button('Get fruit load list'):
 my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
 my_data_rows = get_fruit_load_list()
 streamlit.dataframe(my_data_rows)

streamlit.stop()

def insert_user_fruit(new_fruit):
 with my_cnx.cursor() as my_cur:
  my_cur.execute("INSERT INTO FRUIT_LOAD_LIST VALUES ('" + new_fruit + "')")
  return 'Thanks for adding ' + new_fruit
  
add_my_fruit = streamlit.text_input('What fruit would you like to add?')

if streamlit.button('Add a fruit'):
 my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
 fruit_from_def = insert_user_fruit(add_my_fruit)
 streamlit.text(fruit_from_def)
