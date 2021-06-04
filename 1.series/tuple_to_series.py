import pandas as pd
# 투플을 시리즈로 변환(index 옵션에 인덱스 이름을 지정)
tup_data = ('영인', '2010-05-01', '여', True)
tup_index = ['이름', '생년월일', '성별', '학생여부']

sr = pd.Series(tup_data, index=tup_index)

print("투플을 시리즈로 변환", sr, sep='\n', end='\n\n')
[print(f'{i:10} : {v}') for i, v in sr.items()]
