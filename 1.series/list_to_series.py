import pandas as pd

list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
list_index = [1, 2, 3, 4, 5]
sr = pd.Series(list_data, index=list_index)

print("리스트를 시리즈로 변환하여 변수 sr에 저장", sr, sep='\n', end='\n\n')