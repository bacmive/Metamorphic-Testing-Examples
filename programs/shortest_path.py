##########################################################################
# File name: shortest_path.py
# Author: tam sei kwan
# eMail:1228150491@qq.com
# Created Time: 2020年09月15日 星期二 10时18分32秒
##########################################################################
#!/usr/bin/env python
# coding=utf-8
inf_max = 1e9

def shortest_path(x, y, G):
    '''
    x,y are nodeID
    the input G is a two-dimension array, which represents the Graph
    '''
    a = x-1
    b = y-1
    n = len(G)
    # record the path
    parents = [[i]*n for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if G[i][k] + G[k][j] < G[i][j]:
                    G[i][j] = G[i][k] + G[k][j]
                    parents[i][j] = parents[k][j]
    p = []                    
    def path(i, j):
        if i!=j:
            path(i, parents[i][j])
        p.append(j)
    path(a, b)
    
    p = [i+1 for i in p]

    return (G[a][b], p)


if __name__ == '__main__':
    G = [
        [0,10,20,30],
        [10,0,15,18],
        [20,15,0,6],
        [30,18,6,0]
    ]

    val, p= shortest_path(1,4,G)
    print(val, p)
    
