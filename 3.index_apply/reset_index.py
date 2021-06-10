from test_data import dict_data
import pandas as pd

print("# 딕셔서리를 데이터프레임으로 변환. 인덱스를 [r0, r1, r2]로 지정")
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df, end='\n\n')

print("# 행 인덱스를 정수형으로 초기화")
ndf = df.reset_index()
print(ndf, end='\n\n')
