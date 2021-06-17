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

df = df.set_index('name')
print(df, sep='\n', end='\n\n')


# df.dropna(axis=0, inplace=True)
# print(df, end='\n\n' )
#

print("# 데이터프레임 df",  df, sep='\n', end='\n\n')
add_dict = {'name': ['test5', 'test6'], 'math': [60, 60], 'eng': [60, 70], 'music': [60, 70], 'kor': [60, 70]}
df_add = pd.DataFrame(add_dict)
print(df_add)


df = df.reset_index()
df = df.append(df_add, ignore_index=True)
df.set_index('name', inplace=True)
print("# 데이터프레임 df",  df, sep='\n', end='\n\n')


mask3 = (df.math >= 80) & (df.music >= 80)
print(df.loc[mask3, :], sep='\n', end='\n\n')

#
# print("df.kor.max() = ", df.kor.max(), ' ', "df.kor.min() = ", df.kor.min(), end='\n')
# print("df.describe()", df.describe(), df.mean(), sep='\n', end='\n\n')
