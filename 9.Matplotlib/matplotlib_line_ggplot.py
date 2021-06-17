import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 디스플레이 설정 변경
pd.set_option('display.max_columns', 10)    # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', 20)   # 출력할 열의 너비
pd.set_option('display.unicode.east_asian_width', True)  # 유니코드 사용 너비 조정
pd.set_option('display.width', 600)  # 콘솔 출력 너비

# matplotlib 한글 폰트 오류 문제 해결
font_path = "./malgun.ttf"   #폰트파일의 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# Excel 데이터를 데이터프레임 변환
df = pd.read_excel('시도별 전출입 인구수.xlsx', header=0)
print("시도별 전출입 인구수", df.head(), sep='\n', end='\n\n')

# 누락값(NaN)을 앞 데이터로 채움 (엑셀 양식 병합 부분)
df = df.fillna(method='ffill')

print("시도별 전출입 인구수", df.head(), sep='\n', end='\n\n')

# 서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)
print("서울에서 다른 지역으로 이동한 데이터", df_seoul.head(), sep='\n', end='\n\n')

# 서울에서 경기도로 이동한 인구 데이터 값만 선택
sr_one = df_seoul.loc['경기도']
print("서울에서 경기도로 이동한 인구 데이터 값만 선택", sr_one.head(), sep='\n', end='\n\n')

# 스타일 서식 지정
# [print(style) for style in plt.style.available]
plt.style.use('ggplot')

# 그림 사이즈 지정
plt.figure(figsize=(14, 5))

# x축 눈금 라벨 회전하기
plt.xticks(size=10, rotation='vertical')

# x, y축 데이터를 plot 함수에 입력
plt.plot(sr_one.index, sr_one.values, marker='o', markersize=10)  # 마커 표시 추가
plt.title('서울 -> 경기 인구 이동', size=30)  # 차트 제목

plt.xlabel('기간', size=20)  # x축 이름
plt.ylabel('이동 인구수', size=20)  # y축 이름

plt.legend(labels=['서울 -> 경기'], loc='best', fontsize=15)  # 범례 표시
plt.show()
