import csv


class CsvDataReader:
    def __init__(self, file_name):
        self.file = open(file_name)
        type(self.file)
        self.csvreader = csv.reader(self.file)

        self.rows = []
        for row in self.csvreader:
            self.rows.append(row)
        self.file.close()

    def print_df(self):
        print(self.rows)

    def get_rows_of_file(self):
        return self.rows

