class edge:
    def __init__(self, vertices: list[int], weight: int):
        self.vertices = vertices
        self.weight = weight
    def __repr__(self) -> str:
       return f"{self.vertices[0]}--{self.weight}--{self.vertices[1]}" 

class vertex:
    def __init__(self, number:int, edges: list[edge]):
        self.number = number
        self.edges = edges
        for edge in self.edges:
            assert self.number in edge.vertices, f"edge is not connected to vertex {self.number}"
    def __repr__(self) -> str:
        return f"vertex{self.number} connected to {len(self.edges)} vertices"

def main:
    graph = dict()
with open('problem9.8test.txt', 'r') as file:
    lines = [_.strip().split('\t') for _ in file.readlines()]
    for line in lines:
        edges = [edge([int(line[0]),int(line[i].split(',')[0])],int(line[i].split(',')[1])) for i in range(1,len(line))]
        number = int(line[0])
        graph[number] = vertex(number,edges)
    print(graph)


