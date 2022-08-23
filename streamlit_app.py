import streamlit
import pandas
import requests as re

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

# new section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)

# API request to fruityvice.com
fruityvice_response = re.get('https://fruityvice.com/api/fruit/' + fruit_choice)
# streamlit.text(fruityvice_response.json())

# normalise the json version of the response
fruityvice_normalised = pandas.json_normalize(fruityvice_response.json())
# output the dataframe to the screen as a table
streamlit.dataframe(fruityvice_normalised)
