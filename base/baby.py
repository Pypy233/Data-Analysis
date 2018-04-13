import pandas as pd

names1880 = pd.read_csv('/Users/py/Downloads/pydata-book-2nd-edition/datasets'
                        '/babynames/yob1880.txt', names=['name', 'sex', 'births'])


print(names1880)
print()
# In this case, the sum is about birth
print(names1880.groupby('sex').sum())
print()
print(names1880.groupby('sex').births.sum())
print()
pieces = []
for year in range(1880, 2011):
    frame = pd.read_csv('/Users/py/Downloads/pydata-book-2nd-edition/datasets/babynames'
                        '/yob%d.txt' % year, names=['name', 'sex', 'birth'])
    frame['year'] = year
    pieces.append(frame)

names = pd.concat(pieces, ignore_index=True)
print(names)

total_births = names.pivot_table('birth', index='year', columns='sex', aggfunc='sum')
print(total_births.tail())
print()
total_births.plot(title='Total births by sex')


def add_prop(group = total_births):
    group['prop'] = births / births.sum()
    return group


names = names.groupby(['year', 'sex']).apply(add_prop)