import streamlit

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
