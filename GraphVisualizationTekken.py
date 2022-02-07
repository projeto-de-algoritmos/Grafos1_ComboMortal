# código para demonstrar a biblioteca
# disponível em: https://www.geeksforgeeks.org/visualize-graphs-in-python/
# combos disponíveis em: http://tekken7combo.kagewebsite.com/

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
    def add_edge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize_full_graph(self):
        G = nx.DiGraph()
        G.add_edges_from(self.visual)
        pos = graphviz_layout(G, prog="dot")
        nx.draw(G, pos, with_labels=True, arrowstyle='-|>', arrows=True, node_color="Red")
        plt.savefig(Character + '.png')
        plt.clf()

    def visualize_graph_from_combo(self, command):
        G = nx.DiGraph()
        G.add_edges_from(self.visual)
        T = nx.dfs_tree(G, source=command)
        pos = graphviz_layout(T, prog="dot")
        nx.draw(T, pos, with_labels=True, arrowstyle='-|>', arrows=True)
        plt.savefig('Possibilidades_' + Character + '_from_combo_n:' + str(NumCombo) + '.png')
        plt.clf()

    def add_all_edges(self, list_of_combos):
        G = GraphVisualization()
        for combo in list_of_combos:
            for commands in combo:
                is_not_last_element = combo.index(commands) + 1 < len(combo)
                if is_not_last_element:
                    actual_commands = combo[combo.index(commands)]
                    next_commands = combo[combo.index(commands)+1]
                    G.add_edge(actual_commands, next_commands)

        return G


G = GraphVisualization()
Character = input("Digite o nome do personagem que deseja ver os combos:  ")
print('==================================')
NumCombo = int(input("Digite a partir de qual combo deseja ver as possibilidades:  "))
Csv = CsvDataReader('./tekken/' + Character + '.csv')
ListOfCombos = Csv.get_rows_of_file()
FirstCommandFromCombo = Csv.get_first_command_of_file(NumCombo)
G = G.add_all_edges(ListOfCombos)
G.visualize_graph_from_combo(FirstCommandFromCombo)
G.visualize_full_graph()

