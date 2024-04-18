import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt



def plot_graph(Pos):
    G = nx.Graph()
    for u in range(len(Pos[0])):
        G.add_node(u, pos=(Pos[0][u], Pos[1][u]))
    node_pos = nx.get_node_attributes(G, 'pos')

    for u in range(len(Pos[0])):
        if u == 0:  # Pos[0][0]とPos[1][0]の点を赤色にする
            nx.draw_networkx_nodes(G, pos=node_pos, nodelist=[u], node_color='violet', node_size=300)
        else:
            nx.draw_networkx_nodes(G, pos=node_pos, nodelist=[u], node_color='skyblue', node_size=300)
    plt.axis('on')  # 軸を表示する
    plt.xticks(range(0,11))  # x軸の目盛りを設定
    plt.yticks(range(0,11))  # y軸の目盛りを設定
    plt.xlim(-1,11)
    plt.ylim(-1,11)
    plt.title("Graph")
    
    # 黒い枠を付ける
    plt.gca().spines['top'].set_color('black')
    plt.gca().spines['bottom'].set_color('black')
    plt.gca().spines['left'].set_color('black')
    plt.gca().spines['right'].set_color('black')

    plt.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
    fig1 = plt.gcf()
    st.pyplot(fig1)


def plot_result(Pos,edges):
    
    G = nx.Graph()
    for u in range(len(Pos[0])):
        G.add_node(u, pos=(Pos[0][u], Pos[1][u]))
    node_pos = nx.get_node_attributes(G, 'pos')

    for u in range(len(Pos[0])):
        if u == 0:  # Pos[0][0]とPos[1][0]の点を赤色にする
            nx.draw_networkx_nodes(G, pos=node_pos, nodelist=[u], node_color='violet', node_size=300)
        else:
            nx.draw_networkx_nodes(G, pos=node_pos, nodelist=[u], node_color='skyblue', node_size=300)
    
    colors = ["orange", "green","salmon","blue"]

    # 全てのエッジの太さを設定
    nx.draw_networkx_edges(G, pos=node_pos, edgelist=edges, width=2, edge_color='darkorange', arrows=True,arrowstyle='->')  # エッジを描画
    plt.axis('on')  # 軸を表示する
    plt.xticks(range(0,11))  # x軸の目盛りを設定
    plt.yticks(range(0,11))  # y軸の目盛りを設定
    plt.xlim(-1,11)
    plt.ylim(-1,11)
    plt.title("Optimal Route")
    
    # 黒い枠を付ける
    plt.gca().spines['top'].set_color('black')
    plt.gca().spines['bottom'].set_color('black')
    plt.gca().spines['left'].set_color('black')
    plt.gca().spines['right'].set_color('black')

    plt.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)

    fig2 = plt.gcf()
    st.pyplot(fig2)