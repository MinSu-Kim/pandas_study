import pandas as pd

list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
list_index = ['a', 'b', 'c', 'd', 'e']
sr = pd.Series(data=list_data, index=list_index)

print(sr, sep='\n', end='\n\n')

print(type(sr.index), sr.index, sep='\n', end='\n\n')
print(type(sr.values), sr.values, sep='\n', end='\n\n')