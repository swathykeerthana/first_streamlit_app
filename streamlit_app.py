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

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("the fruit load list contains:")
streamlit.dataframe(my_data_rows)



from urllib.error import urlerror


my_cur.execute("insert into fruit_load_list values('from streamlit)")


fruit_choice = streamlit.text_input('what fruit would you like to add?','kiwi')
streamlit.write('thanks for adding', fruit_choice)







