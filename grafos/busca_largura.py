def get_grafo():
    n = int(input())
    result = []
    for _ in range(n):
        m = input().split()
        result.append(tuple( [ (x) for x in m ] ))
        result.append(tuple( [ (x) for x in m[::-1] ] ))
    list_adj = dict()
    for a,b in result:
        if a in list_adj:
            list_adj[a]['adj'].append({ 'v': b })
        else :
            list_adj[a] = { 'adj' : [{'v' : b}]}
    return list_adj

def bfs(g , s):
    for k in [ v2 for v2 in g if v2 != s ]:
        g[k]['color'] = 'white'
        g['d'] = 999
        g['pi'] = None
    g['s']['color'] = 'gray'
    g['s']['d'] = 0
    g['s']['pi'] = None
    q = []
    q = [s]
    while q != []:
        u = q.pop(0)
        for v in g[u]['adj']:
            if g['v']['color'] == 'white':
                g['v']['color'] = 'gray'
                g['v']['d'] = g[u]['d'] + 1
                g['v']
        

l_adj = get_grafo()

print(l_adj)

for a,b in l_adj.items():
    print(a, [ x['v'] for x in b['adj'] ] )