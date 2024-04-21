import pandas
result = pandas.read_csv('data.csv',delimiter=',')
print(result)
print("****************************")
print(result.shape)

print(result.columns)
print(result.head(2))
print(type(result))



