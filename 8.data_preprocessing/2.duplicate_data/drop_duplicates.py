import pandas as pd

# 중복 데이터를 갖는 데이터프레임 만들기
df = pd.DataFrame({'c1': ['a', 'a', 'b', 'a', 'b'],
                   'c2': [1, 1, 1, 2, 2],
                   'c3': [1, 1, 2, 2, 2]})
print('df', df, sep='\n', end='\n\n')

df2 = df.drop_duplicates()
print("# 데이터프레임에서 중복 행을 제거", df2, sep='\n', end='\n\n')

df3 = df.drop_duplicates(subset=['c2', 'c3'])
print("# c2, c3열을 기준으로 중복 행을 제거", df3, sep='\n', end='\n\n')
