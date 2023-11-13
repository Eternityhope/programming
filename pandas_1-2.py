import pandas as pd

df_1 = pd.DataFrame({'월':[1,2,1,2,1],'야근':[1,3,7,10,2],'휴일':[8,4,10,15,3],'수당':[100,200,30,400,250]})

print(df_1)

df_avr = df_1.groupby("월").mean() #groupby를 활용한 월별 평균값
print(df_avr)

dict_data = {'국적':['한국', '일본', '중국', '미국', '중국', '한국', '미국', '러시아', '한국', '한국', '이탈리아'], 
'연봉':[4000, 6200, 2500, 8600, 3000, 5600, 6800, 3800, 5200, 3300, 4400]}
df_2 = pd.DataFrame(dict_data)

print(df_2)

print(df_2.groupby(['국적']).agg(['mean', 'max'])) #aggregate 메소드 활용