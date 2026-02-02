
import streamlit as st

st.set_page_config(page_title="Emoji Streamlit App 😄", page_icon="📊")

st.title("Welcome to My Awesome Streamlit App! ✨")
st.markdown("--- 😄 ---")

st.header("Here are some cool emojis: ")
st.write("Happy face: 😀")
st.write("Rocket: 🚀")
st.write("Star: ⭐")
st.write("Thumbs up: 👍")
st.write("Heart: ❤️")

st.subheader("Let's add some interactive elements too! 👇")

name = st.text_input("What's your name? 🤔")
if name:
    st.success(f"Hello, {name}! Glad to have you here! 👋")


option = st.selectbox(
    'Which emoji is your favorite? 👇',
    ('😀', '🚀', '⭐', '👍', '❤️'))

st.write('You selected:', option)

st.slider('How much do you like emojis? (0-10) 🤩', 0, 10)

st.button('Click Me! 🎉')

st.markdown("--- That's all for now! 👋 --- ")
