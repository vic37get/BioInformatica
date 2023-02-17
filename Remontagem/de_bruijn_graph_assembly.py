def debruijnize(reads):
    nodes = set()
    not_starts = set()
    edges = []
    for r in reads:
        r1 = r[:-1]
        r2 = r[1:]
        nodes.add(r1)
        nodes.add(r2)
        edges.append((r1,r2))
        not_starts.add(r2)
    return (nodes,edges,list(nodes-not_starts))

def build_k_mer(str,k):
    return [str[i:k+i] for i in range(0,len(str)-k+1)]

def make_node_edge_map(edges):
    node_edge_map = {}
    for e in edges:
        n = e[0]
        if n in node_edge_map:
            node_edge_map[n].append(e[1])
        else:
            node_edge_map[n] = [e[1]]
    return node_edge_map

def eulerian_trail(m,v):
    nemap = m
    result_trail = []
    start = v
    result_trail.append(start)
    while(True):
        trail = []
        previous = start
        while(True):
            
            if(previous not in nemap):
                break
            next = nemap[previous].pop()
            if(len(nemap[previous]) == 0):
                nemap.pop(previous,None)
            trail.append(next)
            if(next == start):
                break;
            previous = next
        # completed one trail
        print(trail)
        index = result_trail.index(start)
        result_trail = result_trail[0:index+1] + trail + result_trail[index+1:len(result_trail)]
        # choose new start
        if(len(nemap)==0):
          break
        found_new_start = False
        for n in result_trail:
            if n in nemap:
                start = n
                found_new_start = True
                break # from for loop
        if not found_new_start:
            print("error")
            print("result_trail",result_trail)
            print(nemap)
            break
    return result_trail

def assemble_trail(trail):
    if len(trail) == 0:
        return ""
    result = trail[0][:-1]
    for node in trail:
        result += node[-1]
    return result

reads = build_k_mer("ATCGTTGCGCGACCG",3)
print(reads)

G = debruijnize(reads)
print(G)

m = make_node_edge_map(G[1])
print(m)

start = G[2][0] if (len(G[2]) > 0) else G[0][0]
print (m)

t = eulerian_trail(m,start)
print(t)

print(assemble_trail(t))