lpgtimport requests
import numpy as np
API_KEY = "DD"
print("Minuim Spanning tree")
x = int(input("please enter the number of sites for the visit,max and min is 4:"))
k = 2
l = 2
sites1 = []
sites2 = []
if x == 4 and x >= 0:
    i = 0
    j = 0
    for i in range(k):
        location1_value = str(input("Please enter the location of your sites:"))
        sites1.append(location1_value)
        i = i + 1
    for j in range(l):
        location2_value = str(input("please enter your site locations"))
        sites2.append(location2_value)
        j = j + 1
else:
    print("Invalid amount of sites")
class Edge:
    def __init__(self,u,v,weight):
        self.u = u
        self.v = v
        self.weight = weight
def getlocation_distance(loc1,loc2):
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={loc1}&destinations={loc2}&key={API_KEY}"
    response  = requests.get(url).json()
    if response['status'] == 'OK':
        distance = response['rows'][0]["elements"][0][distance]['value']
        return distance
edges1_ultimate_final = []
edges2 = []
for i in range(len(sites1)):
    for j in range(len(sites2)):
        loc1 = sites1[i]
        loc2 = sites2[j]
        distance = getlocation_distance(loc1,loc2)
        edge1 = Edge(loc1,loc2,distance)
        edges1_ultimate_final.append(edge1)
        j = j + 1
    i = i + 1 
y = 0
r = 1
loc1 = sites1[y]
loc2 = sites1[r]
distance_critical = getlocation_distance(loc1,loc2)
edge3 = Edge(loc1,loc2,distance_critical)
edges1_ultimate_final.append(edge3)   
for i in range(len(sites2)):
    for j in range(len(sites1)):
        loc1 = sites2[i]
        loc2 = sites2[j]
        distance2 = getlocation_distance(loc1,loc2)
        edge2 = Edge(loc1,loc2,distance2)
        edges2.append(edge2)
        j = j + 1
    i = i + 1
b = 0
z = 1
loc1 = sites2[b]
loc2 = sites2[z]
distance_crtical2 = getlocation_distance(loc1,loc2)
edge4 = Edge(loc1,loc2,distance_crtical2)
edges2.append(edge4)
edges1_ultimate_final.append(edge4)
for edge in edges1_ultimate_final:
    for edge2 in edges2:
        if edge.u == edges2.v and edge.v == edge2.u and edge.weight == edge2.weight:
            print('No error found')
print(edges1_ultimate_final)
print("Are this these all the sites you entered, please say yes or no")
answer = str(input('Your response here:'))
answer2 = str(input("is this is a direted graph, say yes or no:"))
if answer == 'yes' and answer2 == 'no':
    nodes = sorted({edge.u for edge in edges1_ultimate_final}.union({edge.v for edge in edges1_ultimate_final}))
    node_index = {node:i for i,node in enumerate(nodes)}
    n = len(nodes)
    matrix = [[1 * n for _ in range(n)] for _ in range(n)]\
    for i,j in range(n):
        matrix[i][j] = 0
    for edge in edges1_ultimate_final:
        i = node_index[edge.u]
        j = node_index[edge.v]
        matrix[i][j] = matrix[j][i] = edge.weight
    nmatrix = np.matrix
    mst = []
    posotion_index = 0
    history_index_column = [posotion_index]
    while len(nmatrix) >= 1:
        element = float("inf")
        s = -1
        for col in history_index_column:
            for index,row in enumerate(nmatrix):
               if row[col] < element and row[col] != 0:
                element  = row[col]
                s = index
        mst.append(element)
        posotion_index = s
        history_index_column.append(posotion_index)
        nmatrix = np.delete(nmatrix,s,axis=0)
    print("this is your minuim spanning tree")
    print(mst)
    final_mst = []
    for edge,i in edges1_ultimate_final:
        if edge.weight == mst[i]:
            mst[i] = j
            final_mst.append(edge.weight)
            final_mst.append(j)
    print("Your minuium spanning tree with nodes is")
    print(final_mst)
else:
    if answer == 'no':
        print("please reasure all your inputs")
    else:
        print("please use google maps it provides this service")
