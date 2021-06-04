import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_excel('./남북한발전전력량.xlsx')

pd.set_option('display.max_columns', len(df.columns))
pd.set_option('display.max.colwidth', 30)
pd.set_option('display.width', 1000)
#pd.set_option('display.unicode.east_asian_width', True)  # 유니코드 사용 너비 조정

df_ns = df.iloc[[0, 5], 3:]  # 남한, 북한 발전량 합계 데이터만 추출
df_ns.index = ['South', 'North']  # 행 인덱스 변경
df_ns.columns = df_ns.columns.map(int)  # 열 이름의 자료형을 정수형으로 변경

tdf_ns = df_ns.T
print(tdf_ns.head())

# 한글 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # '맑은 고딕'으로 설정,
matplotlib.rcParams['axes.unicode_minus'] = False

tdf_ns.plot(kind='hist', title='남북한 발전 전력량')
plt.show()
