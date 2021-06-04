import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression  # sklearn 라이브러리에서 선형회귀분석 모듈 가져오기
from sklearn.model_selection import train_test_split  # train data 와 test data로 구분(7:3 비율)

# 디스플레이 설정
pd.set_option('display.max_columns', 15)  # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', 30)  # 출력할 열의 너비
pd.set_option('display.width', 600)  # 콘솔 출력 너비

'''
[Step 1] 데이터 준비 - read_csv() 함수로 자동차 연비 데이터셋 가져오기
'''
print("[Step 1] 데이터 준비", end='\n\n')

df = pd.read_csv('./auto-mpg.csv', header=None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin',
              'name']
print("read_csv() 함수로 자동차 연비 데이터셋 가져오기", df.head(), sep='\n', end='\n\n')

'''
[Step 2] 데이터 탐색
'''

# 데이터 자료형 확인
print("[Step 2] 데이터 탐색", end='\n\n')
print("데이터 자료형 확인", end='\n')
print(df.info(), sep='\n', end='\n\n')

# 데이터 통계 요약정보 확인
print("데이터 통계 요약정보 확인", end='\n')
print(df.describe(), sep='\n', end='\n\n')

# horsepower 열의 자료형 변경 (문자열 ->숫자)
print("horsepower 열의 고유값 확인", df['horsepower'].unique(), sep='\n', end='\n\n')  # horsepower 열의 고유값 확인
df['horsepower'].replace('?', np.nan, inplace=True)  # '?'을 np.nan으로 변경
df.dropna(subset=['horsepower'], axis=0, inplace=True)  # 누락데이터 행을 삭제
df['horsepower'] = df['horsepower'].astype('float')  # 문자열을 실수형으로 변환
print(df.describe(), end='\n\n')  # 데이터 통계 요약정보 확인

'''
[Step 3] 속성(feature 또는 variable) 선택
'''
print("[Step 3] 속성(feature 또는 variable) 선택", end='\n\n')

# 분석에 활용할 열(속성)을 선택 (연비, 실린더, 출력, 중량)
ndf = df[['mpg', 'cylinders', 'horsepower', 'weight']]
print("분석에 활용할 열(속성)을 선택 (연비, 실린더, 출력, 중량)", ndf.head(), sep='\n', end='\n\n')

# 종속 변수 Y인 "연비(mpg)"와 다른 변수 간의 선형관계를 그래프(산점도)로 확인
for v in ['cylinders', 'horsepower', 'weight']:
    ndf.plot(kind='scatter', x=v, y='mpg', c='coral', s=10, figsize=(10, 5))
    plt.show()
    plt.close()

# seaborn으로 산점도 그리기
fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)

sns.regplot(x='weight', y='mpg', data=ndf, ax=ax1)  # 회귀선 표시
sns.regplot(x='cylinders', y='mpg', data=ndf, ax=ax2)  # 회귀선 표시
sns.regplot(x='horsepower', y='mpg', data=ndf, ax=ax3)  # 회귀선 표시
plt.show()
plt.close()

"""
# seaborn 조인트 그래프 - 산점도, 히스토그램
sns.jointplot(x='weight', y='mpg', data=ndf)              # 회귀선 없음
sns.jointplot(x='weight', y='mpg', kind='reg', data=ndf)  # 회귀선 표시
plt.show()
plt.close()

# seaborn pariplot으로 두 변수 간의 모든 경우의 수 그리기
sns.pairplot(ndf)
plt.show()
plt.close()
"""

'''
Step 4: 데이터셋 구분 - 훈련용(train data)/ 검증용(test data)
'''
print("Step 4: 데이터셋 구분 - 훈련용(train data)/ 검증용(test data)", end='\n\n')

# 속성(변수) 선택
X = ndf[['weight']]  # 독립 변수 X
y = ndf['mpg']  # 종속 변수 Y

X_train, X_test, y_train, y_test = train_test_split(X,  # 독립 변수
                                                    y,  # 종속 변수
                                                    test_size=0.3,  # 검증 30%
                                                    random_state=10)  # 랜덤 추출 값

print('train data 개수: ', len(X_train))
print('test data 개수: ', len(X_test))
print()

'''
Step 5: 단순회귀분석 모형 - sklearn 사용
'''
print("Step 5: 단순회귀분석 모형 - sklearn 사용", end='\n\n')

# 단순회귀분석 모형 객체 생성
lr = LinearRegression()

# train data를 가지고 모형 학습
lr.fit(X_train, y_train)

# 학습을 마친 모형에 test data를 적용하여 결정계수(R-제곱) 계산
print("학습을 마친 모형에 test data를 적용하여 결정계수(R-제곱) 계산", end='\n\n')
r_square = lr.score(X_test, y_test)
print("r_square : ", r_square, sep=' ', end='\n\n')

# 회귀식의 기울기
print('회귀식의 기울기 a: ', lr.coef_, sep=' ', end='\n\n')

# 회귀식의 y절편
print('회귀식의 y 절편 b: ', lr.intercept_, sep=' ', end='\n\n')

# 모형에 전체 X 데이터를 입력하여 예측한 값 y_hat을 실제 값 y와 비교
print("모형에 전체 X 데이터를 입력하여 예측한 값 y_hat을 실제 값 y와 비교 ")

y_hat = lr.predict(X)

plt.figure(figsize=(10, 5))
ax1 = sns.distplot(y, hist=False, label="y")
ax2 = sns.distplot(y_hat, hist=False, label="y_hat", ax=ax1)
plt.show()
plt.close()
