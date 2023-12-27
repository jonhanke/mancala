import streamlit as st
import pandas as pd
import numpy as np

from mancala import *

## Define the game board instance
if 'game_board' not in st.session_state:
    st.session_state['game_board'] = Kalah(m=6, n=4)



## Create the app title
st.title('Mancala')

## Show the game board
st.write(st.session_state['game_board'].__repr__())


## Add a cleaner board display
col_list = st.columns(8)
first_col = col_list[0]
last_col = col_list[-1]

with first_col:
    st.write('')
    st.write('North Player Cradle')
    st.write(str(st.session_state['game_board'].game_state_list[0]))

with last_col:
    st.write('')
    st.write('South Player Cradle')
    st.write(str(st.session_state['game_board'].game_state_list[7]))

for i, col in enumerate(col_list[1:-1]):
    with col:
        st.write(str(st.session_state['game_board'].game_state_list[14-i]))
        st.write('')
        st.write(str(st.session_state['game_board'].game_state_list[i]))


## Get the next move
move = st.text_input("Enter your move ('Q' to quit): ")

## Apply the move
try:
    st.session_state['game_board'].perform_move(int(move))
except:
    pass

## Show the game history
st.write("Game History:")
st.write(st.session_state['game_board'].history_list())


