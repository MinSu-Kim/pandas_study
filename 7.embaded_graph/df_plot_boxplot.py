import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

pd.set_option('display.max_columns', len(df.columns))
pd.set_option('display.max.colwidth', 30)
pd.set_option('display.width', 1000)

# 열 이름을 지정
df.columns = [
    'mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
    'acceleration', 'model year', 'origin', 'name'
]

# 한글 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # '맑은 고딕'으로 설정,
matplotlib.rcParams['axes.unicode_minus'] = False

print("auto-mpg", df.head(), sep='\n', end='\n\n')

# 열을 선택하여 박스 플롯 그리기
df[['mpg', 'cylinders']].plot(kind='box', title='연비의 분포 및 실린더개수 분포')
plt.show()

