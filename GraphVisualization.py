# código para demonstrar a biblioteca
# disponível em: https://www.geeksforgeeks.org/visualize-graphs-in-python/

# First networkx library is imported
# along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt
from CsvDataReader import CsvDataReader


# Defining a Class
class GraphVisualization:

    def __init__(self):
        # visual is a list which stores all
        # the set of edges that constitutes a
        # graph
        self.visual = []

    # addEdge function inputs the vertices of an
    # edge and appends it to the visual list
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.savefig("teste.png")
        # plt.show()

    def run_graph_visualization(self, list_to_plot):
        # Driver code
        G = GraphVisualization()
        for edge in list_to_plot:
            G.addEdge(edge[0], edge[1])
        G.visualize()


G = GraphVisualization()
Csv = CsvDataReader('Liu_Kang.csv')
List = Csv.get_pairs()
G.run_graph_visualization(List)
