import seaborn as sns
import pandas as pd
from matplotlib.pyplot import title

titanic = sns.load_dataset('titanic')

# 컬럼개수
pd.set_option('display.max_columns', len(titanic.columns))
# 컬럼별 사이즈
pd.set_option('display.max.colwidth', 15)
# 화면 폭 사이즈
pd.set_option('display.width', 1000)


print("# titanic 데이터셋", type(titanic), titanic.head(), sep='\n', end='\n\n')

print("# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기")
df = titanic.loc[:, ['age', 'fare']]
print(df.head(), type(df), sep='\n', end='\n\n')  # 첫 5행만 표시

print("# 데이터프레임에 숫자 10 더하기")
addition = df + 10
print(addition.head(), type(addition), sep='\n')  # 첫 5행만 표시

