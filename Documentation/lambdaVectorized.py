import pandas as pd
old = pd.read_csv('user_reviews.csv')
new = pd.read_csv('user_reviews.csv')

# if then elif else (new)
# create new column
new['qualitative_rating'] = ''
# assign 'qualitative_rating' based on 'grade' with .loc
new.loc[new.grade < 5, 'qualitative_rating'] = 'bad'
new.loc[new.grade == 5, 'qualitative_rating'] = 'ok'
new.loc[new.grade > 5, 'qualitative_rating'] = 'good'

# create column based on other column (old)
# create new column
old['len_text'] = ''
# calculate length of column value with loop
for index in old.index:
    old.loc[index, 'len_text'] = len(old.loc[index, 'text'])

# create column based on other column (new)
# create new column
new['len_text'] = ''
# calculate length of column value by converting to str
new['len_text'] = new['text'].str.len()

