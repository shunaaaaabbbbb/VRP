import streamlit as st

def page_howto():


    st.title("このサイトの使い方")
    st.subheader("下図のように各数値を入力して「グラフを表示して最適ルートを計算」ボタンを押してください。")
    st.image("image/input.png")
    st.title("\u2193")
    st.subheader("「グラフを表示して最適ルートを計算」ボタンを押すと下図のようにグラフとそのグラフの最適ルートが得られます。")
    st.image("image/result.png")
    st.title("\u2193")
    st.subheader("最適解が得られないときは以下のように表示されます。")
    st.image("image/error.png")

