import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# 한글 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # '맑은 고딕'으로 설정,
matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('./남북한발전전력량.xlsx')  # 데이터프레임 변환

pd.set_option('display.max_columns', len(df.columns))
pd.set_option('display.max.colwidth', 30)
pd.set_option('display.width', 1000)

print("남북한발전전력량", df, type(df.iloc[0, 2]), sep='\n', end='\n\n')

df_ns = df.iloc[[0, 5], 2:]  # 남한, 북한 발전량 합계 데이터만 추출
df_ns.index = ['South', 'North']  # 행 인덱스 변경
df_ns.columns = df_ns.columns.map(int)  # 열 이름의 자료형을 정수형으로 변경

print("남북한발전전력량", df_ns.head(), sep='\n', end='\n\n')

# 선 그래프 그리기
df_ns.plot(title="선 그래프 그리기")
# 행, 열 전치하여 다시 그리기
tdf_ns = df_ns.T
print(tdf_ns.head())

# plt.subplot(132)
tdf_ns.plot(title="행, 열 전치하여 다시 그리기")
tdf_ns.plot(kind='bar', title="남북한 발전 전력량")
plt.show()
