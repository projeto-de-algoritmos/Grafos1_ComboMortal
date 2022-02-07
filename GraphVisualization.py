import networkx as nx
import matplotlib.pyplot as plt
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
    def add_edge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list

    def visualize_full_graph(self, character):
        G = nx.DiGraph()
        G.add_edges_from(self.visual)
        pos = graphviz_layout(G, prog="dot")
        nx.draw(G, pos, with_labels=True, arrowstyle='-|>', arrows=True, node_color="salmon")
        plt.savefig(character + '.png')
        plt.clf()

    def visualize_graph_from_combo(self, command, character, numCombo):
        G = nx.DiGraph()
        G.add_edges_from(self.visual)
        T = nx.dfs_tree(G, source=command)
        pos = graphviz_layout(T, prog="dot")
        nx.draw(T, pos, with_labels=True, arrowstyle='-|>', arrows=True)
        plt.savefig('Possibilidades_' + character + '_from_combo_n' + str(numCombo + 1) + '.png')
        plt.clf()

    def add_all_edges(self, listOfCombos):
        G = GraphVisualization()
        for combo in listOfCombos:
            for commands in combo:
                is_not_last_element = combo.index(commands) + 1 < len(combo)
                if is_not_last_element:
                    actual_commands = combo[combo.index(commands)]
                    next_commands = combo[combo.index(commands)+1]
                    G.add_edge(actual_commands, next_commands)

        return G