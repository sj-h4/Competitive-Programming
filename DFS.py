#DFS(再帰関数で)
# v := スタート位置

def dfs(Graph, v):

    #初期化する
    seen = [-1]*(len(Graph))

    #vを探索済みにする
    seen[v] = 1

    #vから行ける各頂点 next_vについて
    for next_v in Graph[v]:

        #next_vが探索済みならスルー
        if seen[next_v] != -1: continue

        #再帰して探索
        dfs(Graph, next_v)



#Graph = [['頂点の番号', '隣接する頂点の番号'] for _ in range("頂点の個数")]