import pandas as pd

# 중복 데이터를 갖는 데이터프레임 만들기
df = pd.DataFrame(
    {
        'c1': ['a', 'a', 'b', 'a', 'b'],
        'c2': [1, 1, 1, 2, 2],
        'c3': [1, 1, 2, 2, 2]
    }
)
print('df', df, sep='\n', end='\n\n')

print("# 데이터프레임 전체 행 데이터 중에서 중복값 찾기")
print(df.duplicated(), sep='\n', end='\n\n')

print("# 데이터프레임의 특정 열 데이터에서 중복값 찾기")
print(df['c2'].duplicated(), sep='\n', end='\n\n')
