import streamlit as st
import numpy as np

# ---------- Game Logic ----------
def print_board_ui(b):
    symbols = {0: " ", 1: "X", -1: "O"}
    st.write("### Game Board")
    board_str = ""
    for r in range(3):
        row = " | ".join(symbols[val] for val in b[r])
        board_str += row + "\n"
        if r < 2:
            board_str += "--+---+--\n"
    st.code(board_str)

def check_winner(b):
    if 3 in np.sum(b, axis=1) or 3 in np.sum(b, axis=0):
        return "X"
    if -3 in np.sum(b, axis=1) or -3 in np.sum(b, axis=0):
        return "O"

    if np.trace(b) == 3 or np.trace(np.fliplr(b)) == 3:
        return "X"
    if np.trace(b) == -3 or np.trace(np.fliplr(b)) == -3:
        return "O"

    if not 0 in b:
        return "DRAW"

    return None

# ------------------- STREAMLIT UI -------------------

st.title("🎮 Tic Tac Toe (NumPy + Streamlit)")

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = np.zeros((3, 3), dtype=int)

if "current" not in st.session_state:
    st.session_state.current = 1   # X starts

symbols = {1: "X", -1: "O"}

print_board_ui(st.session_state.board)

# Result check before showing inputs
result = check_winner(st.session_state.board)
if result:
    if result == "DRAW":
        st.success("😐 It's a Draw!")
    else:
        st.success(f"🎉 {result} Wins!")

    if st.button("Restart Game"):
        st.session_state.board = np.zeros((3, 3), dtype=int)
        st.session_state.current = 1
    st.stop()

# Player turn indicator
st.subheader(f"Current Turn: **{symbols[st.session_state.current]}**")

# Row and column selectors
row = st.number_input("Choose Row (0–2)", min_value=0, max_value=2, step=1)
col = st.number_input("Choose Column (0–2)", min_value=0, max_value=2, step=1)

if st.button("Place Move"):
    # Validate move
    if st.session_state.board[row, col] != 0:
        st.error("This position is already occupied!")
    else:
        st.session_state.board[row, col] = st.session_state.current
        st.session_state.current *= -1   # switch turn

    st.rerun()
