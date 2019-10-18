import sys
import re
FindKeyARR = []
FindValueArr = []
OurControlValueArr = []
OurControlKeyArr = []
with open(sys.argv[1], 'r') as dosya:
    Reader = dosya.readlines()


    for x in range(0,7):
        if(Reader[x].__len__() != 0):
            FindValueArr.append(re.findall("[0-9]", Reader[x]))
            FindKeyARR.append(re.findall("[A-Z]", Reader[x]))

    #print(ElemanSayisi)
KeyArr = []
ValueArr = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
#print(FindValueArr)
for i in range(0,20):
    KeyArr.append(None)
    for x in range(0,20):
        ValueArr[x].append(None)


#if(int(FindValueArr[0][0]) == 0):
    #print("true")
p = 0
while( p  < len(FindKeyARR)):
    KeyArr[p] = FindKeyARR[p][0]
    p = p +1


#print("sıfırın sıfırıncı eleman" , FindValueArr)

for h in range(len(FindValueArr)):
    q = -1
    while (q < len(FindValueArr) - 1):
        q = q + 1
        if(int(FindValueArr[h][q]) != 0):
            ValueArr[h][q] = FindKeyARR[h][q+1]

graph = { KeyArr[0] : ValueArr[0],
          KeyArr[1] : ValueArr[1],
         KeyArr[2] : ValueArr[2],
         KeyArr[3] : ValueArr[3],
         KeyArr[4] : ValueArr[4],
         KeyArr[5] : ValueArr[5],
         KeyArr[6] : ValueArr[6],
          None : [None, None]}




# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]

    # return path if start is goal
    if start == goal:
        return start

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        #print("PATH" , path)
        # get the last node from the path
        node = path[-1]


        #print("NODE", node)
        if node not in explored and node is not None:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                #print("This is new path" , new_path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                myarray = []
                if neighbour == goal:

                    for a in range(len(new_path)):
                        if(a == len(new_path)-1):
                            print(new_path[-1])
                        else:
                            print(new_path[a], end= " - ")

                    return new_path

            # mark node as explored
            explored.append(node)

    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("

x = input(str("Please enter the start state : "))
y = input(str("Please enter the goal state : "))
print("BFS : ", end="")
bfs_shortest_path(graph, x, y)  # returns ['G', 'C', 'A', 'B', 'D']


def dfs(graph, origin, destination):
    # initialize our path list with the origin node
    path_list = [[origin]]

    # empty lists return false, so the loop will keep running
    # as long as there are paths in the path_list to check
    while path_list:

        # pop out the last path on the path list
        path = path_list.pop()

        # if the last node in that path is our destination,
        # we found a correct path
        last_node = path[-1]
        if last_node == destination:
            for a in range(len(path)):
                if (a == len(path) - 1):
                    print(path[-1])
                else:
                    print(path[a], end=" - ")
            return path

        # if not, we have to add new paths with all of the
        # neighbors of that last node, as long as those neighbors
        # aren't on the path already
        else:
            for node in graph[last_node]:
                if node not in path:
                    # make a new path ending with the neighbor node
                    new_path = path + [node]
                    # add the new path to the path list
                    path_list.append(new_path)

                    # if the while loop continues without finding a path,
    # then no path exists
    print('No path exists between %s and %s' % (origin, destination))

print("DFS : ", end="")
dfs(graph, x, y)

myARR = []

def ucs(graph, origin, destination):
   x  = 0
   minvalue = 1000
   myARR.append(origin)
   while(x < 20):
       if(origin == FindKeyARR[x][0]):
           print(origin)
           y = -1
           while(y < len(FindValueArr[0])):
                y = y + 1
                if (y == len(FindValueArr[0])):

                    return minvalue
               # print("test" ,FindValueArr[x][y])
                if (int(FindValueArr[x][y]) != 0):
                    if(int(FindValueArr[x][y]) < int(minvalue)):
                        minvalue = FindValueArr[x][y]
                        while(y  == len(FindValueArr[0])-1):
                            myARR.append(FindKeyARR[x][y-1])
                       # print("minvalue")
                        continue
