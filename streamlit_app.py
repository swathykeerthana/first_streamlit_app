import streamlit
streamlit.title ('my moms new healthy diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')



streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +this_fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
return fruityvice_normalized
  

streamlit.header('Fruityvice Fruit Advice!')
try:
fruit_choice = streamlit.text_input('what fruit would you like information about?')
if not fruit_choice:
streamlit.error("please select the fruit to get information")
else:
back_from_function = get_fruityvice_data(fruit_choice)
streamlit.dataframe(back_from_function)


except urlerror as e:
  streamlit.error()

streamlit.stop()
import snowflake.connector

def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list ")
    return my_cur.fetchall()

if streamlit.button ('get fruit load list'):
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_data_rows =get_fruit_load_list()
my_cnx.close()
streamlit.dataframe(my_data_rows)

def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
  my_cur.execute ("insert into fruit_load_list values('" + papaya + "')")
 return "thanks for adding" + new_fruit

if streamlit.button ('add a fruit to the list'):
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
back_from_function = insert_row_snowflake(new_fruit)
streamlit.text(back_from_function)



from urllib.error import urlerror









