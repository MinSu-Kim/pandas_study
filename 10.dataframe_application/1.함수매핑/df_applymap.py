import seaborn as sns
import pandas as pd

pd.set_option('display.max_columns', 15)  # 출력할 최대 열의 개수
pd.set_option('display.width', 600)       # 출력 전체폭 너비

print("# titanic 데이터셋에서 데이터프레임 만들기")
titanic = sns.load_dataset('titanic')
print('titanic', titanic.head(), sep='\n', end='\n\n')

print("# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기")
df = titanic.loc[:, ['age', 'fare']]
print(df.head())
print()


# 사용자 함수 정의
def add_10(n):  # 10을 더하는 함수
    return n + 10


print("# 데이터프레임에 applymap()으로 add_10() 함수를 매핑 적용")
df_map = df.applymap(add_10)
print(df_map.head(), end='\n\n')

print("# 데이터프레임에 applymap()으로 lambda 함수를 매핑 적용")
print(df_map.applymap(lambda x : x - 10).head())
