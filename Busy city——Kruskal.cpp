//
//  main.cpp
//  Busy city——Kruskal
//
//  Created by 杨添凯 on 2019/4/30.
//  Copyright © 2019年 杨添凯. All rights reserved.
//

#include <iostream>
#include <algorithm>
#define MAX 30000
using namespace std;

struct Edge{
    int u;
    int v;
    int score;
}edge[MAX];

int father[MAX];
int size[MAX];

//根结点的father指向自己的下标
int Find(int x){
    while (x!=father[x]) 
    {
        x = father[x];
    }

    return x;
}

//合并
void Union(int u, int v){
    u = Find(u);
    v = Find(v);
    if (u==v){
        return;
    }
    else{
        if (size[u]>=size[v]){
            father[v] = u;
            size[u] += size[v];
        }
        else{
            father[u] = v;
            size[v] +=size[u];
        }
    }
}

bool cmp(Edge a, Edge b){
    return a.score < b.score;
}

int main(){
    int n;
    int m;
    cin>>n>>m;
    //初始化并查集
    for(int i=1; i<=n; ++i){
        father[i]=i;
        size[i]=1;
    }
    //输入
    for(int i=1; i<=m; ++i){
        cin>>edge[i].u>>edge[i].v>>edge[i].score;
    }
    sort(edge+1, edge+m+1, cmp);
    int count;    //路径总数（n-1）
    int max;    //最大耗费
    //初始化
    {
        count = 0;
        max = 0;
    }
    //Kruskal
    for(int i=1; i<=m; ++i){
        if(Find(edge[i].u)!=Find(edge[i].v)){
            Union(edge[i].u, edge[i].v);
            if(max<edge[i].score){
                max = edge[i].score;
            }
            count++;
        }
        if(count==n-1){
            break;
        }
    }
    cout<<count<<" "<<max<<endl;
}
