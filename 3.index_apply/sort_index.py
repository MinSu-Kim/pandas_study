import pandas as pd
from test_data import dict_data

print("# 딕셔서리를 데이터프레임으로 변환. 인덱스를 [r0, r1, r2]로 지정")
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df, end='\n\n')

print("# 내림차순으로 행 인덱스 정렬")
ndf = df.sort_index(ascending=False)
print(ndf, end='\n\n')
