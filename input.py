import streamlit as st
import random

## テストテスト

def input_node():
    num =  st.slider("頂点数を入力(デポを除く)", min_value=2, max_value=10, key = "node")
    V = [i for i in range(num+1)]
    Pos = [[0 for _ in range(num+1)] for _ in range(2)]
    for i in range(num-1):
        Pos[0][i+1] = random.uniform(0,10)
        Pos[1][i+1] = random.uniform(0,10)
    Pos[0][0] = sum(Pos[0][1:]) / len(Pos[0][1:])
    Pos[1][0] = sum(Pos[1][1:]) / len(Pos[1][1:])
    
    return Pos, V

def input_car():
   car = st.slider("車両数を入力", min_value = 1, max_value = 4, key = "car")
   lim = st.number_input("走行距離の上限を入力",min_value = 1.0,step = 0.1, key = "lim")
   T = [i for i in range(car)]
   return car, lim, T
    