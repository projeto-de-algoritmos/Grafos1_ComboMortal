# código para demonstrar a biblioteca
# disponível em: https://www.geeksforgeeks.org/visualize-graphs-in-python/

# First networkx library is imported
# along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt
from CsvDataReaderTekken import CsvDataReader
from networkx.drawing.nx_pydot import graphviz_layout


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
        pos = graphviz_layout(G, prog="dot")
        nx.draw(G, pos, with_labels=True, node_color="Red")
        plt.savefig("tekken.png")

    def run_graph_visualization(self, list_of_combos):
        # Driver code
        G = GraphVisualization()
        for combo in list_of_combos:
            # actual_command = 0
            # next_command = 1
            for commands in combo:
                is_not_last_element = combo.index(commands) + 1 < len(combo)
                if is_not_last_element:
                    actual_commands = combo[combo.index(commands)]
                    next_commands = combo[combo.index(commands)+1]
                    G.addEdge(actual_commands, next_commands)

        G.visualize()


G = GraphVisualization()
Csv = CsvDataReader('./tekken/Alisa.csv')
List = Csv.get_rows_of_file()
G.run_graph_visualization(List)
