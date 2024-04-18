import streamlit as st
import matplotlib.pyplot as plt
from solver import solver 
from input import input_node
from input import input_car
from plot import plot_graph
from plot import plot_result



def page_main():
    st.title("このサイトは配送計画問題が解けるwebサイトです。")
    st.write("")
    st.subheader("「頂点数」、「車両数」、「車両の走行距離の上限」を入力すれば、移動距離の合計が最小となるような配送ルートを教えてくれます。")
    g_button = False
    r_button = False
    global a
    global b
    global c
    global Pos1
    col1,col2 = st.columns(2)
    with col1:
        Pos,V = input_node()
        car, lim,T = input_car()
      
        if st.button("グラフを表示して最適ルートを計算"):
            g_button = True
            if g_button:
                b = 0
                if b == 0:
                    c = b
                    b += 1
            if c == 0:
                r_button = True

        
        #if r_but:
         #   r_button = True
            

    with col2:
        if g_button:
            a = 0
            if a == 0:
                Pos1 = Pos
                a += 1
            plot_graph(Pos)
        if r_button:
            edges = solver(V,Pos1,T,car,lim)
            if edges == "error":
                st.subheader("問題が解けないので入力値を変えてください。")
            else:
                plot_result(Pos1,edges)


    st.title("")
    st.title("")
    st.title("")
    st.title("")
    st.write("※各頂点は[0,10]×[0,10]の2次元ユークリッド平面上にランダムに配置されます。")
    st.write("※任意の2頂点間の距離はユークリッド距離で定義されます。")
    st.write("※各車両の走行距離が設定された走行距離の上限を超えないような配送ルートを考えます。")
    st.write("※各車両がデポ（ピンクの点）から出発して各頂点を回ってまたデポに戻ってくるようなルートを考えます。")
    st.write("※全ての頂点を丁度1度通るような配送ルートのうち、車両の走行距離の合計が最小となるような配送ルートを求めます。")       

    


