//参考：DFS (深さ優先探索) 超入門！ 〜 グラフ・アルゴリズムの世界への入口 〜【前編】
//https://qiita.com/drken/items/4a7869c5e304883f539b

//#include <bits/stdc++.h>
//using namespace std;

using Graph = vector<vector<int>>;

//DFS(深さ優先探索)
vector<bool> seen;
void dfs(const Graph &G, int v) {
    
    //vを探索済みにする
    seen[v] = true;

    //vから行ける各頂点 next_v について
    for (auto next_v : G[v]) {

        //next_vが探索済みならスルー
        if (seen[next_v]) continue;

        //再帰して探索
        dfs(G, next_v);
    } 
}