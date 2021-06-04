import pandas as pd

list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
sr = pd.Series(data=list_data, index=['a', 'b', 'c', 'd', 'e'])

print(sr, sep='\n', end='\n\n')

print(type(sr.index), sr.index, sep='\n', end='\n\n')
print(type(sr.values), sr.values, sep='\n', end='\n\n')