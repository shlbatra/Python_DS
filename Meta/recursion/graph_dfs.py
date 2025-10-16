#  DFS Search for value

def dfs_graph(graph, source, visited, tgt):
    if source == tgt:
        return True

    for nbr in graph[source]:
        if nbr in visited: continue # ignore cycles
        visited.add(nbr)
        isfound = dfs_graph(graph, nbr, visited, tgt)
        if isfound == True:
            return True

    return False

graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

found = dfs_graph(graph, 'a', set(), 'e')
print(found)
found = dfs_graph(graph, 'a', set(), 'k')
print(found)