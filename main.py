import pandas
from pandas import DataFrame


numpy_array_reversed = pandas.read_csv("CustomerNumbers_4210_backup.csv").values[::-1]

df = pandas.DataFrame(numpy_array_reversed)

df.to_csv("customers_4210_reversed.csv")