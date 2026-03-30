class Edge:
    def __init__(self, vertices: list[int], weight: int):
        self.vertices = vertices
        self.weight = weight
    def __repr__(self) -> str:
       return f"{self.vertices[0]}--{self.weight}--{self.vertices[1]}" 

class Vertex:
    def __init__(self, number:int, edges: list[Edge]):
        self.number = number
        self.edges = edges
        self.shortestPath = 0
        for edge in self.edges:
            assert self.number in edge.vertices, f"edge is not connected to vertex {self.number}"
    def updateSP(self, pathValue: int):
        self.shortestPath = pathValue
    def __repr__(self) -> str:
        return f"vertex{self.number} connected to {len(self.edges)} vertices, with shortest path {self.shortestPath}"
class Heap:
    def __init__(self):
        self.vertices = []
        self.hashTable = dict()
    def switchVertices(self, ver1i:int, ver2i:int):
        """
        switches two vertices in a heap following their heap indexes (1 indexing)
        """
        self.hashTable[self.vertices[ver1i-1].number], self.hashTable[self.vertices[ver2i-1].number] = \
        self.hashTable[self.vertices[ver2i-1].number],self.hashTable[self.vertices[ver1i-1].number]
        self.vertices[ver1i-1], self.vertices[ver2i-1] = self.vertices[ver2i-1], self.vertices[ver1i-1]

    def insertVertex(self, vertex):
        self.vertices.append(vertex)
        heap_i = len(self.vertices)
        self.hashTable[vertex.number] = heap_i
        while (self.vertices[heap_i-1].shortestPath < self.vertices[heap_i//2-1].shortestPath) & (heap_i>1):
            self.switchVertices(heap_i,heap_i//2)
            heap_i = heap_i//2
    def retrieveMin(self):
        self.switchVertices(1,len(self.vertices))
        min_vertex = self.vertices.pop()
        del self.hashTable[min_vertex.number]
        heap_i = 1
        while True:
            if heap_i*2+1 <= len(self.vertices):
                if self.vertices[heap_i*2-1].shortestPath < self.vertices[heap_i*2].shortestPath:
                    targetChild = heap_i*2
                else:
                    targetChild = heap_i*2+1
            elif heap_i*2 <= len(self.vertices):
                targetChild = heap_i*2
            else:
                break
            if self.vertices[heap_i-1].shortestPath > self.vertices[targetChild-1].shortestPath:
                self.switchVertices(heap_i,targetChild)
                heap_i = targetChild
            else:
                break
        return min_vertex
    def __repr__(self):
        output_string = ""
        for i in range(min(20, len(self.vertices))):
            output_string += str(self.vertices[i].shortestPath)+"   "
            if i in {0, 2, 6, 12}:
                output_string += "\n"
        return output_string
    def deleteVertex(self, vertex_number):
        heap_i = self.hashTable[vertex_number]
        self.switchVertices(heap_i,len(self.vertices))
        del self.vertices[-1]
        del self.hashTable[vertex_number]
        while True:
            if heap_i*2+1 <= len(self.vertices):
                if self.vertices[heap_i*2-1].shortestPath < self.vertices[heap_i*2].shortestPath:
                    targetChild = heap_i*2
                else:
                    targetChild = heap_i*2+1
            elif heap_i*2 <= len(self.vertices):
                targetChild = heap_i*2
            else:
                break
            if self.vertices[heap_i-1].shortestPath > self.vertices[targetChild-1].shortestPath:
                self.switchVertices(heap_i,targetChild)
                heap_i = targetChild
            else:
                break



graph = dict()

with open('problem9.8.txt', 'r') as file:
    lines = [_.strip().split('\t') for _ in file.readlines()]
    for line in lines:
        edges = [Edge([int(line[0]),int(line[i].split(',')[0])], 
                      int(line[i].split(',')[1])) for i in range(1,len(line))]
        number = int(line[0])
        graph[number] = Vertex(number,edges)
    # print(graph)

treated_vertices = set()
treated_vertices.add(graph[1])
graph[1].shortestPath = 0
dijkstra_heap = Heap()
for edge in graph[1].edges:
    graph[edge.vertices[1]].shortestPath = \
            graph[edge.vertices[0]].shortestPath + edge.weight
    dijkstra_heap.insertVertex(graph[edge.vertices[1]])
# print(dijkstra_heap)

while len(graph)>len(treated_vertices):
    vertex_to_treat = dijkstra_heap.retrieveMin()
    treated_vertices.add(vertex_to_treat)
    # print(f"{vertex_to_treat} treated")
    # print(dijkstra_heap)
    # print(graph)
    for edge in vertex_to_treat.edges:
        if not(graph[edge.vertices[1]] in treated_vertices):
            if edge.vertices[1] in dijkstra_heap.hashTable:
                if graph[edge.vertices[0]].shortestPath + edge.weight <  graph[edge.vertices[1]].shortestPath:
                    dijkstra_heap.deleteVertex(edge.vertices[1])
                    graph[edge.vertices[1]].shortestPath = graph[edge.vertices[0]].shortestPath + edge.weight 
                    dijkstra_heap.insertVertex(graph[edge.vertices[1]])
            else:
                graph[edge.vertices[1]].shortestPath = graph[edge.vertices[0]].shortestPath + edge.weight 
                dijkstra_heap.insertVertex(graph[edge.vertices[1]])

print([graph[i].shortestPath for i in [7,37,59,82,99,115,133,165,188,197]])

    

# graph[1].shortestPath = 8
#
# graph[2].shortestPath = 3
# graph[3].shortestPath = 2
# graph[4].shortestPath = 5
# graph[5].shortestPath = 4
# graph[6].shortestPath = 7
# graph[7].shortestPath = 13
# graph[8].shortestPath = 1
# test_heap = Heap()
# for i in range(1,9):
#     test_heap.insertVertex(graph[i])
# print(test_heap)
# min_vertex = test_heap.retrieveMin()
# print(f"min_vertex is {min_vertex}")
#
# print(test_heap)
# min_vertex = test_heap.retrieveMin()
# print(f"min_vertex is {min_vertex}")
#
# print(test_heap)
# min_vertex = test_heap.retrieveMin()
# print(f"min_vertex is {min_vertex}")

# test_heap.deleteVertex(3)
# print(test_heap)
