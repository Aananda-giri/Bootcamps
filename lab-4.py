# Lab-4.1 Python program to implement BFS
def calculate_path_cost(path):
    path_cost = 0
    for i in range(1, len(path)):
        edge = path[i-1] + path[i]
        step_cost = cost[edge]
        path_cost += step_cost
    return path_cost
def BFS():
    expanded = []
    pathqueue = [[start]]
    fringe = [start]
    while fringe:
        node = fringe.pop(0)
        path = pathqueue.pop(0)
        if node == goal:
            print("Goal Found!!!!!")
            print("Solution path:", path)
            path_cost = calculate_path_cost(path)
            print(f"path cost: {path_cost}")
            break
        # return
        else:
            neighbours = graph[node]
            for neighbour in neighbours:
                # if neighbour not in neighbours:
                fringe.append(neighbour)
                new_path = list(path)
                new_path.append(neighbour)
                pathqueue.append(new_path)
            expanded.append(node)

graph = {'a':['b','c'], 'b':['c','d','e'], 'c':['d','e'], 'd':['g'], 'e':['d','g']}
cost = {'ab':5, 'ac':3, 'bc':6, 'bd':2, 'be':8, 'cd':7, 'ce':6, 'dg':5, 'eg':4}

        