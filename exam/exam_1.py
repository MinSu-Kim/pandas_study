import pandas as pd

exam_data = {'name': ['test1', 'test2', 'test3'],
             'math': [90, 80, 70],
             'eng': [98, 89, 95],
             'music': [85, 95, 100],
             'kor': [100, 90, 90]
             }

df = pd.DataFrame(exam_data)
print(df)
print()

# df.set_index('name', inplace=True)
# print(df, sep='\n', end='\n\n')

df = df.set_index('name')
print(df, sep='\n', end='\n\n')

# sr_math = df.math
# print('math', sr_math, type(sr_math), sep='\n', end='\n\n')

sr_test1 = df.loc['test1']
print(sr_test1, sep='\n', end='\n\n')
print(df.loc['test1'], sep='\n', end='\n\n')

sr_eng = df['eng']
print(sr_eng)
print(df.eng)
print()

print("# 데이터프레임 df",  df, sep='\n', end='\n\n')

add_dict = {'name': 'test4', 'math': None, 'eng': 99, 'music':99, 'kor':99}
sr_add = pd.Series(add_dict, name=add_dict['name'])
print(sr_add)
df = df.reset_index()
df = df.append(sr_add, ignore_index=True)
df.set_index('name', inplace=True)

print("# 데이터프레임 df",  df, sep='\n', end='\n\n')

result2 = df.apply(lambda x: x.isnull(), axis=0)
print(result2, type(result2), sep='\n', end='\n\n')

df.dropna(axis=0, inplace=True)
print(df, end='\n\n' )

mask3 = (df.math >= 90) & (df.music >= 60)
print(df.loc[mask3, :], sep='\n', end='\n\n')

print("df.kor.max() = ", df.kor.max(), ' ', "df.kor.min() = ", df.kor.min(), end='\n')
print("df.describe()", df.describe(), df.mean(), sep='\n', end='\n\n')


print("# 데이터프레임 df",  df, sep='\n', end='\n\n')
add_dict = {'name': ['test5', 'test6'], 'math': [60, 60], 'eng': [60, 70], 'music': [60, 70], 'kor': [60, 70]}
df_add = pd.DataFrame(add_dict)

print(df_add)
df = df.reset_index()
df = df.append(df_add, ignore_index=True)
df.set_index('name', inplace=True)
print("# 데이터프레임 df",  df, sep='\n', end='\n\n')