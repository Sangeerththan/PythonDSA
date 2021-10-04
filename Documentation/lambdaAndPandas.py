import pandas as pd
df = pd.DataFrame({
    'Name': ['Luke','Gina','Sam','Emma'],
    'Status': ['Father', 'Mother', 'Son', 'Daughter'],
    'Birthyear': [1976, 1984, 2013, 2016],
})

df['age'] = df['Birthyear'].apply(lambda x: 2021-x)
print(df)

# filter age > 18
filtered_age=list(filter(lambda x: x>18, df['age']))
print(f'filteredAge:{filtered_age}')

df['double_age'] = df['age'].map(lambda x: x*2)
print(df)

df[['Name','Status']] = df.apply(lambda x: x[['Name','Status']].str.lower(), axis=1)
print(df)

#Assigning names to lambda functions are bad practices
# #Bad - Passing functions with single arguements inside lambda fn
# map(lambda x:abs(x), list_3)
# #Good
# map(abs, list_3)
# #Good
# map(lambda x: pow(x, 2), float_nums)


#Conditional Lambda statement
df['Gender'] = df['Status'].map(lambda x: 'Male' if x=='father' or x=='son' else 'Female')

