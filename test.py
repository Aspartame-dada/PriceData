from pandas import read_csv
f=open('price.csv')
data=read_csv(f,encoding='utf-8')
data.to_excel('test.xlsx')
