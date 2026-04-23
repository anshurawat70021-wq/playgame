import streamlit as st
import random

st.set_page_config(page_title="Fun Games Hub 🎮", layout="centered")

st.title("🎮 Fun Games Hub")

# Sidebar menu
game = st.sidebar.selectbox(
    "Choose a game 👇",
    ["Guess the Number", "Rock Paper Scissors", "Quiz Game"]
)

# -----------------------------
# 🎯 GAME 1: Guess the Number
# -----------------------------
if game == "Guess the Number":
    st.header("🔢 Guess the Number")

    if "number" not in st.session_state:
        st.session_state.number = random.randint(1, 100)

    guess = st.number_input("Enter your guess (1-100)", min_value=1, max_value=100)

    if st.button("Submit Guess"):
        if guess < st.session_state.number:
            st.warning("Too low! 📉")
        elif guess > st.session_state.number:
            st.warning("Too high! 📈")
        else:
            st.success("🎉 Correct! You win!")
            st.session_state.number = random.randint(1, 100)

# -----------------------------
# ✊ GAME 2: Rock Paper Scissors
# -----------------------------
elif game == "Rock Paper Scissors":
    st.header("✊ Rock Paper Scissors")

    choices = ["Rock", "Paper", "Scissors"]
    user = st.selectbox("Choose your move", choices)

    if st.button("Play"):
        computer = random.choice(choices)
        st.write(f"Computer chose: {computer}")

        if user == computer:
            st.info("It's a draw 🤝")
        elif (
            (user == "Rock" and computer == "Scissors") or
            (user == "Paper" and computer == "Rock") or
            (user == "Scissors" and computer == "Paper")
        ):
            st.success("You win 🎉")
        else:
            st.error("You lose 😢")

# -----------------------------
# 🧠 GAME 3: Quiz Game
# -----------------------------
elif game == "Quiz Game":
    st.header("🧠 Simple Quiz")

    score = 0

    q1 = st.radio("1. Capital of India?", ["Mumbai", "Delhi", "Kolkata"])
    q2 = st.radio("2. 5 + 3 = ?", ["6", "8", "10"])
    q3 = st.radio("3. Which is a programming language?", ["Python", "Snake", "Lion"])

    if st.button("Submit Quiz"):
        if q1 == "Delhi":
            score += 1
        if q2 == "8":
            score += 1
        if q3 == "Python":
            score += 1

        st.success(f"Your Score: {score}/3")

        if score == 3:
            st.balloons()
