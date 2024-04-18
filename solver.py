import streamlit as st
from pulp import *

def solver(V,Pos,T,car,lim):
    d = {}
    for u in range(len(Pos[0])):
        for v in range(len(Pos[1])):
            d[(u,v)] = ((Pos[0][u] - Pos[0][v])**2 + (Pos[1][u] - Pos[1][v])**2)**(1/2)

    V_0 = V[1:]
    ## 整数計画問題として定式化したものを解く
    prob = pulp.LpProblem(sense = LpMinimize)

    x = LpVariable.dicts("x", [(i, u, v) for i in T for u in V for v in V if u != v], cat="Binary")
    y = LpVariable.dicts("y", (V_0), cat="Continuous")

    prob += lpSum(d[(u,v)] * x[i,u,v] for i in T for u in V for v in V if u != v)

    for i in T:
        prob += lpSum(x[i,0,v] for v in V_0) == 1

    for v in V_0:
        prob += lpSum(x[i,u,v] for i in T for u in V if u != v) == 1

    for i in T:
        for v in V:
            prob += lpSum(x[i,u,v] for u in V if u != v) - lpSum(x[i,v,w] for w in V if v != w) == 0

    for i in T:
        prob += lpSum(d[(u,v)] * x[i,u,v] for u in V for v in V_0 if u != v) <= lim

    for u in V_0:
        for v in V_0:
            if u != v:
                prob += y[u] - y[v] + len(V)*lpSum(x[i,u,v] for i in T) <= len(V) - 1

    result = prob.solve()
    if LpStatus[result] == "Optimal":
        edges = []
        for i in T:
            for u in V:
                for v in V:
                    if u != v:
                        if x[i,u,v].value() == 1:
                            edges.append((u,v))
    
        return edges
    else:
        return "error"