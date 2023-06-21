INF = int(1e9+7)

def floyd_warshall(dist, length):
    # path array stores the intermediate node in between source and destination
    path = [[INF for i in range(length)]for j in range(length)]
    # for evry nodes, check if the path having the node as
    # intermediate node is shorter than current distance
    # if it is, update distance array and add intermediate node to path array
    for r in range(length):
        for p in range(length):
            for q in range(length):
                if(dist[p][q]>dist[p][r]+dist[r][q]):
                    dist[p][q] = dist[p][r]+dist[r][q]
                    path[p][q] = r
    print_dist(dist,length)
    return path

def print_dist(dist,length):
    # print the shortest distance between source and destination
    for p in range(length):
        temp=""
        for q in range(length):
            if(dist[p][q]==INF):
                temp+="INF "
            else:
                temp+=str(dist[p][q])+" "
        print(temp+" ")

def print_path(printPath,path,src,dst):
    # print the shortest path by calling print_path() recursively
    if(path[src][dst]==INF):
        printPath.append(src)
        return
    # print path from source to intermediate node
    print_path(printPath,path,src,path[src][dst])
    # print path from intermediate node to destination
    print_path(printPath,path,path[src][dst],dst)
    printPath.append(dst)
    return

if __name__ == '__main__':
    W = [[0,3,INF,7],
         [8,0,2,INF],
         [5,INF,0,1],
         [2,INF,INF,0]]
    # get intermedeate node for every source and destination 
    path = floyd_warshall(W,len(W[0]))
    # print the shortest path
    printPath = []
    print_path(printPath,path,1,3)
    print("path from 1 to 3:",printPath)
    printPath.clear()
    print_path(printPath,path,0,2)
    print("path from 0 to 2:",printPath)
