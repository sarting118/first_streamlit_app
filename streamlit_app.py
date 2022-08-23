import streamlit
import pandas
import requests as re
import snowflake.connector
from urllib.error import URLError

# add a title
streamlit.title("My Mom's New Healthy Diner")
# add a header
streamlit.header('Breakfast Faves')
# if using two .text options I get spaces between lines
# add menu options
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
# add menu options
# streamlit.text('Kale, Spinach & Rocket Smoothie  \nHard-Boiled Free-Range Egg')

streamlit.text('🥬 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')

# alternative to the above - no spaces between lines
# streamlit.text('Omega 3 & Blueberry Oatmeal  \nKale, Spinach & Rocket Smoothie  \nHard-Boiled Free-Range Egg')

streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍇 Build your own fruit smoothie 🍌')

# read in txt file
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list.set_index('Fruit', inplace=True)

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# subset the df on the selected fruit
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display the dataframe onto the menu
streamlit.dataframe(fruits_to_show)

# create the repeatable code block, function
def get_fruityvice_data(this_fruit_choice):
  # API request to fruityvice.com
  fruityvice_response = re.get('https://fruityvice.com/api/fruit/' + fruit_choice)
  # normalise the json version of the response
  fruityvice_normalised = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalised

# new section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error('Please select a fruit to get information.')
  else:
    # streamlit.text(fruityvice_response.json())
    # output the dataframe to the screen as a table
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
    #streamlit.write('The user entered', fruit_choice)

except URLError as e:
  streamlit.error()
  
# don't run anything past here while we troubleshoot
# streamlit.stop()


# streamlit.text("Hello from Snowflake:")
streamlit.header('The fruit load list contains:')

def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    # my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
    # let's query some data instead
    my_cur.execute('select * from fruit_load_list')
    return my_cur.fetchall() # if only wanted one - could you fetchone()

# add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  # display results in dataframe instead of lsit
  # streamlit.text(my_data_row)
  streamlit.dataframe(my_data_rows)

streamlit.stop()
# adding an entry box
new_fruit_choice = streamlit.text_input('What fruit would you like to add?', 'Jackfruit')
streamlit.write('Thanks for adding', new_fruit_choice)

# add rows in snowflake fruit list
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
