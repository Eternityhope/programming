import pandas as pd

df = pd.DataFrame({'인덱스':['index1', 'index2', 'index3'],'이름':['A', 'B', 'C'], 'ID':['AAA', 'BBB', 'CCC'], '나이':[20, 25, 41]})

print(df)

column_1 = df.loc[:, '이름':'ID'] #slice 사용
print(column_1)

row_index_1 = df.iloc[2] # range 사용
print(row_index_1)






