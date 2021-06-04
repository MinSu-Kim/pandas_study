import pandas as pd

df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']], index=['준서', '예은'],  columns=['나이', '성별', '학교'])
print('행 인덱스/열 이름 지정하여, 데이터프레임 만들기',df, df.index, df.columns, sep='\n', end='\n\n')

df.index = ['학생1', '학생2']
df.columns = ['연령', '남녀', '소속']
print('행 인덱스, 열 이름 변경하기', df, df.index, df.columns, sep='\n', end='\n\n')

df.rename(columns={'연령': '나이', '남녀': '성별', '소속':'학교'}, inplace=True)
print("열 이름 중, '연령'를 '나이'으로, '남녀'를 '성별'로, '소속'을 '학교'으로 바꾸기")
print(df, df.index, df.columns, sep='\n', end='\n\n')

df.rename(index={'학생1': '준서', '학생2':'예은'}, inplace=True)
print("df의 행 인덱스 중에서, '학생1'을'준서'로, '학생2'를 '예은'로 바꾸기")
print(df, df.index, df.columns, sep='\n', end='\n\n')

