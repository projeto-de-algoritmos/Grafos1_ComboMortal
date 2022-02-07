# código para demonstrar a biblioteca
# disponível em: https://www.geeksforgeeks.org/visualize-graphs-in-python/
# busca em profundidade disponivel: https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.traversal.depth_first_search.dfs_tree.html#networkx.algorithms.traversal.depth_first_search.dfs_tree
# combos disponívem em: https://criticalhits.com.br/games/mortal-kombat-9-todos-os-combos-de-cada-personagem/

# First networkx library is imported
# along with matplotlib

from CsvDataReader import CsvDataReader
from GraphVisualization import GraphVisualization

G = GraphVisualization()
character = input("Digite o nome do personagem que deseja ver os combos:  ")
print('==================================')
numCombo = int(input("Digite a partir de qual combo deseja ver as possibilidades:  ")) - 1
Csv = CsvDataReader('./characters/' + character + '.csv')
listOfCombos = Csv.get_rows_of_file()
firstCommandFromCombo = Csv.get_first_command_of_file(numCombo)
G = G.add_all_edges(listOfCombos)
G.visualize_graph_from_combo(firstCommandFromCombo, character, numCombo)
G.visualize_full_graph(character)
