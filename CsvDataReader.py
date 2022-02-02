import pandas as pd


class CsvDataReader:
    def __init__(self, file_name):
        self.df = pd.read_csv(file_name)
        self.df.fillna('', inplace=True)
        self.inputs_list = []

    def print_df(self):
        print(self.df)

    def get_pairs(self):

        self.n = 0

        # essa parte do código vai ter que ser alterada pois só funciona para 3 colunas, temos que fazer um código modular

        for line in self.df.input_1:
            if self.df.input_1[self.n] != '' and self.df.input_1[self.n] != '':
                self.inputs_list.append([self.df.input_1[self.n], self.df.input_2[self.n]])

            if self.df.input_2[self.n] != '' and self.df.input_3[self.n] != '':
                self.inputs_list.append([self.df.input_2[self.n], self.df.input_3[self.n]])

            self.n += 1

        return self.inputs_list
