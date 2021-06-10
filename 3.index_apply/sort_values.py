import pandas as pd
from test_data import dict_data

print("# 딕셔서리를 데이터프레임으로 변환. 인덱스를 [r0, r1, r2]로 지정")
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df, end='\n\n')

print("# c1 열을 기준으로 내림차순 정렬")
ndf = df.sort_values(by='c1', ascending=False)
print(ndf)
