from test_data import dict_data
import pandas as pd

print("# 딕셔서리를 데이터프레임으로 변환. 인덱스를 [r0, r1, r2]로 지정")
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df, end='\n\n')

print("# 인덱스를 [r0, r1, r2, r3, r4]로 재지정")
new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf = df.reindex(new_index)
print(ndf, end='\n\n')

print("# reindex로 발생한 NaN값을 숫자 0으로 채우기")
new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf2 = df.reindex(new_index, fill_value=0)
print(ndf2, end='\n\n')