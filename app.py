import streamlit as st
import random

choices = {
    "rock": "stone.jpeg",
    "paper": "paper.jpeg",
    "scissor": "scissor.jpeg"  
}

user_choice = st.selectbox("Choose your option", list(choices.keys()))

if st.button("PLAY"):
    com_choice = random.choice(list(choices.keys()))  # better inside button

    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        st.image(choices[user_choice])
    with col2:
        st.write("V/S")
    with col3:
        st.image(choices[com_choice])

    
    if user_choice == com_choice:
        st.markdown("### It's a tie! 🤝")
    elif (
        (user_choice == "rock" and com_choice == "scissors") or 
        (user_choice == "paper" and com_choice == "rock") or 
        (user_choice == "scissors" and com_choice == "paper")
    ):
        st.markdown("### You win! 🏆")
    else:
        st.markdown("### You lose! 😢")