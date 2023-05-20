import pandas as pd

def read_specific_columns_by_index(file_path, column_indices):
    # Read specific columns of a csv file using Pandas
    df = pd.read_csv(file_path, sep='\t', usecols=column_indices, encoding=encoding)

    return df

file_path = 'transactions-and-notes-export.csv'  # replace with your file path
column_indices = [0, 1, 5, 6, 7, 9, 10, 14, 15, 16, 17, 18, 19, 27]  # replace with the indices of the columns you want to read
encoding = 'utf-16'  # replace with the encoding of your file

data = read_specific_columns_by_index(file_path, column_indices)

print(data)
