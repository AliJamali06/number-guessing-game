import streamlit as st
import random

# title
st.title("Number Guessing Game")
st.sidebar.header("Game Setting")

# Gsme Setting
min_value = st.sidebar.number_input("Minimun Value", min_value=1, value=1)
max_value = st.sidebar.number_input("Maximum Value",min_value=min_value + 1, value=50)

#Select difficulity level
difficulty = st.sidebar._selectbox(
    "Select Difficulty Level",
    ["Easy (Unlimited Attempts)", "Medium (10 Attempts)", "Hard (5 Attempts)"]
)
#my code up
attempts_limits = {"Easy (Unlimited Attempts)": None, "Medium (10 Attempts)": 10, "Hard (5 Attempts)": 5}

# initialize session state properly
if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(min_value, max_value)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "game_over"not in st.session_state:
    st.session_state.game_over = False
if "reset_game" not in st.session_state:
    st.session_state.reset_game = False

# display game instructions
st.write(f"I have selected a number between **{min_value} and {max_value}**. Can you guess it?")

# get user input
if not st.session_state.game_over:
    user_guess = st.number_input("Enter your guess:", min_value=min_value, max_value=max_value, step=1)
    
    if st.button("Check Guess"):
        if user_guess is not None:
            st.session_state.attempts +=1
   
            if user_guess < st.session_state.random_number:
                st.warning("To Low! Try Again")
            elif user_guess > st.session_state.random_number:
                st.warning("To High! Try Again.")
            
            else:
                st.success(f" Congratulations! You guesses the number in {st.session_state.attempts} attempts.")
                st.session_state.game_over = True

            
            # check attempt limits
            if attempts_limits[difficulty] is not None and st.session_state.attempts >= attempts_limits[difficulty]:
                st.session_state.game_over = True
                st.warning("Game Over! You've reached the maximum attempts.")
                

#show number of attempts
st.write(f"**Attempts** {st.session_state.attempts}")

# Reset Button
if st.button("Reset Game") and st.session_state.game_over:
    st.session_state.reset_game = True
    st.session_state.attempts = 0
    st.experimental_rerun()
