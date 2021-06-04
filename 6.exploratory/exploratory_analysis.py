import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 컬럼개수
pd.set_option('display.max_columns', len(df.columns))
# 컬럼별 사이즈
pd.set_option('display.max.colwidth', 30)
# 화면 폭 사이즈
pd.set_option('display.width', 1000)

# 열 이름을 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']
print("# 데이터프레임 df의 내용을 일부 확인", end='\n\n')
print("df.head()", df.head(), sep='\n', end='\n\n')  # 처음 5개의 행
print("df.tail()", df.tail(), sep='\n', end='\n\n')  # 마지막 5개의 행

print("# df의 모양과 크기 확인: (행의 개수, 열의 개수)를 투플로 반환")
print(df.shape, sep='\n', end='\n\n')

print("# 데이터프레임 df의 내용 확인")
print(df.info(), sep='\n', end='\n\n')

print("# 데이터프레임 df의 자료형 확인")
print(df.dtypes, sep='\n', end='\n\n')

print("# 시리즈(mog 열)의 자료형 확인")
print(df.mpg.dtypes, sep='\n', end='\n\n')

print("# 데이터프레임 df의 기술통계 정보 확인")
print(df.describe(), df.describe(include='all'), sep='\n', end='\n\n')

print("# 데이터프레임 df의 각 열이 가지고 있는 원소 개수 확인")
print(df.count(), sep='\n', end='\n\n')

print("# df.count()가 반환하는 객체 타입 출력")
print(type(df.count()), sep='\n', end='\n\n')

print("# 데이터프레임 df의 특정 열이 가지고 있는 고유값 확인")
unique_values = df['origin'].value_counts()  # origin 제조국가
print(unique_values, sep='\n', end='\n\n')

print("# value_counts 메소드가 반환하는 객체 타입 출력")
print(type(unique_values), sep='\n', end='\n\n')
